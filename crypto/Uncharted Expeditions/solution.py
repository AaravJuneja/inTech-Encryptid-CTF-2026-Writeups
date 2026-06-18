import base64

raw = open("crypto/Uncharted Expeditions/output.txt").read().strip().replace(" ", "")

b64 = bytes(int(raw[i:i+8], 2) for i in range(0, len(raw), 8)).decode("ascii")

enc = base64.b64decode(b64)

key = bytearray(8)
for i, c in enumerate(b"encryptid{"):
    p = (i * 7 + 13) & 0xff
    key[i % 8] = enc[i] ^ c ^ p

print("Recovered Key:", bytes(key))

flag = bytearray()
for i, c in enumerate(enc):
    p = (i * 7 + 13) & 0xff
    flag.append(c ^ key[i % 8] ^ p)

print("Flag:", flag.decode())
