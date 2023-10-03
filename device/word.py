import struct

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
     
    def to_short(self):
        buf = bytes([self.lo_value, self.hi_value])
        
        return struct.unpack('<h',buf)[0]
    
    def to_ushort(self):
        buf = bytes([self.lo_value, self.hi_value])
        
        return struct.unpack('<H',buf)[0]
    
   
        