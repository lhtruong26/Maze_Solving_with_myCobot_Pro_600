import socket
import time

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
    MESSAGE = "set_angles(8.63,-130.20,-128.53,-11.27,90.00,1.38, 500)"
    send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
    time.sleep(5)
    MESSAGE = "set_angles(40.53,-140.17,-98.86,-30.97,90.00,33.29, 500)"
    send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
    time.sleep(5)
    MESSAGE = "set_angles(67.36,-133.33,-117.48,-19.19,90.00,60.11, 500)"
    send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
    # time.sleep(5)
    # MESSAGE = "set_angles(68.41,-135.99,-109.75,-24.26,90.00,61.17,500)"
    # send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)
    # time.sleep(5)
    # MESSAGE = "set_angles(70.99, -138.49, -103.11, -28.40, 90.00, 63.74, 500)"
    # send_tcp_packet(SERVER_IP, SERVER_PORT, MESSAGE)