import struct
from device import word as w

# ワードを定義するクラス


class DoubleWord:

    # コンストラクタ
    # address -- "MR001"などのアドレス番号
    # hi_value -- 上位8バイト
    # lo_value -- 下位8バイト
    def __init__(self, address, hi_word, lo_word):
        self.address = address
        self.hi_word = hi_word
        self.lo_word = lo_word

    def short(self):

        return self.lo_word.to_short()[0]

    def s(self):
        return self.short()

    def ushort(self):

        return self.lo_word.to_ushort()[0]

    def u(self):
        return self.short()

    def int(self):
        buf = bytes([self.lo_word.lo_value, self.lo_word.hi_value,
                    self.hi_word.lo_value, self.hi_word.hi_value])

        return struct.unpack('<i', buf)[0]

    def l(self):
        return self.int()

    def uint(self):
        buf = bytes([self.lo_word.lo_value, self.lo_word.hi_value,
                    self.hi_word.lo_value, self.hi_word.hi_value])

        return struct.unpack('<I', buf)[0]

    def d(self):
        return self.uint()

    def float(self):
        buf = bytes([self.lo_word.lo_value, self.lo_word.hi_value,
                    self.hi_word.lo_value, self.hi_word.hi_value])

        return struct.unpack('<f', buf)[0]

    def f(self):
        return self.float()

    def hex(self):
        lo_str = self.lo_word.to_hex()
        hi_str = self.hi_word.to_hex()

        return hi_str + lo_str

    def bits(self):
        lo_bits = self.lo_word.to_bits()
        hi_bits = self.hi_word.to_bits()

        lo_bits.extend(hi_bits)

        return lo_bits

    @staticmethod
    def from_int(address, value):
        buf = struct.pack('<i', value)

        lo_word = w.Word(address, buf[1], buf[0])
        hi_word = w.Word(address, buf[3], buf[2])

        return DoubleWord(address, hi_word, lo_word)

    @staticmethod
    def from_uint(address, value):
        buf = struct.pack('<I', value)

        lo_word = w.Word(address, buf[1], buf[0])
        hi_word = w.Word(address, buf[3], buf[2])

        return DoubleWord(address, hi_word, lo_word)

    @staticmethod
    def from_float(address, value):
        buf = struct.pack('<f', value)

        lo_word = w.Word(address, buf[1], buf[0])
        hi_word = w.Word(address, buf[3], buf[2])

        return DoubleWord(address, hi_word, lo_word)

    @staticmethod
    def from_hex(address, value):
        buf = bytes.fromhex(value)

        lo_word = w.Word(address, buf[2], buf[3])
        hi_word = w.Word(address, buf[0], buf[1])

        return DoubleWord(address, hi_word, lo_word)
