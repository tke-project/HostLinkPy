import socket

DELIMITAR = "\r"

class KV:
    
    ip = "192.168.0.1"
    port = 8501
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(2)

        try:
            self.client.connect((self.ip, self.port))
            return True
        
        except socket.error:
            return False
        
    def read_device(self, name, suffix):
               
        s = "RD "
        s += name + suffix
        s += DELIMITAR
        
        buf = s.encode(encoding='shift-jis')
        
        self.client.send(buf)
        
        recv = self.client.recv(512)
        
        res = bytes.decode(recv, encoding='shift-jis')
        res = res.replace('\r\n', '')
        return res