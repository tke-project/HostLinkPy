class LR:
    header = 'LR'

    def __init__(self, address):
        self.address = address

    @staticmethod
    def dec(addr):
        if LR.header in addr:
            addr = addr.replace(LR.header, '')

        a = int(int(addr) / 100)
        b = int(addr) % 100

        return 16 * a + b

    @staticmethod
    def hex(addr):

        a = int(addr / 16)
        b = addr % 16

        if a == 0:
            return LR.header + '0' + format(b, '02')
        else:
            return LR.header + str(a) + format(b, '02')

    @staticmethod
    def addr_list(addr, count):
        if LR.header in addr:
            addr = addr.replace(LR.header, '')

        arr = []
        addr_val = LR.dec(addr)
        for i in range(count):
            arr.append(LR.hex(addr_val + i))

        return arr
