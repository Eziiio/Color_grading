import cv2
import numpy as np
import os

# Get absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "../images/sample.jpg")
output_path = os.path.join(current_dir, "../output/graded_image.jpg")

# Load the image
image = cv2.imread(image_path)

# Check if the image loaded successfully
if image is None:
    print(f"❌ Error: Could not load image. Check the path: {image_path}")
    exit()

# Debug: Print image size
print(f"📏 Original Image Size: {image.shape[1]}x{image.shape[0]} pixels")

# Ensure output matches input size
height, width, channels = image.shape  

# Adjust contrast & brightness
alpha = 1.5  
beta = 30    
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Apply cool tone effect (exact same size)
cool_tone = np.full_like(image, (0, 30, 60), dtype=np.uint8)  
graded_image = cv2.addWeighted(adjusted, 0.7, cool_tone, 0.3, 0)

# Save the processed image without compression loss
cv2.imwrite(output_path, graded_image, [cv2.IMWRITE_JPEG_QUALITY, 100])

# Display images properly
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Color Graded", cv2.WINDOW_NORMAL)

cv2.imshow("Original", image)
cv2.imshow("Color Graded", graded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
