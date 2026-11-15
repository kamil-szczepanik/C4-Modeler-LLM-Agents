## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability, strict regulatory compliance, and high-performance clinical workflows.

## Key Elements
- Internal Staff Application (React / TypeScript, Nginx)
- Staff Auth & Session Manager
- Admission & Reception Module
- EMR Clinical Workspace Module
- Billing & Claims Module
- Compliance & Audit Dashboard
- API Gateway (Kong / Envoy)
- External Identity Provider (IdP)

## Relationships
- Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance/Security Officers, Hospital/Clinic Management -> Internal Staff Application [HTTPS (Web)]
- Staff Auth & Session Manager -> External Identity Provider (IdP) [HTTPS (OIDC / SAML 2.0 with MFA)]
- Internal Staff Application -> API Gateway [HTTPS (mTLS/OIDC, REST/GraphQL)]

## Technology Stack
- React & TypeScript: Frontend framework for dynamic, role-based single-page application interfaces.
- Nginx: High-performance web server enforcing TLS 1.3, HSTS, CSP nonces, and SRI.
- OpenID Connect (OIDC) / SAML 2.0: Secure authentication standard integrating multi-factor authentication.
- HttpOnly, Secure, SameSite=Strict Cookies: Secure storage mechanism isolating tokens from XSS vulnerabilities.

## Rationale
This architecture fits the requirements by utilizing role-based code splitting and lazy loading to achieve sub-second EMR screen loads (P95). It enforces rigorous security and compliance controls (HIPAA/GDPR) via strict token handling and secure transport protocols.