# Red Team Practice: Denial of Service (DoS) via SSH Configuration Hardening
## Repository Overview
- Target OS: FreeBSD-based firewall appliance
- Target IP: 10.100.100.2
- Attack: Red Team persistence, host enumeration, and account lockdown
- Outcome: DoS of security application due to strict SSH AllowGroups policy enforcement

## Enumeration and Inital Access
### Network Scanning and Password Spraying
The engagement started by using Network Executive (nxc) to sweep the subnet for open SSH ports and test default credentials across active infrastructure.
