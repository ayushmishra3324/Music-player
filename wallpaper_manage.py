from PIL import Image
import os

def convert_images_to_gif(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Iterate through each file in the input folder
    for file in files:
        # Check if the file is an image (you can adjust the extensions as needed)
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            # Open the image file
            image_path = os.path.join(input_folder, file)
            image = Image.open(image_path)
            resized_image = image.resize((400, 240))
            # Create the output file path with the .gif extension
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.gif')

            # Convert and save the image as GIF format
            resized_image.save(output_path, format='GIF')

# Example usage
input_folder = 'wallpaper'
output_folder = 'new'

convert_images_to_gif(input_folder, output_folder)
