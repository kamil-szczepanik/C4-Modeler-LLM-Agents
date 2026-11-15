## Overview
The Library Management System is a cloud-native platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency while delivering high-performance search and scalable administrative workflows.

## Key Elements
- Library Member (Patron)
- Librarian / Staff
- Library Administrator
- Library Management System (LMS)
- EU Cloud Infrastructure (AWS/Azure EU Region)
- EU Identity Provider (IdP)
- EU Compliance & Audit Logging Service
- EU Monitoring & APM Provider
- Third-Party Digital Content Providers (OverDrive/Libby)
- External Notification Service
- EU Secondary Region Backup Target
- Anycast CDN / DDoS Protection Service (EU-PoPs)

## Relationships
- Library Member / Librarian / Administrator -> `Uses (TLS 1.3, HTTPS)` -> Anycast CDN / DDoS Protection Service
- Anycast CDN -> `Routes Traffic (TLS 1.3)` -> Library Management System
- Library Management System -> `Persists Data (mTLS, Encrypted TLS/IPsec)` -> EU Cloud Infrastructure
- Library Management System -> `Authenticate Users (OIDC/OAuth2)` -> EU Identity Provider
- Library Management System -> `Export Audit Events (Syslog/HTTPS)` -> EU Compliance & Audit Logging Service
- Library Management System -> `Emit Metrics (OTLP/HTTPS)` -> EU Monitoring & APM Provider
- Library Management System -> `Lend/Sync Assets (OAuth2, HTTPS/REST)` -> Third-Party Digital Content Providers
- Library Management System -> `Dispatch Alerts (SMTP/HTTPS API)` -> External Notification Service
- EU Cloud Infrastructure -> `Replicates Backup (Encrypted TLS/IPsec)` -> EU Secondary Region Backup Target

## Technology Stack
- TLS 1.3 / mTLS: Secures all ingress and inter-system transit.
- OIDC/OAuth2 with MFA: Secures user and administrative authentication via EU IdP.
- OTLP/HTTPS: Transmits operational telemetry to meet the <800ms search latency requirement.
- OAuth2 Client Credentials & HMAC: Secures third-party digital content API integrations.

## Rationale
This architecture ensures strict compliance with EU-only data residency constraints by anchoring all hosting, backup, and monitoring within certified EU regions. The decoupled external integrations and robust edge security satisfy demanding performance, security, and digital circulation requirements.