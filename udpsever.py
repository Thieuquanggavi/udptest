import socket

# Tạo một UDP server
def udp_server():
    # Khởi tạo socket với loại SOCK_DGRAM (UDP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Cấu hình địa chỉ và cổng cho server
    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    print("Server UDP đã sẵn sàng và đang lắng nghe...")

    while True:
        # Nhận dữ liệu từ client
        data, client_address = server_socket.recvfrom(4096)
        print(f"Đã nhận được {data.decode()} từ {client_address}")

        # Phản hồi lại client
        response = f"Server đã nhận được thông điệp: {data.decode()}"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_server()
