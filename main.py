from device import *
from address.MR import *

#アドレスを連番で取得
mrs = MR.addr_list('MR10304', 200)
for mr in mrs:
    print(mr)

# kv = kv.KV("192.168.0.1", 8501)
# if kv.connect():

#    value = kv.read_device("DM0", ".U")
#    print(value)

# else:
#    print("接続できませんでした。")
