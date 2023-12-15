import struct

# ワードを定義するクラス


class Word:

    address = ""
    hi_value = 0
    lo_value = 0

    # コンストラクタ
    # address -- "MR001"などのアドレス番号
    # hi_value -- 上位8バイト
    # lo_value -- 下位8バイト
    def __init__(self, address, hi_value, lo_value):
        self.address = address
        self.hi_value = hi_value
        self.lo_value = lo_value

    def __repr__(self):
        lo_str = format(self.lo_value, '02x').upper()
        hi_str = format(self.hi_value, '02x').upper()

        return '[' + hi_str + ', ' + lo_str + ']'

    def short(self):
        buf = bytes([self.lo_value, self.hi_value])

        return struct.unpack('<h', buf)[0]

    def s(self):
        return self.short()

    def ushort(self):
        buf = bytes([self.lo_value, self.hi_value])

        return struct.unpack('<H', buf)[0]

    def u(self):
        return self.ushort()

    def hex(self):
        lo_str = format(self.lo_value, '02x').upper()
        hi_str = format(self.hi_value, '02x').upper()

        return hi_str + lo_str

    def h(self):
        return self.hex()

    def bits(self):
        bits = []

        value = self.to_short()
        for i in range(16):
            bit = value & 1
            value = value >> 1

            bits.append(bit)

        return bits

    @staticmethod
    def from_short(address, value):
        buf = struct.pack('<h', value)

        return Word(address, buf[1], buf[0])

    @staticmethod
    def from_ushort(address, value):
        buf = struct.pack('<H', value)

        return Word(address, buf[1], buf[0])

    @staticmethod
    def from_hex(address, value):
        buf = bytes.fromhex(value)

        return Word(address, buf[0], buf[1])

    @staticmethod
    def from_string(address, value):
        words = []

        buf = value.encode(encoding='shift-jis')

        length = len(buf)

        for i in range(int(length/2)):
            lo_value = buf[2*i+1]
            hi_value = buf[2*i]

            words.append(Word(address, hi_value, lo_value))

        if length % 2 == 1:
            lo_value = 0
            hi_value = buf[length-1]

            words.append(Word('', hi_value, lo_value))

        return words

    @staticmethod
    def to_string(words):

        buf = []

        for word in words:
            buf.append(word.hi_value)
            buf.append(word.lo_value)

        return bytes(buf).decode('shift-jis')
