# Red Team Practice: Denial of Service (DoS) via SSH Configuration Hardening
## Repository Overview
- Target OS: FreeBSD-based firewall appliance
- Target IP: 10.100.100.2
- Attack: Red Team persistence, host enumeration, and account lockdown
- Outcome: DoS of security application due to strict SSH AllowGroups policy enforcement

## Enumeration and Inital Access
### Network Scanning and Password Spraying
The engagement started by using Network Executive (nxc) to sweep the subnet for open SSH ports and test credentials across active infrastructure. Credentials were extracted by looking other resources.
```
nxc ssh 10.100.100.0/24 -u 'root' -p 'iamy0urf4ther'
```
Validated administrative shell access on two targets: 10.100.100.2 and 10.100.100.20.
<img width="1375" height="887" alt="Screenshot 2026-05-22 at 2 54 25 PM" src="https://github.com/user-attachments/assets/a4c295db-e2be-4e28-baba-2b6d52707615" />

## Target Architecture
To prepare for account lockdown, the local password file was audited to check for local active users and system groups.
```
cat /etc/passwd
# And checking the shadow equivalent on BSD:
sudo cat /etc/master.passwd
```

## Account Lockdown
### The Action
In an attempt to prevent Blue Team persistence and block other team accounts from accessing the machine, the SSH daemon configuration (/etc/ssh/sshd_config) was hardened globally.
The following policy was appended to restrict login capabilities exclusively to the raw root user:
```
AllowGroups root
```
The service configuration syntax was verified and the SSH daemon was restarted:
```
sudo sshd -t
sudo systemctl restart ssh   # Executed on management workstation / target
```
### Why it Crashed
While restricting access to AllowGroups root works seamlessly on vanilla Linux operating systems, it crashes or locks down network appliances like pfSense.
1. Group Mapping Failure: In pfSense, the web configurator and administrative sessions rely on specific group relationships (like admins or wheel). Whitelisting only the group root immediately cut off internal processing groups.
2. Interactive Menu Interruption: The admin user shell hooks directly into /etc/rc.initial to spawn the web panel and system monitoring tools. Blocking all groups except root broke the communication loops for the underlying configuration parsers, effectively inducing an application-layer denial of service (DoS).
3. Session Rejection: All subsequent non-root login requests were immediately dropped with an unhandled auth rejection loop:
```
ashla@10.100.100.202's password: 
Permission denied, please try again.
```
<img width="941" height="507" alt="Screenshot 2026-05-31 at 5 39 34 PM" src="https://github.com/user-attachments/assets/39b3a0e7-9b85-45b8-9a2b-c033cbdd8ab2" />

## Remediations
- Appliance Rule of Thumb: Never apply raw OS-hardening policies (AllowGroups, DenyUsers) directly to complex security appliances (pfSense, VyOS, Cisco) via the raw shell. Always utilize the built-in user management engine through the WebGUI/API.
- Operational Risk: A red team action meant for local containment can easily become an accidental destructive attack (Denial of Service) if systemic groups are modified without assessing the system's dependencies.















