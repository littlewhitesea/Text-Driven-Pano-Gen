import torch
from torchvision import transforms
from torchvision.io import read_image
from torchmetrics.image.kid import KernelInceptionDistance
from pathlib import Path

# Initialize KID metric
kid = KernelInceptionDistance(subset_size=50)

# Preprocessing: Resize images to match KID requirements (299x299)
transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.Lambda(lambda img: img if img.shape[0] == 3 else img.expand(3, -1, -1)),  # Ensure 3 channels
])

def load_images_from_folder(folder_path):
    """Load all images from a folder and apply preprocessing."""
    images = []
    for image_path in Path(folder_path).rglob("*.*"):  # Read all files in the folder
        img = read_image(str(image_path))  # Read image as a tensor
        img = transform(img)  # Apply resizing and ensure 3 channels
        images.append(img)
    return torch.stack(images)  # Combine all images into a single tensor

# Define folder paths
real_folder = "Path_of_Folder_Containing_GT_CMP_Images"
fake_folder = "Path_of_Folder_Containing_Generated_CMP_Images"

# Load images from folders
real_images = load_images_from_folder(real_folder)
fake_images = load_images_from_folder(fake_folder)

# Update KID metric with all real and fake images at once
kid.update(real_images, real=True)
kid.update(fake_images, real=False)

# Compute KID
kid_mean, kid_std = kid.compute()
print(f"KID Mean: {kid_mean}")
print(f"KID Standard Deviation: {kid_std}")
