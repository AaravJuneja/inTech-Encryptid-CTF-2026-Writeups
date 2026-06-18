# Sanity Check

## Description

> Sometimes doing exactly the opposite of what you're told gets you great success in life. Oh, and have you ever gone to 64th base with someone before?

[chall.bin](chall.bin)

## Solution

The challenge hint suggests doing the opposite of what is implied:
- "Opposite of what you're told" = instead of decoding encode the provided text.
- "64th base" = Base64.

Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')) drag and drop the file to get:

encryptid/leftcurlybrace/w3lc0m3/underscore/70/underscore/3ncryp71d/underscore/2026/underscore/br1ng/underscore/br3ad/underscore/4l0ng/underscore/7h3/underscore/w4y/underscore/pl34se/rightcurlybrace//

Replacing `leftcurlybrace` with `{`, `underscore` with `_`, `rightcurlybrace` with `}` and removing `/` separators yields the flag:

`encryptid{w3lc0m3_70_3ncryp71d_2026_br1ng_br3ad_4l0ng_7h3_w4y_pl34se}`