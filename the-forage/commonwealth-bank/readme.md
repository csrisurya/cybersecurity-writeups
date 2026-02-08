# Commonwealth Bank Cybersecurity Generalist: Fraud Analytics & Enterprise Defense

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

### References
1. [Top 10 Common types of Cybersecurity Attacks (infocyte.com)](https://www.datto.com/blog/cybersecurity-101-intro-to-the-top-10-common-types-of-cybersecurity-attacks)
2. [11 Types of Phishing + Real-Life Examples (pandasecurity.com)](https://www.pandasecurity.com/en/mediacenter/tips/types-of-phishing/)
3. [8 Critical steps to take after a ransomware attack: Ransomware response guide for businesses - Emsisoft | Security Blog](https://blog.emsisoft.com/en/36921/8-critical-steps-to-take-after-a-ransomware-attack-ransomware-response-guide-for-businesses/)
4. [Battling Ransomware: How to Respond to a Ransomware Incident (forbes.com)](https://www.forbes.com/sites/forbestechcouncil/2018/12/27/battling-ransomware-how-to-respond-to-a-ransomware-incident/?sh=b464b4864dc6)
5. [Frequently Asked Questions - Ransomware | Information Security Office (berkeley.edu)](https://security.berkeley.edu/faq/ransomware/)
6. [What to do before and after a cybersecurity breach? | american.edu](https://www.american.edu/kogod/research/cybergov/upload/what-to-do.pdf)

















