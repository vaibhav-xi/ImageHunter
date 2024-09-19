import os
from PIL import Image

def is_image_healthy(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()  # Check if it's corrupted
        return True
    except Exception as e:
        return False

def delete_corrupted_images(directory, delete_image):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the file is an image by extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            if not is_image_healthy(file_path):
                
                if delete_image:
                    
                    os.remove(file_path)
                    print(f"Deleting corrupted image: {file_path}")
                    
                else:
                    print(f"Corrupted image path: {file_path}")

if __name__ == "__main__":
    
    try:
        
        current_directory = os.getcwd()
        
        print("""
            1. Print Names of Corrupted Images
            2. Find and Delete
            """)
        
        i = int(input("Selected Option >> "))
        
        if i == 1:
            
            delete_corrupted_images(current_directory, False)
            
        elif i == 2:
            
            delete_corrupted_images(current_directory, True)
            
        else:
            
            print("Incorrect Option")
            
    except Exception as e:
        
        print(f"Unable to Run Script, error --> {e}")
