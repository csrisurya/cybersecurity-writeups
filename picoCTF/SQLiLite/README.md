# SQLiLite

https://play.picoctf.org/practice/challenge/304

## Vulnerability Breakdown and Technical Analysis
This login site is exploitable using an SQL injection attack. There are two ways of how this could be exploited.
The different ways are given to explore the various tabs in Burp. 

### Option 1: SQL Code Injection
The POST request is captured after arbitrary values for the username and password fields are entered and sent
to the Repeater tab. Then, the SQL injection is inserted <b>username=admin'--</b>. The single quote will close
the username field and the proceeding text is rendered under SQL code. Therefore, the two dashses is perceived as 
the commenting syntax. This means that the password is not rendered, allowing the attacker to bypass the password.

<img width="949" height="872" alt="image" src="https://github.com/user-attachments/assets/154bddb3-825b-4994-9b7c-cd95484f09e7" />

### Option 2: Automated Attack
The POST request is captured after arbitrary values for the username and password fields are entered and sent
to the Intruder tab. Choose 'Sniper Attack' then make the password field as the payload. The payloads are then 
copied from https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Intruder/Auth_Bypass.txt
and the payload type is a 'Simple list'. In the attack results, look in the repsonse body for each payload and
find the flag.

<img width="1545" height="805" alt="image" src="https://github.com/user-attachments/assets/fac313f5-4abf-4752-bcd9-8e71d0ef1113" />

## Security Impact
1. Unauthorized Data Access: Allows attackers to view and change data.

## Remediation Recommendations
1. Use parameterized queries, which entails using a template for the SQL query and then bind the user inputs are parameters (not as strings)
2. Utlize input validation by rejecting any special characters such as ' and --.
