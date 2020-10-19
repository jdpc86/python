from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os
#
# full = RSA.generate(2048)
#
# print(full.n)


n = 0xD1E79FF135D14E342D76185C23024E6DEAD4D6EC2C317A526C811E83538EA4E5ED8E1B0EEE5CE26E3C1B6A5F1FE11FA804F28B7E8821CA90AFA5B2F300DF99FDA27C9D2131E031EA11463C47944C05005EF4C1CE932D7F4A87C7563581D9F27F0C305023FCE94997EC7D790696E784357ED803A610EBB71B12A8BE5936429BFD
e = 0x010001
d = 0x091550E28B45A770B296EDAEEF04E687F3258AB765A22E7CEA9D1BC8EB10BD2A0601A4421D267FD5ED5BF25A7372B67FFAD6D41A81A194B67623617F0A86A28F3727A6EC0E34ACCA4823F486CB3E08D9BBC2D043D62CC943EF898EF7C74CDCD8E9CEA87006019D6464B7B2BA37043D911611580A7A87D862E6BEBE4AD96146B1

# construct key using only n and d
try:
    # pycrypto >=2.5, only tested with _slowmath
    impl = RSA.RSAImplementation(use_fast_math=False)
    # partial = impl.construct((bytes_to_long(n), bytes_to_long(e), bytes_to_long(d)))
    partial = impl.construct((n, e, d))
    # partial.key.d = d
except TypeError:
    # pycrypto <=2.4.1
    partial = RSA.construct(n, bytes_to_long(b'0ox'), d)


pub = partial.publickey()
# pri = partial.privatekey()

private_key = partial.exportKey("PEM")
private_key_filename = "/Users/jd/tmpjd/id_rsa"
with open(private_key_filename, "w+b") as fd:
    fd.write(private_key)
    os.chmod(private_key_filename, 0o600)

# create message with padding
# http://en.wikipedia.org/wiki/RSA_%28algorithm%29#Padding_schemes
# cleartext = open('~/tmpjd/config.bin', 'rb').read()
#
# signature = partial.sign(cleartext, None)
#
# print ("validating message: ", pub.verify(cleartext, signature))
#
#
# message = pub.encrypt(cleartext, None)
#
# # bypassing the blinding step on decrypt
# enc_msg=map(bytes_to_long, message)
# dec_msg = map(partial.key._decrypt, enc_msg)

# print("decrypting: ")
# for m in dec_msg:
#     print(long_to_bytes(m))
    