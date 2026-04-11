# IntroToBurp
https://play.picoctf.org/practice/challenge/419

## Vulnerability Breakdown and Technical Analysis
After the filling out the login page and OTP token, the POST request is captured inside Burp and passed onto the Repeater tab.
Through the Repeater tab, the HTTP response could be modified by removing the 'otp' parameter all together. 
This allows us to bypass the OTP and the flag is revealed.

<img width="949" height="778" alt="image" src="https://github.com/user-attachments/assets/f7b1dce5-1a97-48d9-9813-465cd0f24ea6" />

<img width="949" height="795" alt="image" src="https://github.com/user-attachments/assets/a0b6a669-f4ed-4881-84f6-a1f5848d6677" />


## Security Impact
1. Authentication Bypass: The purpose of the multi-factor authentication is rendered useless. Therefore, an attacker only needs the username and password to gain access.
2. Logic Flaw: If the server expects a value (OTP token) but does not receive it, it defaults to authorized rather than denied.

## Remediation Recommendations
1. Enforce strict schema with what parameters that should be expected. If there are any missing values, it should result in an error.
 
