class MR:
    header = 'MR'

    def __init__(self, address):
        self.address = address

    @staticmethod
    def dec(addr):
        if MR.header in addr:
            addr = addr.replace(MR.header, '')

        a = int(int(addr) / 100)
        b = int(addr) % 100

        return 16 * a + b

    @staticmethod
    def hex(addr):

        a = int(addr / 16)
        b = addr % 16

        if a == 0:
            return MR.header + '0' + format(b, '02')
        else:
            return MR.header + str(a) + format(b, '02')

    @staticmethod
    def addr_list(addr, count):
        if MR.header in addr:
            addr = addr.replace(MR.header, '')

        arr = []
        addr_val = MR.dec(addr)
        for i in range(count):
            arr.append(MR.hex(addr_val + i))

        return arr
