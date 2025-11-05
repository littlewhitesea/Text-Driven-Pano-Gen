import torch
from torchvision import transforms
from torchvision.io import read_image
from torchmetrics.multimodal.clip_score import CLIPScore
from pathlib import Path


clip_score = CLIPScore(model_name_or_path="openai/clip-vit-large-patch14")


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Lambda(lambda img: img if img.shape[0] == 3 else img.expand(3, -1, -1)),
    transforms.ConvertImageDtype(torch.float32),
])


def load_images_and_prompts(image_folder, prompt_file):
    """Load images and their corresponding text prompts."""
    # Read text prompts
    with open(prompt_file, 'r') as f:
        prompts = [line.strip() for line in f.readlines()]

    images = []
    for idx, image_path in enumerate(sorted(Path(image_folder).rglob("*.*"))):
        img = read_image(str(image_path))
        img = transform(img)
        images.append(img)

    return torch.stack(images), prompts


# Specify folder paths and text prompt file
image_folder = "Path_of_Folder_Containing_Images"
prompt_file = "Path_of_Text_Prompt_File"


images, prompts = load_images_and_prompts(image_folder, prompt_file)


clip_scores = []
for img, text in zip(images, prompts):
    score = clip_score(img, text)  # Compute CLIP score for each image-text pair
    clip_scores.append(score.item())

# Calculate average CLIP score
average_clip_score = sum(clip_scores) / len(clip_scores)
print(f"Average CLIP Score: {average_clip_score:.4f}")
