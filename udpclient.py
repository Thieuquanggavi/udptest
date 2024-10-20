import socket

# Tạo một UDP client
def udp_client():
    # Khởi tạo socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Địa chỉ của server
    server_address = ("localhost", 12345)

    try:
        # Gửi dữ liệu đến server
        message = "Xin chào từ client!"
        print(f"Gửi: {message}")
        client_socket.sendto(message.encode(), server_address)

        # Nhận phản hồi từ server
        data, server = client_socket.recvfrom(4096)
        print(f"Nhận phản hồi từ server: {data.decode()}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    udp_client()
