import os

TREASURE = open("flag.txt", "rb").read()

KEY = os.urandom(8)

out = b""
for i, j in enumerate(TREASURE):
    PIRATE = (i * 7 + 13) & 0xff
    out += bytes([j ^ KEY[i % len(KEY)] ^ PIRATE])

print(out.hex())
