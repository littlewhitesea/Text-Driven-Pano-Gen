# This is an unofficial implementation of
# Discontinuity Score from https://arxiv.org/pdf/2407.18207.
# ECCV 2024: Geometry Fidelity for Spherical Images


import os
import torch
import torch.nn.functional as F
import torchvision.transforms.functional as TF
from PIL import Image


def detect_seam(image):
    """
    Detects vertical seams (boundaries) in an image by convolving
    a concatenated boundary region with a Scharr filter.

    Args:
        image (torch.Tensor): A PyTorch tensor representing the image (C, H, W).

    Returns:
        torch.Tensor: A tensor representing the convolved output (H, 4).
    """
    # Ensure the image is a PyTorch tensor and has the correct dimensions
    if not isinstance(image, torch.Tensor):
        raise TypeError("Input image must be a PyTorch tensor.")
    if image.ndim != 3:
        raise ValueError("Input image must be 3-dimensional (C, H, W).")
    if image.shape[2] < 6:
        raise ValueError("Input image width must be at least 6 pixels.")

    # Convert to grayscale
    if image.shape[0] == 3:  # If RGB
        grayscale_image = (
                0.299 * image[0, :, :] + 0.587 * image[1, :, :] + 0.114 * image[2, :, :]
        ).unsqueeze(0)
    else:
        grayscale_image = image

    # Extract boundaries and concatenate
    left_boundary = grayscale_image[:, :, -3:]
    right_boundary = grayscale_image[:, :, :3]
    boundary_region = torch.cat([left_boundary, right_boundary], dim=2)

    # Apply Scharr kernel
    scharr_kernel = torch.tensor(
        [[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]], dtype=image.dtype, device=image.device
    ).view(1, 1, 3, 3)
    convolved_output = F.conv2d(boundary_region, scharr_kernel, padding=(1, 0))

    return convolved_output.squeeze(0)


def compute_DS(a_hat, c=0.1):
    """
    Computes the Discontinuity Score (DS) from a seam tensor.

    Args:
        a_hat (torch.Tensor): A seam tensor of size (H, 4).
        c (float): A small constant to avoid division by zero.

    Returns:
        float: The computed DS value.
    """
    if a_hat.shape[1] != 4:
        raise ValueError("Input tensor a_hat must have a size of (H, 4).")

    H = a_hat.size(0)  # Number of rows
    term1 = torch.abs(a_hat[:, 1]) / (torch.abs(a_hat[:, 0]) + c)
    term2 = torch.abs(a_hat[:, 2]) / (torch.abs(a_hat[:, 3]) + c)
    summation = torch.sum(term1 + term2)
    return (1 / (2 * H)) * summation.item()


def calculate_average_DS(folder_path):
    """
    Calculates the average Discontinuity Score (DS) for all images in a folder.

    Args:
        folder_path (str): Path to the folder containing RGB images.

    Returns:
        float: The average DS for all images in the folder.
    """
    total_DS = 0
    image_count = 0

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Load and process the image
            img = TF.to_tensor(Image.open(file_path))
            seam = detect_seam(img)
            DS_value = compute_DS(seam)

            print(f"Processed {filename}: DS = {DS_value:.4f}")
            total_DS += DS_value
            image_count += 1
        except Exception as e:
            print(f"Skipping {filename}: {e}")

    if image_count == 0:
        raise ValueError("No valid images found in the folder.")

    # Compute the average DS
    average_DS = total_DS / image_count
    return average_DS


# Specify the folder path
folder_path = "Path_of_Folder_Containing_Images"

### Example of Dataset Structure ###
### */Path_of_Folder_Containing_Images/ ###
### */Path_of_Folder_Containing_Images/xxxx.png (jpg, etc) ###

# Calculate and print the average DS
average_DS = calculate_average_DS(folder_path)
print(f"Average Discontinuity Score (DS) for all images in the folder: {average_DS:.4f}")
