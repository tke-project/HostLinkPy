#ワードを定義するクラス

class Word:
    
    address = ""
    hi_value = 0
    lo_value = 0
    
    #コンストラクタ
    #address -- "MR001"などのアドレス番号
    #hi_value -- 上位8バイト
    #lo_value -- 下位8バイト
    def __init__(self, address, hi_value, lo_value):
        self.address = address
        self.hi_value = hi_value
        self.lo_value = lo_value
        
    def to_int16(self):
        bytes = [self.lo_value, self.hi_value]
        
        return int.from_bytes(bytes, 'little')