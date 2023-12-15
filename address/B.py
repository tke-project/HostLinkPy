class B:
    header = 'B'

    def __init__(self, address):
        self.address = address

    @staticmethod
    def dec(addr):
        if B.header in addr:
            addr = addr.replace(B.header, '')
        addr = '0x' + addr

        return int(addr, 16)

    @staticmethod
    def hex(addr):

        if addr <= 0xff:
            return B.header + format(addr, '03x').upper()
        else:
            return B.header + format(addr, '04x').upper()

    @staticmethod
    def addr_list(addr, count):
        if addr[0] == B.header:
            addr = addr.replace(addr[0], '', 1)

        arr = []
        addr_val = B.dec(addr)
        for i in range(count):
            arr.append(B.hex(addr_val + i))

        return arr
