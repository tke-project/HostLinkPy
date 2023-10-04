from device import word as w
from device import double_word as dw
from device import relay as r
from plc import kv

DM0 = w.Word.from_string("DM0", "こんにちは")

for w in DM0:
    print(w)



#kv = kv.KV("192.168.0.1", 8501)
#if kv.connect():

#    value = kv.read_device("DM0", ".U")
#    print(value)

#else:
#    print("接続できませんでした。")


