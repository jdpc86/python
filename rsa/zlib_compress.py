import zlib

inputFile = '/Users/jd/tmpjd/archer/tmp.json'
with open(inputFile, 'rb') as f:
    # src = f.read().decode('utf8')
    src = f.read()
outputFile = '/Users/jd/tmpjd/archer/tmp.cry'
with open(outputFile, "w+b") as fd:
    fd.write(zlib.compress(src))
    # os.chmod(private_key_filename, 0o600)