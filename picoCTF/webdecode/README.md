# WebDecode
https://play.picoctf.org/practice/challenge/427

## Vulnerability Breakdown and Technical Analysis
Burp Suite was utlized to look at the responses of the GET request of each page in the test website. The html code contains a long string that seems very off-putting compared to the other code. When the long string is highlighted, Burp decodes it from Base64 format and the CTF flag is revealed.  

<img width="1915" height="778" alt="image" src="https://github.com/user-attachments/assets/286d7fed-ede8-4334-b142-8f19d5465b9b" />


## Security Impact
1. Information Disclosure: Any sensitive info should not be publicly displayed.
2. False Sense of Security: Base64 is not secure because it is easily decoded. 

## Remediation Recommendations
1. Never store sensitive data in source code.
2. Any data that should be encrypted should be used by encryption standards such as AES, RSA, and ECC. 
