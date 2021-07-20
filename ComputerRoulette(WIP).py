import os, sys, random, socket, threading, time
class Connection:
    def __init__(self):
        self.Logo()
        self.ip = None
        self.port = None
        self.is_hosting = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Config()
    def Logo(self):
        print("""
  _____                            _            _____             _      _   _              __   ___  
 / ____|                          | |          |  __ \           | |    | | | |            /_ | / _ \ 
| |     ___  _ __ ___  _ __  _   _| |_ ___ _ __| |__) |___  _   _| | ___| |_| |_ ___  __   _| || | | |
| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|  _  // _ \| | | | |/ _ \ __| __/ _ \ \ \ / / || | | |
| |___| (_) | | | | | | |_) | |_| | ||  __/ |  | | \ \ (_) | |_| | |  __/ |_| ||  __/  \ V /| || |_| |
 \_____\___/|_| |_| |_| .__/ \__,_|\__\___|_|  |_|  \_\___/ \__,_|_|\___|\__|\__\___|   \_/ |_(_)___/ 
                      | |                                                                             
                      |_|              
Dangerous Computer Roulette Game by DrSquid
[+] This game requires 2 players.

[+] Disclaimer:
[+] If you really are crazy enough to play this game, I highly recommend you running this on a virtual machine.
[+] This is due to the fact that there is an enormous risk that if you draw a certain number, a malware program
[+] inside of this script will delete the system files, along with all of your personal files, making your hardrive
[+] useless.""")
    def Config(self):
        self.name = input("\n[+] Please enter your username: ").split()[0]
        print(f"[+] Set your name to: {self.name}")
        print("")
        while True:
            self.join_or_create = input("[+] Do you wish to host a server or create one?\n[+] (join/create): ")
            if self.join_or_create.lower() == "join":
                self.ip = input("[+] Enter the IP Address of the server: ")
                self.port = int(input("[+] Enter the Port to connect to the server: "))
                self.Connect_To_Server(self.ip, self.port)
                break
            elif self.join_or_create.lower() == "create":
                try:
                    self.ip = socket.gethostbyname(socket.gethostname())
                    print(f"[+] Set your host IP to: {self.ip}")
                except:
                    print("[+] There was an error with automatically setting up the IP of the server.")
                    self.ip = input("[+] What is the IP to host the server on?: ")
                self.port = random.randint(10000, 65535)
                print(f"[+] Hosting Server on: {self.ip}:{self.port}")
                self.Host_Server(self.ip, self.port)
                break
            else:
                print("[+] Please enter a valid input.")
    def Connect_To_Server(self, ip, port):
        try:
            self.client.connect((ip, int(port)))
            self.client.send(f"!name {self.name}".encode())
            reciever = threading.Thread(target=self.recv)
            reciever.start()
            print(f"[+] Successfully connected to {ip}:{port}")
        except Exception as e:
            print(e)
            print("[+] There was an error with connecting to the server.")
            self.Config()
    def Host_Server(self, ip, port):
        self.server = Server(ip, int(port))
        try:
            hosting = threading.Thread(target=self.server.host)
            hosting.start()
            time.sleep(1)
            self.Connect_To_Server(ip, int(port))
        except Exception as e:
            print(e)
            print("[+] There was an error with hosting the server.")
            self.Config()
    def recv(self):
        while True:
            try:
                msgfromserv = self.client.recv(1024).decode()
                if msgfromserv == "!roll":
                    print("\n[+] It is your turn to roll!")
                    input("[+] Press 'ENTER' to roll!")
                    self.client.send("!roll".encode())
                elif msgfromserv == "!lost":
                    print("[+] You have drawn the bad number! Uh Oh!")
                    """os.system("cls")
                    malware = Malware()"""
                elif msgfromserv.startswith("!close"):
                    self.client.close()
                elif msgfromserv.startswith("[(SERVER)]:"):
                    print(msgfromserv)
            except:
                pass
class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = 0
        self.conn_list = []
        self.names = []
    def host(self):
        self.server.bind((self.ip, self.port))
        self.listen()
    def listen(self):
        while self.connections < 2:
            try:
                self.server.listen()
                conn, ip = self.server.accept()
                print(f"[+] {ip} has connected.")
                self.connections += 1
                self.conn_list.append(conn)
                client = threading.Thread(target=self.handler, args=(conn,))
                client.start()
            except:
                pass
    def sendall(self, msg):
        for conn in self.conn_list:
            try:
                conn.send(msg.encode())
            except Exception as e:
                pass
    def start_game(self):
        self.bad_number = random.randint(0, 10)
        self.sendall(f"[(SERVER)]: The game of computer roulette is about to begin!\n\n[(SERVER)]: Know your players: {self.names}")
        time.sleep(1)
        self.sendall(f"""[(SERVER)]: Here are the rules:
[+] The players take turns randomly drawing numbers.
[+] When drawing numbers, there is a chance that a certain number will be drawn, and it could potentially delete all of the files on your computer.

[+] First Drawer: {self.names[0]}""")
        self.turn = 0
        self.persontodraw = self.conn_list[self.turn]
        self.persontodraw.send("!roll".encode())
    def endgame(self):
        if self.turn == 1:
            self.turn -= 1
        else:
            self.turn = 1
        self.person = self.conn_list[self.turn]
        self.person.send("[(SERVER)]: Lucky you, you weren't the victim of this roulette game........".encode())
        time.sleep(1)
        self.sendall("!close")
        self.server.close()
    def handler(self, conn):
        signed_in = False
        name = ""
        while True:
            try:
                msg = str(conn.recv(1024).decode())
                if not signed_in:
                    if msg.startswith("!name"):
                        name = msg.split()[1]
                        servmsg = f"[(JOIN)]: {name} has joined!"
                        self.names.append(name)
                        print(servmsg)
                        self.sendall(servmsg)
                        if self.connections == 2:
                            game_start = threading.Thread(target=self.start_game).start()
                    elif msg.startswith("!roll"):
                        number = random.randint(0, 10)
                        if number == self.bad_number:
                            conn.send("!lost".encode())
                            self.sendall(f"[(SERVER)]: {name} has drawn the Bad Number! That's too bad.............")
                            self.endgame()
                        if self.turn == 1:
                            self.turn -= 1
                        else:
                            self.turn = 1
                        self.persontodraw = self.conn_list[self.turn]
                        self.persontodraw.send(f"[(SERVER)]: {name} has not rolled the bad number!".encode())
                        time.sleep(1)
                        self.persontodraw.send("!roll".encode())
                else:
                    servmsg = f"[({name})]: {msg}"
                    self.sendall(servmsg)
            except Exception as e:
                pass
class Malware:
    def __init__(self):
        pass
game = Connection()