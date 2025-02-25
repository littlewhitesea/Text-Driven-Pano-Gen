# This is an unofficial implementation
# of OmniFID from https://arxiv.org/pdf/2407.18207.
# ECCV 2024: Geometry Fidelity for Spherical Images


import torch
from torchvision import transforms
from torchvision.io import read_image
from torchmetrics.image.fid import FrechetInceptionDistance
from pathlib import Path

import pdb

# Preprocessing: Resize images to match FID requirements (299x299)
transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.Lambda(lambda img: img if img.shape[0] == 3 else img.expand(3, -1, -1)),  # Ensure 3 channels
])

def load_images_from_folder(folder_path):
    """Load all images from a folder and apply preprocessing."""
    images = []
    for image_path in Path(folder_path).rglob("*.*"):  # Read all files in the folder
        # pdb.set_trace()
        img = read_image(str(image_path))  # Read image as a tensor
        img = transform(img)  # Apply resizing and normalization
        images.append(img)
    return torch.stack(images)  # Combine all images into a single tensor

def calculate_fid_for_face(real_folder, fake_folder, face_region):
    """Calculate FID for a specific face region."""
    fid = FrechetInceptionDistance(feature=2048)  # Initialize FID metric
    real_images = load_images_from_folder(Path(real_folder) / face_region)
    fake_images = load_images_from_folder(Path(fake_folder) / face_region)
    fid.update(real_images, real=True)
    fid.update(fake_images, real=False)
    return fid.compute()

def main():
    # Define folder paths
    real_folder = "Path_of_Folder_Containing_GT_CMP_Images"
    fake_folder = "Path_of_Folder_Containing_Generated_CMP_Images"

    ### Example of Dataset Structure ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/ ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/U/xxxx.png (jpg, etc) ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/F/xxxx.png (jpg, etc) ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/R/xxxx.png (jpg, etc) ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/B/xxxx.png (jpg, etc) ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/L/xxxx.png (jpg, etc) ###
    ### */Path_of_Folder_Containing_GT_CMP_Images/D/xxxx.png (jpg, etc) ###

    # Face regions
    face_regions = ["U", "F", "R", "B", "L", "D"]

    # Calculate FID scores for each face region
    fid_scores = {}
    for face in face_regions:
        fid_scores[face] = calculate_fid_for_face(real_folder, fake_folder, face)

    # Calculate frontal face FID (average of F, R, B, L)
    frontal_fid = 0.25 * (fid_scores["F"] + fid_scores["R"] + fid_scores["B"] + fid_scores["L"])

    # Calculate OmniFID
    omni_fid = (fid_scores["U"] + frontal_fid + fid_scores["D"]) / 3

    # Print results
    print(f"Individual FID Scores: {fid_scores}")
    print(f"Frontal FID: {frontal_fid}")
    print(f"OmniFID: {omni_fid}")

if __name__ == "__main__":
    main()
