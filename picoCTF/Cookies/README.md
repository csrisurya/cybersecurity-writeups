# Cookies

https://play.picoctf.org/practice/challenge/173?category=1&page=1&search=cookie

## Vulnerability Breakdown and Technical Analysis
The GET request for the search funtionality and sent to the Intruder tab in Burp Suite. The cookie parameter
is what generates different responses, so this should be exploited by brute forcing mutiple values for it.
For the Sniper attack, the cookie value is selected as the payload with the 'Numbers' payload type. Initially, the number range
between 0-15 did not reveal any flag. In the second attempt, the number range was broadened to 0-30. As indicated in the
HTTP response, the cookie value of 18 revealed the flag. 

<img width="1545" height="805" alt="image" src="https://github.com/user-attachments/assets/09e991ee-3a61-4bae-a881-8c3313252eb0" />

## Security Impact
1. Broken Access Control: There is a client-side value that determines what content is displayed. In this instance,
2. the cookie is an Insecure Object Reference Reference (IDOR) and allows attackers to access restricted information.

## Remediation Recommendation
1. Use random strings for the UUIDs for cookie values, instead of predictable integers.
2. Implement server side session management, where the client does not have control over the ID of data being retrieved.
3. Use a digital signature to authenticate the cookie and validate the integrity of the request.
