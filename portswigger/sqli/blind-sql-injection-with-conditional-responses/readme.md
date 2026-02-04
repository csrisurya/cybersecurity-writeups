# Blind SQL Injection with Conditional Responses
This laboratory demonstrates how to exploit a Blind SQL Injection vulnerability to exfiltrate sensitive data—specifically the administrative password—from a database by observing conditional changes in the application's HTTP responses.

## Phase 1: Vulnerability Identification
The application uses a tracking cookie (TrackingId) that is processed by a backend SQL query. If the query returns results, the page displays a "Welcome back!" message.
1. <b>Intercept the Request:</b> Use Burp Suite Proxy to intercept a standard GET request and send it to the Repeater tab for manual manipulation.
2. <b>Confirm Injection Point:</b>
    * True Condition: Appending <i>' and 1=1--</i> to the TrackingId cookie. Since <i>1=1</i> is true, the "Welcome back!" message remains visible.
    * False Condition: Appending <i>' and 1=0--</i>. Since <i>1=0</i> is false, the "Welcome back!" message disappears from the response.
  
## Phase 2: Database Enumeration
Once the vulnerability is confirmed, we can use conditional logic to query the internal structure of the database.
* <b>Confirm Table Existence:</b> Verify the users table exists by injecting:
  <i>' and (SELECT 'x' FROM users LIMIT 1)='x'--</i>

* <b>Confirm Username:</b> Check for the specific user administrator:
  <i>' and (SELECT username FROM users WHERE username='administrator')='administrator'--</i>

## Phase 3: Data Exfiltration (Password Discovery)
1. <b>Determine Password Length</b>
Before brute-forcing the password, we must determine its length using Burp Intruder.
    * <b>Payload:</b> <i>' and (SELECT username FROM users WHERE username='administrator' AND LENGTH(password)>§1§)--</i>
    * <b>Process:</b> Use a "Numbers" payload type (1 to 30).
    * <b>Result:</b> The last payload that triggers the "Welcome back!" message indicates the length. In this lab, the password length was confirmed to be 20 characters.
2. <b>Automated Brute-Force Script</b>
Because Burp Suite Community Edition is rate-limited, a Python script is more efficient for extracting the 20-character string. The script iterates through each character position ($i$) and tests it against the ASCII values of printable characters ($j$). [See the script](blind_sqli_with_conditional_responses.py)
## Conclusion
By analyzing the presence or absence of the "Welcome back!" string, we successfully reconstructed the administrator's password: <i>inp2c2@geget88q1krnv</i>.

## Remediation
To prevent this, the application should use parameterized queries (prepared statements), which ensure that user input is treated as data (e.g., string) rather than executable SQL code.






