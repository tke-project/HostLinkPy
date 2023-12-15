class W:
    header = 'W'

    def __init__(self, address):
        self.address = address

    @staticmethod
    def dec(addr):
        if W.header in addr:
            addr = addr.replace(W.header, '')
        addr = '0x' + addr

        return int(addr, 16)

    @staticmethod
    def hex(addr):

        if addr <= 0xff:
            return W.header + format(addr, '03x').upper()
        else:
            return W.header + format(addr, '04x').upper()

    @staticmethod
    def addr_list(addr, count):
        if addr[0] == W.header:
            addr = addr.replace(addr[0], '', 1)

        arr = []
        addr_val = W.dec(addr)
        for i in range(count):
            arr.append(W.hex(addr_val + i))

        return arr
