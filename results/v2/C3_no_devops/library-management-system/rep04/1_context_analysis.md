## Overview
The Library Management System is a cloud-native enterprise solution that enables public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search requirements.

## Key Elements
* **Personas:** Library Patron (Member), Librarian / Circulation Staff, Library Administrator.
* **Software System:** Library Management System (LMS).
* **External Systems:** Identity Provider (IdP), Payment Gateway, Notification Service, Inter-Library Loan (ILL) Network.

## Relationships
* **Personas $\rightarrow$ LMS:** HTTPS via TLS 1.3 (Web/Mobile Client UI).
* **LMS $\rightarrow$ IdP:** OIDC / OAuth2 for authentication.
* **LMS $\rightarrow$ Payment Gateway:** HTTPS/REST for fine processing.
* **LMS $\rightarrow$ Notification Service:** HTTPS/SMTP for patron alerts.
* **LMS $\rightarrow$ ILL Network:** HTTPS REST/SOAP with mutual TLS (mTLS) and OAuth2 client credentials.

## Technology Stack
* **Cloud Infrastructure:** EU-central regional deployment for data residency compliance.
* **Authentication:** Keycloak or Auth0 via OpenID Connect (OIDC) with mandatory MFA for staff.
* **Data Security:** AES-256 encryption at rest for databases and TLS 1.3 in transit.
* **Integrations:** Stripe/Adyen (Payments), Twilio/SendGrid (Notifications), and regional consortium APIs (ILL).

## Rationale
This architecture uses an authenticated cloud-native microservices approach with robust external integrations to meet performance goals and EU residency constraints. Strict security controls like mTLS, RBAC, and AES-256 ensure regulatory compliance and data protection.