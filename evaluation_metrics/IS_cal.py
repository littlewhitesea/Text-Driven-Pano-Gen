import torch
from torchvision import transforms
from torchvision.io import read_image
from torchmetrics.image.inception import InceptionScore
from pathlib import Path

# Initialize InceptionScore metric
inception = InceptionScore()

# Preprocessing: Resize images to match Inception requirements (299x299)
transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.Lambda(lambda img: img if img.shape[0] == 3 else img.expand(3, -1, -1)),  # Ensure 3 channels
])

def load_images_from_folder(folder_path):
    """Load all images from a folder and apply preprocessing."""
    images = []
    for image_path in Path(folder_path).rglob("*.*"):  # Read all files in the folder
        img = read_image(str(image_path))  # Read image as a tensor
        img = transform(img)  # Apply resizing and normalization
        images.append(img)
    return torch.stack(images)  # Combine all images into a single tensor

# Define the folder path for generated images
fake_folder = "Path_of_Folder_Containing_Images"

# Load generated images
fake_images = load_images_from_folder(fake_folder)

# Update InceptionScore metric with the fake images
inception.update(fake_images)

# Compute Inception Score
inception_score = inception.compute()
print(f"Inception Score: {inception_score}")
