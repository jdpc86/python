
# decrypt tp-link config.bin file
# coded by root@kev7n.com

from Crypto.Cipher import DES
from hashlib import md5
import sys
import zlib

# backup your config.bin from 192.168.x.1
# usage find PPPOE account
# ./run.py wan_ppp_usr
# keys: wan_ppp_usr,wan_ppp_pwd

key = b'\x47\x8D\xA5\x0B\xF9\xE3\xD2\xCF'

# key = b'\x47\x8D\xA5\x0B\xF9\xE3\xD2\xCF'
# key = bytes.fromhex('478DA50BF9E3D2CF')
crypto = DES.new(key, DES.MODE_ECB)

data = open('/Users/jd/tmpjd/config.bin', 'rb').read()
data_decrypted1 = crypto.decrypt(data[32:])
# data_decrypted = zlib.decompress(data_decrypted1, -zlib.MAX_WBITS)
data_decrypted = zlib.decompress(data_decrypted1)
assert data_decrypted[:16] == md5(data_decrypted[16:]).digest()
data_decrypted_finally = data_decrypted[16:]
data_decrypted_dict = {}
data_decrypted_array = data_decrypted_finally.split('\r\n')
for item in data_decrypted_array:
    if not item:
        continue
    item_array = item.split(' ', 1)
    item_key = item_array[0]
    item_value = item_array[1]
    data_decrypted_dict[item_key] = item_value

if len(sys.argv) > 1:
    print (data_decrypted_dict[sys.argv[1]])
open('config.bin.txt', 'wb').write(data_decrypted_finally)