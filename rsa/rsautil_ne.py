from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64 
import urllib.parse
import os
#
# full = RSA.generate(2048)
#
# print(full.n)

def base64_url_decode(s):
    # padding_factor = (4 - len(inp) % 4) % 4
    # inp += "="*padding_factor 
    return base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))

nbase64urlint = "wZJS_u_9dXgoMi-4NVaqzygfKkqBZ2aT48TrJWRQPn-kqfh-RremrbgomZNFxCEk345PU3B2TXjNTVelgEKEzpsP8bkRMi8cXyNXj3tnArqfXIHc1dzcbGIn5zqrm4KqX-hLE0d5zGQGaVKjS04xeADQO7-8CzcnatoeqO36FX6-nroEWRF-zecPzf7td7os7DvkBO4S75k5rCPMaOkwbCvzGvKtXk0Q5EZfUqRoC1fJPmChh9iIP5eRYxCKJzDsOrkYSRWVksZ0ftiVJyBYnruESbjAX_6-KwggjTxGvSGm6PgIO5no1DMeNn21977TpeL3VCr1hOjvmUficzhCfw"
nbase64urlint_2 = "18O6PX88jh7TVGSVeoZqCS37Uh26lbF_OKsuIMq2zlBhEya8q66HHdQtjZAZE0oPDKPJHOqF79PkiNSgtdY35JdRY9SWeAYteYIGHc1iCqR-8tX5_BcKbA4VpACbvmQ8oXT0sLl1hqPgq-gBF-y2tCc_UzTmRRdGRIubZMGAj_qh93kGrEih7Hr2hrTmNNAXa_UIuIpxG4gm_6Dlq8WdvcKc3TSI7pRwM4XSa5QlI4gt29KzfQe6u-BA4_-VodPKUqkHP7Ya5S967615bc73-EdF-uwdsDTIVbLIxzVzLfED0tkOawQxA3AjNR-Yr7R2EWEsrpic_bq3Uvfb9ImilQ"

n = base64_url_decode(nbase64urlint_2)

e = base64_url_decode("AQAB")

rsak = RSA.construct((bytes_to_long(n),bytes_to_long(e)))

# rsak = RSA.construct(n,e,NULL)
# pub_key = rsak.publickey
# keySize=2048

pub_key=rsak.publickey().exportKey()

pub_key_filename = "/Users/jd/tmpjd/id_rsa2"
with open(pub_key_filename, "w+b") as fd:
    fd.write(pub_key)
    os.chmod(pub_key_filename, 0o600)

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
    