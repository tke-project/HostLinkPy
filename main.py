from device import word
from device import relay
from plc import kv


kv = kv.KV("192.168.0.1", 8501)
if kv.connect():

    value = kv.read_device("DM0", ".U")
    print(value)

else:
    print("接続できませんでした。")


