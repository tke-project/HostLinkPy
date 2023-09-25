#リレーを定義するクラス

class Relay:
    
    address = ""
    value = False
    
    #コンストラクタ
    #address -- "MR001"などのアドレス番号
    #value -- True or False
    def __init__(self, address, value):
        self.address = address
        self.value = value