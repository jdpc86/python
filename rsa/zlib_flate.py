import zlib

inputFile = '/Users/jd/tmpjd/archer/cfg_bin/tmp.zlib'
with open(inputFile, 'rb') as f:
    # src = f.read().decode('utf8')
    src = f.read()
outputFile = '/Users/jd/tmpjd/archer/cfg_bin/tmp.json'
with open(outputFile, "w+b") as fd:
    fd.write(zlib.decompress(src, 32))
    # os.chmod(private_key_filename, 0o600)