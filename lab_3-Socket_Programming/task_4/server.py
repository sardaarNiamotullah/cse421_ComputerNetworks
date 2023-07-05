import socket

HEADER = 16
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server is listening...")
conn, addr = server.accept()
connected = True

while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            conn.send("Goodbye".encode(FORMAT))
        else:
            msg = int(msg)

            if msg <= 40:
                conn.send(f"You receives {200*msg}".encode(FORMAT))
            else:
                iniSalary = 200*40
                extraSalary = (msg - 40) * 300
                totalSaraly = 8000+iniSalary+extraSalary
                conn.send(f"You receives {totalSaraly}".encode(FORMAT))
conn.close()