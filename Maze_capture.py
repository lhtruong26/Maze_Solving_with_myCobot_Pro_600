import cv2
import time

def capture_maze_image_from_camera(save_path='maze_image.png', capture_duration=5):
    # Initialize the camera (usually 0 for the default webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened correctly
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Record the start time
    start_time = time.time()

    # Capture frames for the given duration
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # If the frame was not read properly, break the loop
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Display the captured frame in a window (optional)
        cv2.imshow('Camera - Capture Maze Image', frame)

        # Check if the time has passed the capture duration
        if time.time() - start_time >= capture_duration:
            print("Capture time elapsed. Saving the maze image.")
            # Save the captured image to the specified file path
            cv2.imwrite(save_path, frame)
            break

        # Wait for 1ms and check if the user presses 'q' to quit early (optional)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Capture interrupted by user.")
            break

    # Release the camera and close the display window
    cap.release()
    cv2.destroyAllWindows()

# Example usage
capture_maze_image_from_camera(save_path='maze_image.png', capture_duration=1)
