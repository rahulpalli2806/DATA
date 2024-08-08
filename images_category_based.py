import os
import shutil

def organize_images(labels_dir, images_dir, output_dir):
    """
    Organizes and copies images based on the label filenames.

    Args:
        labels_dir: The directory containing the class subdirectories with label files.
        images_dir: The directory containing the .jpg image files.
        output_dir: The root directory where images will be organized.
    """
    # Iterate over each class directory in the labels directory
    for class_name in os.listdir(labels_dir):
        class_labels_dir = os.path.join(labels_dir, class_name)
        
        # Skip non-directory files
        if not os.path.isdir(class_labels_dir):
            continue

        # Create the output directory for the current class
        class_output_dir = os.path.join(output_dir, class_name)
        os.makedirs(class_output_dir, exist_ok=True)

        # Iterate over all label files in the current class folder
        for label_file in os.listdir(class_labels_dir):
            if not label_file.endswith('.txt'):
                continue
            
            # Extract filename without extension
            base_filename = os.path.splitext(label_file)[0]
            image_filename = f"{base_filename}.tif"
            image_file_path = os.path.join(images_dir, image_filename)

            # # Print debug information
            # print(f"Processing label file: {label_file}")
            # print(f"Expected image file path: {image_file_path}")

            if os.path.exists(image_file_path):
                # Copy the image file to the output directory
                shutil.copy(image_file_path, class_output_dir)
                # print(f"Copied {image_filename} to {class_output_dir}")
            else:
                print(f"Image file {image_file_path} does not exist.")

# Define the directory paths
labels_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//classewise_labels//train//part1//"  # Directory containing class subdirectories
images_dir = r"D:\Object_Detection\DATA\FAIR1M\FAIR1M\train\part1\images"  # Directory containing .jpg image files
output_dir = "D://Object_Detection//DATA//FAIR1M//FAIR1M_DOTA_CORE_CLASS//classewise_images//train//part1//images//"  # Root directory where images will be organized

# Run the organization function
organize_images(labels_dir, images_dir, output_dir)
