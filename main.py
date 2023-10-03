from device import word as w
from device import double_word as dw
from device import relay as r
from plc import kv

DM0 = w.Word('DM0', 0x14, 0x12)
DM1 = w.Word('DM1', 0xC1, 0x49)

DM0L = dw.DoubleWord('DM0L', DM1, DM0)

print('int: ' + str(DM0L.to_int()[0]))
print('uint: ' + str(DM0L.to_uint()[0]))
print('float: ' + str(DM0L.to_float()[0]))

#kv = kv.KV("192.168.0.1", 8501)
#if kv.connect():

#    value = kv.read_device("DM0", ".U")
#    print(value)

#else:
#    print("接続できませんでした。")


