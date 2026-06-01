# UW Bothell - CyberAI Conference 2026 - AccessHub Security Review

A hands-on AI-assisted threat modeling exercise completed at the **CyberAI Conference hosted at the University of Washington Bothell**. Working as part of a 4-person team (Team Grayhats), we conducted a full security review of a fictional internal access management tool called **AccessHub**, using STRIDE methodology and AI.


## 🏗️ What We Reviewed

AccessHub is a fictional internal web application that allows employees to request access to company resources, and lets managers approve or deny those requests. It is a standard three-tier AWS architecture:

- **Frontend**: React SPA served via CloudFront + S3
- **Backend**: Node.js/Express API on ECS Fargate (2 containers), behind an ALB
- **Database**: RDS PostgreSQL in a private subnet
- **CI/CD**: GitHub Actions → ECR → ECS

The design doc was intentionally flawed — our job was to find the security issues before any code was written.

## 🗺️ Architecture Diagram

![AccessHub Architecture Diagram](./Threat_Model_drawio.png)

**Trust Boundaries Identified:**
- Internet / AWS boundary
- Users & External Systems ↔ Frontend (AWS)
- Frontend ↔ Backend / Public Subnet
- Backend / Public Subnet ↔ Database / Private Subnet

## Top 10 Threats Identified

We used the **STRIDE** framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) to identify and prioritize threats.

| # | Threat | STRIDE | Likelihood | Impact | Priority |
|---|--------|--------|------------|--------|----------|
| 1 | Forgeable JWTs via hardcoded signing key (`"accesshub-secret"`) | Spoofing / EoP | High | High | 🔴 P1 |
| 2 | User-management endpoints may lack backend role checks | EoP / Tampering | High | High | 🔴 P1 |
| 3 | SQL injection via string-concatenated queries | Tampering / Info Disclosure | High | High | 🔴 P1 |
| 4 | Analysts can bypass frontend filtering on `GET /requests` | Info Disclosure / EoP | High | High | 🔴 P1 |
| 5 | Weak password storage using MD5 | Spoofing | High | High | 🔴 P1 |
| 6 | No rate limiting or account lockout → brute-force attacks | Spoofing / DoS | High | High | 🔴 P1 |
| 7 | JWT tokens never expire — stolen tokens remain valid indefinitely | Spoofing / EoP | Medium | High | 🟠 P2 |
| 8 | Full request bodies logged to CloudWatch (passwords, tokens exposed) | Info Disclosure | High | Medium | 🟠 P2 |
| 9 | Plaintext secrets in ECS environment variables | Info Disclosure / EoP | Medium | High | 🟠 P2 |
| 10 | Debug ports 22/9229 exposed to `0.0.0.0/0` | EoP / DoS | Medium | High | 🟠 P2 |

## Top 3 Threats

### 1. JWT Forgery via Hardcoded Signing Key
The JWT signing key is the literal string `"accesshub-secret"`, shared across dev/staging/prod and stored in plaintext ECS environment variables. Any attacker who learns this key — through a leaked repo, log, or container access — can mint a `role: "manager"` token and call any privileged endpoint without valid credentials. Every access control in the system trusts the JWT, so this single weakness invalidates all of them.

**Mitigation:** Generate a strong random key per environment, store in AWS Secrets Manager, add token expiry, and re-verify roles from the database on sensitive actions.

---

### 2. Privilege Escalation via Unprotected User-Management Endpoints
The design states `POST /users` and `PATCH /users/:id` are "intended for managers only" but never confirms backend role enforcement is actually implemented. A low-privileged analyst could call these endpoints directly to create a manager account or escalate their own role — gaining full approval and user-management rights with a single API call.

**Mitigation:** Enforce manager-only authorization in the backend on every user-management endpoint. Never rely on frontend button hiding. Add authorization tests for each endpoint.

---

### 3. SQL Injection via String-Concatenated Queries
The design explicitly states that some older endpoints build SQL queries by concatenating user-supplied values into SQL strings. This sits directly in front of all four database tables (users, requests, approvals, audit\_log). A single malicious input could dump credentials, tamper with approval records, or wipe the audit trail — with no WAF or rate limiting anywhere in the stack to slow an attacker down.

**Mitigation:** Replace all string-concatenated SQL with parameterized queries immediately. Add input validation and least-privilege database permissions.




