import zlib

inputFile = '/Users/jd/01_github/archerc9/config/tmp.zlib'
with open(inputFile, 'rb') as f:
    # src = f.read().decode('utf8')
    src = f.read()
outputFile = '/Users/jd/tmpjd/archer/tmp_orig.json'
with open(outputFile, "w+b") as fd:
    fd.write(zlib.decompress(src, 32))
    # os.chmod(private_key_filename, 0o600)