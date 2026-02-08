# Commonwealth Bank: Fraud Analytics & Enterprise Defense
**Summary:** This simulation provided a comprehensive look into the daily responsibilities of a Cybersecurity Generalist at Commonwealth Bank. By leveraging Splunk Enterprise to visualize and detect financial fraud patterns, I developed a data-driven approach to protecting customer assets. My technical proficiency was further tested through a multi-stage Incident Response scenario involving phishing and ransomware, where I managed the full lifecycle from containment to recovery. Additionally, I conducted a deep-dive Penetration Test of web applications and designed ACSC-aligned security awareness content, demonstrating a well-rounded ability to both identify technical vulnerabilities and strengthen an organization's human firewall.

## Fraud Detection & Data Visualization (Splunk)
**Objective:** Use Splunk to identify fraudulent transaction patterns within a simulated dataset of customer payments.  

### Dataset Metadata

| Feature Column | Data Type | Description | Key Values / Legend |
| :--- | :--- | :--- | :--- |
| **Step** | Integer | Month from the start of the simulation. | 0: May, 1: June, 2: July, 3: August |
| **Customer** | String | Unique Identifier for the customer. | Customer ID |
| **Age** | Categorical | Categorized age groups. | 0: <=18, 1: 19-25, 2: 26-35, 3: 36-45, 4: 46-55, 5: 56-65 |
| **Gender** | Character | Gender of the customer. | F: Female, M: Male |
| **PostcodeOrigin**| String | Postcode of origin/source. | Source Postcode |
| **Merchant** | String | The merchant's ID. | Merchant ID |
| **Category** | String | Category of the purchase. | e.g., Transportation, Food, Health |
| **Amount** | Float | Amount of the purchase. | Transaction amount |
| **Fraud** | Boolean | Target variable showing fraudulent status. | 0: Non-fraudulent, 1: Fraudulent |

### Key Contributions
* **Splunk Dashboarding:** Built a comprehensive dashboard to track metrics like "Count by Category" and "Fraud Detected by Age/Gender".
* **Query Development:** Leveraged Splunk Search Processing Language (SPL) to filter data.
    * *Example Query:* sourcetype="fraud_detection.csv" | top category
    * *Example Query:* sourcetype="fraud_detection.csv" fraud="1" | stats count values(fraud) by category.
* **Pattern Recognition:** Identified which demographics and merchants were most susceptible to fraudulent activity

<DASHBAORD>

### References
Refer to <instrcution> for 

## Incident Response - Phishing & Ransomware
**Objective:** Analyze a multi-stage cyberattack targeting the Risk Department.

### Scenario
* 10:30 AM - One colleague received an email from HR telling all employees to update their timesheets in the company’s support portal so the timesheets can be approved on time by their line managers against the next pay day. The colleague clicked the link in the email that opened what looked like the portal. However, following the employee's input of the user credentials, an unfamiliar error page appeared like the one below.
IMAGE  
* 2:00 PM - Eight more reports of emails similar to the one reported earlier are received by the IT Service Desk. Further investigation shows 62 colleagues across the Risk Department received the same email over the course of two days. The emails directed the users to a fake website to steal their usernames and passwords and download a harmful program.
* 3:50 PM - IT Service Desk receives calls and emails from more colleagues that the file-shares are not opening and they receive an error when trying to open a Word document they have always been able to open.

### Attack Overview
* **Phishing:** The initial email from "HR" was a phishing attempt. It used social engineering (urgency regarding payroll) to trick users into visiting a spoofed portal to steal their credentials.
* **Malware Delivery:** The fake website also prompted a download of a harmful program, which served as the initial infection vector.
* **Ransomware:** The report at 3:50 p.m. regarding file-shares not opening and Word documents failing to open is a classic indicator of ransomware. The malware likely encrypted the files, making them inaccessible to the users.

### Next Steps
* **Analyze & Scope:** Confirm the ransomware strain, identify "Patient Zero" from the 62 email recipients, and map all impacted servers and workstations.
* **Contain & Isolate:** Disconnect infected systems from the network, block the malicious domain at the firewall, and disable compromised user credentials immediately.
* **Resolve & Recover:** Wipe infected machines for a clean OS reinstall, restore data from secure offline backups, and validate that no "sleeper" malware remains.
* **Harden & Educate:** Conduct a "Lessons Learned" meeting, update email filters, and launch mandatory phishing training (e.g., Least Privilege).

## Security Awareness & Education 
**Objective:** Design an infographic based on ACSC (Australian Cyber Security Centre) advice to educate peers on password security.

**Core Principles Addressed:**
* **Strong Passwords:** Implementing ACSC guidelines for complex, unique passwords.
* **Management:** Utilizing tools and habits to manage credentials securely.
* **Prevention:** Using visual storytelling to reduce the likelihood of successful social engineering attacks.

## Penetration Testing Report (HackThisSite)
**Objective:** Conduct a "Black-box" security audit of a web application and document vulnerabilities.
* **Target:** https://www.hackthissite.org/missions/basic/
* **Levels:** 1 through 11

| Level | Vulnerability Type | Description & Findings | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **1** | **Insecure Source Code** | Credentials (password) were stored directly within HTML comments in the client-side code. | Never store credentials or sensitive logic in client-side code (HTML, CSS, JS) where they are visible to users. |
| **2** | **Broken Authentication** | The application failed to validate the presence of a password file, allowing access when no password was provided. | Implement robust server-side authentication checks and ensure configuration files are properly secured. |
| **3** | **Information Disclosure** | Sensitive URL paths and file locations (e.g., password.php) were exposed in the HTML source code. | Disable directory listing and ensure sensitive file paths are not exposed in client-side code. |
| **4 & 5** | **Insecure Direct Object Reference (IDOR)** | Attackers could intercept and modify the recipient's email address by manipulating hidden fields in the DOM. | Perform all sensitive business logic on the server side; do not rely on hidden client-side fields for security. |
| **6** | **Weak Encryption** | The application used a simple, reversible character-shift cipher based on string position. | Use industry-standard, non-reversible cryptographic hashing algorithms. |
| **7** | **Command Injection** | The application allowed execution of shell commands (e.g., `ls`) through unsanitized user input fields. | Implement strict input sanitization and use parameterized execution to prevent OS command injection. |
| **8 & 9** | **SSI Injection / Path Traversal** | Server-Side Includes (SSI) were exploited to execute commands and navigate the file system directory. | Sanitize all user inputs and disable SSI execution where it is not strictly required for business functionality. |
| **10** | **Cookie Manipulation** | Authorization was granted by manually modifying cookie parameters (e.g., `level10_authorized`) via an intercepting proxy. | Use secure, server-managed session tokens and never rely on client-side cookies for authorization status. |
| **11** | **Directory Listing / Config Disclosure** | Insecure server configurations allowed for directory listing and unauthorized access to the `.htaccess` file. | Disable directory browsing on the web server and restrict access to configuration files like `.htaccess`. |










