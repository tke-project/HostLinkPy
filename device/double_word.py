import struct
from device import word as w

#ワードを定義するクラス

class DoubleWord:
    
    address = ""
    hi_word = w.Word('',0,0)
    lo_word = w.Word('',0,0)
    
    #コンストラクタ
    #address -- "MR001"などのアドレス番号
    #hi_value -- 上位8バイト
    #lo_value -- 下位8バイト
    def __init__(self, address, hi_word, lo_word):
        self.address = address
        self.hi_word = hi_word
        self.lo_word = lo_word        
     
    def to_short(self):
        
        return self.lo_word.to_short()
    
    def to_ushort(self):
        
        return self.lo_word.to_ushort()
 
    def to_int(self):
        buf = bytes([self.lo_word.lo_value, self.lo_word.hi_value,
                    self.hi_word.lo_value, self.hi_word.hi_value])
        
        return struct.unpack('<i', buf)
    
    def to_uint(self):
        buf = bytes([self.lo_word.lo_value, self.lo_word.hi_value,
                    self.hi_word.lo_value, self.hi_word.hi_value])
        
        return struct.unpack('<I', buf)

    def to_float(self):
        buf = bytes([self.lo_word.lo_value, self.lo_word.hi_value,
                    self.hi_word.lo_value, self.hi_word.hi_value])
        
        return struct.unpack('<f', buf)
   