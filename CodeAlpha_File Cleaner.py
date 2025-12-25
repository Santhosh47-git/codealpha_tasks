import os
import shutil

def organize_images(source_folder):
    # Create the destination folder if it doesn't exist
    target_folder = os.path.join(source_folder, "Organized_Images")
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Created directory: {target_folder}")

    # Loop through all files in the source folder
    count = 0
    for filename in os.listdir(source_folder):
        # Check for image extensions
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            
            # Move the file
            shutil.move(source_path, target_path)
            print(f"Moved: {filename}")
            count += 1

    print(f"\nTask Complete! {count} images moved to 'Organized_Images'.")

# Example usage:
# organize_images("C:/Users/YourName/Desktop")