import cv2
import numpy as np

# Load the original image
img = cv2.imread('maze_image.png')

# Get the image dimensions
height, width = img.shape[:2]

# Rotate the image to the desired orientation
angle = 1# Example: rotate counter-clockwise by 15 degrees
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

# Get new dimensions after rotation
rotated_height, rotated_width = rotated_img.shape[:2]

# Define crop parameters based on the rotated image
crop_height = rotated_height // 2  # Half the rotated height
crop_width = rotated_width // 2    # Half the rotated width
crop_left = 70    # Crop more from the left
crop_right = 112   # Crop more from the right
crop_top = 0     # Crop more from the top
crop_bottom = 36  # Crop more from the bottom

# Calculate cropping boundaries based on rotated image
top_left_y = (rotated_height - crop_height) // 2
top_left_y = max(0, top_left_y + crop_top)  # Crop more from the top
top_left_x = (rotated_width - crop_width) // 2
top_left_x = max(0, top_left_x + crop_left)  # Crop more from the left
bottom_right_y = top_left_y + crop_height
bottom_right_y = min(rotated_height, bottom_right_y - crop_bottom)  # Crop more from the bottom
bottom_right_x = top_left_x + crop_width
bottom_right_x = min(rotated_width, bottom_right_x - crop_right)  # Crop more from the right

# Define the amount to expand the crop by (e.g., 50 pixels)
expand_size = 48

# Adjust the boundaries to crop a larger area
top_left_y = max(0, top_left_y - expand_size)
top_left_x = max(0, top_left_x - expand_size)
bottom_right_y = min(height, bottom_right_y + expand_size)
bottom_right_x = min(width, bottom_right_x + expand_size)

# Crop the rotated image
cropped_img = rotated_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

# Convert to grayscale
gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold
# Pixels above 127 become white (255), and below become black (0)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Save and display the cropped image
cv2.imwrite('Extract_maze.png', binary)
cv2.imshow('Extract maze', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
