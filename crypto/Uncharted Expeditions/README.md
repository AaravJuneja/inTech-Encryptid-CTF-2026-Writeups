# Uncharted Expeditions

## Description

> We finally found the island marked X on the last Log Pose. The treasure's there, I can feel it. We just needed to crack the stone inscription but we got jumped by pirates before we could decipher it. I'm regrouping at coordinates 64 64 64. Meet me there. We'll split into pairs of 8, decode the message and head back before they find it first.

[chall.py](chall.py) [output.txt](output.txt)

## Solution

`output.txt` contains binary digits separated by spaces. Parse them into 8 bit bytes, decode to ASCII to get a Base64 string and then Base64 decode for the ciphertext:
```python
raw = open("output.txt").read().strip().replace(" ", "")
b64 = bytes(int(raw[i:i+8], 2) for i in range(0, len(raw), 8)).decode("ascii")
enc = base64.b64decode(b64)
```

`BxERID8rKnZOXFJPa1xuMnewgZCPu/m/vaWeytbK6fbxwKYtBRNPUy40BTpCF18oRT5xakmY3sLJx6TpgbjnicbgxaLz9/qAHlROCSYcKyQNW0oRaXw6NmlIiM6dmKm2rICm2pXkjpPu2P6+FxA5BxoQNXE6R3EITwR5aUEiYtS9i8O/9YSqr/XVidy+7/Ojo18MUwwuEWwoLlpODmxbPnEsfpS5z5DblfO2uZ780p+G4end71sbcBxHOAUsYDcDE1FVTTJ3cgCej8uZka717o3Iksbp6eL86eQ1A04GKWpyLWFtUlMNEVU2RWbeldXohv+dteLfzYflzrrvwfWiFg4gRiYZN20rWEkLRGlcZSVrn5bSkbn6/7Ku9dLb1umv5/qzDw==`

Decode the Base64 as hinted in description. Since we already know the flag format `encryptid{...}`. We know the first 10 bytes of the plaintext (`encryptid{`). The encryption is:
```python
ciphertext[i] = plaintext[i] ^ key[i % 8] ^ ((i * 7 + 13) & 0xff)
```

We can recover the key by rearranging:
```python
key[i % 8] = ciphertext[i] ^ plaintext[i] ^ ((i * 7 + 13) & 0xff)
```

The source code reveals that the key repeats every 8 bytes, the first 8 characters of the known prefix are enough to recover the full key:
```python
key = bytearray(8)
for i, c in enumerate(b"encryptid{"):
    p = (i * 7 + 13) & 0xff
    key[i % 8] = enc[i] ^ c ^ p
```

This gives: `okipoki!`

With the key recovered, we decrypt the entire ciphertext:

```python
flag = bytearray()
for i, c in enumerate(enc):
    p = (i * 7 + 13) & 0xff
    flag.append(c ^ key[i % 8] ^ p)

print("Flag:", flag.decode())
```

`encryptid{hee_hee_cryp70gr4phy_1s_4_ch1lds_pl4y_w1sh_s0m30n3_k1nd_w0uld_t34ch_m3_th3_w4ys_b4ck_1n_th3_0ld_d4ys_0h_w3ll_gu3ss_1ts_t1m3_t0_r3v0lut10n1ze_crypt0_mys3lf_4nd_4ls0_th4nk_y0u_f0r_r3ad1ng_4ll_th1s_m3y_g0d_bl3ss_y0u_m0r3_th3n_1_l0v3_t0_w4tch_y0u_f41l_4t_l34rn1ng_crypt0gr4phy_hee_hee!}`