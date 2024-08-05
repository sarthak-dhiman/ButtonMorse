from PIL import Image

def convert_image_to_pixel_array(image_path, width, height):
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')

    # Resize the image to the desired dimensions
    image = image.resize((width, height))

    # Convert the image to a pixel array
    pixel_array = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = image.getpixel((x, y))
            # Convert pixel value to 0 (black) or 1 (white)
            row.append(1 if pixel > 128 else 0)
        pixel_array.append(row)

    return pixel_array

# Path to your image
image_path = 'D:\ButtonMorse\ButtonMorse_git\pixil-frame-0.bmp'

# Dimensions of the OLED display
width = 128
height = 64

# Convert the image to a pixel array
pixel_logo = convert_image_to_pixel_array(image_path, width, height)

# Print the pixel array (optional)
for row in pixel_logo:
    print(row)
