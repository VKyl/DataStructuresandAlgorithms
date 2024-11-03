from PIL import Image

# Load an image
image_path = './data/test.jpg'
image = Image.open(image_path)

# Convert to different color spaces
rgb_image = image.convert('RGB')
cmyk_image = image.convert('CMYK')
# hsv_image = image.convert('HSV')
lab_image = image.convert('LAB')
ycbcr_image = image.convert('YCbCr')
grayscale_image = image.convert('L')

rgb_image.save('output_rgb.jpg')
cmyk_image.save('output_cmyk.jpg')
lab_image.save('output_lab.jpg')
ycbcr_image.save('output_ycbcr.jpg')
grayscale_image.save('output_grayscale.jpg')
