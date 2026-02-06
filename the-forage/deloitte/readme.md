# Data Breach Investigation of Deloitte Client: Daikibo Industrials

## Summary
A major news publication has revealed sensitive private information about Daikibo Industrials. 
A production problem has caused its assembly lines to stop, threatening the smooth operation 
of supply chains relying on Daikibo’s products. The client suspects the security of their 
new status board may have been breached. The investigation concluded that an external attack 
was not possible as all logged activity originated from internal static IP addresses. However, 
a specific user ID was identified performing highly suspicious, automated API requests at exact 
intervals, continuing even after their authorization had expired.

## Network Perimeter Analysis
The first step was to determine if the Daikibo telemetry dashboard was exposed to the public internet.  
* <b>Findings:</b> All logged requests originated from the 192.168.0.x subnet.
* <b>Conclusion:</b> Because these are part of an internal network, the alleged breach could not have happened 
from an attacker on the internet directly. Access required physical presence on-site or a connection to 
the company’s VPN.

## Suspicious Activity Investigation
A comparison of user behavior was conducted to distinguish legitimate users from potential automated threats.

Standard users followed a logical browsing flow:
1. <b>Authentication:</b> Initial 401 Unauthorized redirecting to a successful login.
2. <b>Resource Loading:</b> Loading CSS and JS files for the dashboard.
3. <b>Manual Navigation:</b> Sporadic API requests to specific factories and machines at irregular intervals (e.g., 09:29:57, then 09:30:57)

User ID mdB7yD2dp1BFZPontHBQ1Z (connecting via IP 192.168.0.101) exhibited a pattern indicative of a bot or script.
The requests occurred at the exact second (:48) every hour.
(INSERT IMAGE)

## Persistent Unauthorized Access
Further evidence of automation was found when the user's session expired.
* <b>Observation:</b> Starting at 2021-06-26T00:00:48.000Z, the script continued attempting to query factory statuses.
* <b>Outcome:</b> The server correctly issued 401 (UNAUTHORIZED) responses.
* <b>Analysis:</b> A human user receiving an unauthorized error would stop or re-authenticate. The script continued to fire every hour until 16:00:48, receiving 16 consecutive failures before the user manually logged back in at 16:04:01.
(IMAGE)

## Remediation Recommendations
1. <b>Rate Limiting:</b> Limit the frequency of API requests per User ID/IP to prevent automated data scraping.
2. <b>Session Management:</b> Review session timeout durations and implement alerts for repeated 401 errors from the same internal IP.
3. <b>Intranet Monitoring:</b> Deploy an Intrusion Detection System (IDS) to flag unusual dashbaord usage patterns.
