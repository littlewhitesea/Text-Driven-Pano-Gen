import subprocess
import os
from PIL import Image
import numpy as np
import py360convert

def convert_and_split_cubemap(input_dir, output_dir, width=256):
    """Converts equirectangular images to cubemaps and splits them into faces,
       organizing faces into separate directories."""

    os.makedirs(output_dir, exist_ok=True)

    # Create face directories once outside the loop
    face_dirs = {}  # Store face directory paths
    for face in ["F", "R", "B", "L", "U", "D"]:
        face_dirs[face] = os.path.join(output_dir, face)
        os.makedirs(face_dirs[face], exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            base_name, _ = os.path.splitext(filename)
            cubemap_path = os.path.join(output_dir, f"{base_name}_cubemap.png")

            command = [
                "convert360",
                "e2c",
                input_path,
                cubemap_path,
                "--height", str(width),
                "--width", str(width)
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Converted: {filename} to {cubemap_path}")

                try:
                    cube_dice = np.array(Image.open(cubemap_path))
                    cube_h = py360convert.cube_dice2h(cube_dice)
                    cube_dict = py360convert.cube_h2dict(cube_h)

                    for face, img_array in cube_dict.items():
                        img = Image.fromarray(img_array.astype(np.uint8))
                        output_face_path = os.path.join(face_dirs[face], f"{base_name}_{face}.png")
                        img.save(output_face_path)  # Save in the specific face directory
                    print(f"Saved cube faces to respective directories.")

                except Exception as e:
                    print(f"Error splitting cubemap {cubemap_path}: {e}")

            except subprocess.CalledProcessError as e:
                print(f"Error converting {filename}: {e}")
            except FileNotFoundError:
                print("Error: convert360 not found. Make sure it's installed and in your PATH.")
                return

### Remember to install the package below ###
### pip install py360convert ###

# Example usage (replace with your paths):
input_directory = "Path_of_Folder_Containing_ERP_Images"
output_directory = "Path_of_Folder_Containing_CMP_Images"
convert_and_split_cubemap(input_directory, output_directory)