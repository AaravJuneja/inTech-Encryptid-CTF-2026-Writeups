# Bounty Hunter

## Description

> The bounty hunter has declared that NOTHING is capable of defeating him and his self-proclaimed puzzles. Are you?

`https://intech-encryptid-web-1.onrender.com/`

## Solution

Looking at the source code of the homepage (`/`) reveals the following HTML comment:
```html
<!-- perhaps the robots could appear from the sky and help you out? -->
```

This hints at checking `robots.txt` which contains:
```
User-Agent: *
Disallow: /do-you-believe-in-reincarnation
```

Navigating to `/do-you-believe-in-reincarnation` presents a password prompt and sets the following cookie:
```
Set-Cookie:
encrypted_password=aURvQmVsaWV2ZUluUmVpbmNhcm5hdDFvbiMzOT8hPw%3D%3D
```

URL decoding (`%3D` -> `=`) gives:
```
aURvQmVsaWV2ZUluUmVpbmNhcm5hdDFvbiMzOT8hPw==
```

The trailing `==` indicates Base64 encoding. Decoding it yields:
```
iDoBelieveInReincarnat1on#39?!?
```

Submitting this password grants access and reveals the flag `encryptid{h34rt1ly_r3inc4rn473d_f7w}`