import cv2
import numpy as np
import socket
import time

# Maze properties
top = 1
right = 2
left = 4
bottom = 8
num_rows = 4  # Number of rows in the maze
num_cols = 4  # Number of columns in the maze



def process_maze_image_to_matrix(image_path, num_rows, num_cols):
    # Load and preprocess the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  # Binarize the image (walls are white)

    # Determine the size of each square
    cell_height = binary.shape[0] // num_rows
    cell_width = binary.shape[1] // num_cols

    # Initialize the maze matrix
    maze = np.zeros((num_rows, num_cols), dtype=int)

    # Process each square
    for row in range(num_rows):
        for col in range(num_cols):
            # Determine the square boundaries
            top_row = row * cell_height
            bottom_row = (row + 1) * cell_height
            left_col = col * cell_width
            right_col = (col + 1) * cell_width

            # Extract edges
            cell_value = 0
            if np.any(binary[top_row, left_col:right_col] == 255):  # Top edge
                cell_value += top
            if np.any(binary[top_row:bottom_row, right_col - 1] == 255):  # Right edge
                cell_value += right
            if np.any(binary[bottom_row - 1, left_col:right_col] == 255):  # Bottom edge
                cell_value += bottom
            if np.any(binary[top_row:bottom_row, left_col] == 255):  # Left edge
                cell_value += left

            # Assign the value to the maze matrix
            maze[row, col] = cell_value

    return maze

# Example usage
image_path = 'maze_image.png'  # Replace with your maze image path
maze = process_maze_image_to_matrix(image_path, num_rows, num_cols)

# Display the resulting matrix
print("Maze Matrix:")
print(maze)

rows, cols = maze.shape

# Define movement deltas for directions
directions = {
    "top": (-1, 0, top, bottom),  # Move top, reverse is bottom
    "right": (0, 1, right, left),  # Move right, reverse is left
    "bottom": (1, 0, bottom, top),  # Move bottom, reverse is top
    "left": (0, -1, left, right),  # Move left, reverse is right
}

# Function to check possible moves from a given cell
def check_possible_moves(maze, current):
    row, col = current
    possible_moves = []

    # Loop through all directions
    for direction, (dr, dc, bit, reverse_bit) in directions.items():
        next_row, next_col = row + dr, col + dc

        # Check if the next cell is within bounds
        if 0 <= next_row < maze.shape[0] and 0 <= next_col < maze.shape[1]:
            # Check if the current cell allows movement in the given direction
            if maze[row, col] & bit:
                # Check if the next cell allows movement back (reverse direction)
                if maze[next_row, next_col] & reverse_bit:
                    possible_moves.append((next_row, next_col))

    print(f"Possible moves from {current}: {possible_moves}")
    return possible_moves

def solve_maze(maze, start, end, path = None, visited=None):
    if path is None:
        path = []  # Initialize the path if not already provided

    if visited is None:
        visited = set()  # Initialize the visited set if not already provided

    current = start
    row, col = current

    # If we've reached the end, return the path
    if current == end:
        return path + [current]

    # Mark the current cell as visited
    visited.add(current)

    # Get all possible moves from the current cell
    possible_moves = check_possible_moves(maze, current)

    # Try all possible moves
    for move in possible_moves:
        if move not in visited:  # Avoid revisiting the same cell
            new_path = path + [current]  # Add the current cell to the path
            result = solve_maze(maze, move, end, new_path, visited)  # Recursively call for the next cell
            if result:  # If a path is found, return it
                return result

    # If no path is found, return None
    return None

# Find starting point (first row with top open)
start = (0,1)
end = (3,2)
# for col in range(cols):
#     if maze[0, col] & top:
#         end = (0, col)
#         print(f"Start: {start}")
#         break

# Find ending point (last row with bottom open)

# for col in range(cols):
#     if maze[-1, col] & bottom:
#         start = (rows - 1, col)
#         print(f"End: {end}")
#         break

# Example usage
# current = start  # Example current position in the maze
# possible_moves = check_possible_moves(maze, current)

path = solve_maze(maze, start, end)

# Display the solution path
if path:
    print(f"Path found: {path}")
else:
    print("No path found.")


spot2_03 = "set_angles(56.23,-131.06,-125.10,-13.84,90.00,48.99, 500)"
spot2_02 = "set_angles(51.25,-129.08,-119.40,-20.12,90.00,44.91, 500)"
spot2_01 = "set_angles(47.98,-135.46,-110.71,-25.4,90.00,40.73, 500)"
spot2_00 = "set_angles(44.14,-138.90,-101.59,-30.89,90.00,37.45, 500)"
spot2_13 = "set_angles(58.65,-132.31,-119.91,-17.41,90.00,52.49, 500)"
spot2_12 = "set_angles(54.90,-134.88,-112.86,-22.25,90.00,47.65, 500)"
spot2_11 = "set_angles(50.89,-138.22,-104.51,-27.96,90.00,43.73, 500)"
spot2_10 = "set_angles(47.44,-142.12,-96.44,-30.89,90.00,37.45, 500)"
spot2_23 = "set_angles(61.01,-134.29,-113.59,-21.13,90.00,58.08, 500)"
spot2_22 = "set_angles(57.12,-142.4,-104.42,-24.96,90.00,58.08, 500)"
spot2_21 = "set_angles(53.1,-140.44,-98.43,-31.36,90.00,46.92, 500)"
spot2_20 = "set_angles(49.73,-144.41,-89.37,-37.26,90.00,43.53, 500)"
spot2_33 = "set_angles(63.01,-136.54,-106.91,-24.9,90.00,58.08, 500)"
spot2_32 = "set_angles(59.03,-139.48,-99.67,-29.92,90.00,53.70, 500)"
spot2_31 = "set_angles(55.21,-142.96,-91.60,-35.15,90.00,49.78, 500)"
spot2_30 = "set_angles(52.21,-147.14,-83.03,-40.51,90.00,46.42, 500)"
coordinates2 = np.array(
    [
        [spot2_00, spot2_01, spot2_02, spot2_03],
        [spot2_10, spot2_11, spot2_12, spot2_13],
        [spot2_20, spot2_21, spot2_22, spot2_23],
        [spot2_30, spot2_31, spot2_32, spot2_33]
    ])


def send_tcp_packet(server_ip, server_port, message):
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")

        # Send the message
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        # Optionally receive a response (if server sends one)
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {response}")

    except socket.error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")



if __name__ == "__main__":
    # Replace with the correct IP and port
    SERVER_IP = "192.168.1.159"
    SERVER_PORT = 5001

    MESSAGE = "set_angles(8.63,-130.20,-128.53,-11.27,90.00,1.38, 500)"  # home position
    send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
    time.sleep(3)



    for r, c in path:
        element = coordinates2[r][c]
        print(element)
        MESSAGE = element
        send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
        time.sleep(4)

    MESSAGE = "set_angles(8.63,-130.20,-128.53,-11.27,90.00,1.38, 500)"  # home position
    send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
    time.sleep(3)

