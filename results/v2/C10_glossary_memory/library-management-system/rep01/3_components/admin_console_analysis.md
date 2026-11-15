## Overview
The Admin Console is a secure web-based container within the Library Management System that enables Library Administrators to configure operations, manage users, and monitor metrics. It enforces strict EU-only data residency and role-based access control.

## Key Elements
- Admin UI Router & View Controller (React/TypeScript SPA)
- System Configuration Client (TypeScript Module)
- Admin Authentication & Session Manager (OpenID Connect SDK)
- Audit & Telemetry Dispatcher (TypeScript Module)
- Reporting & Analytics Dashboard Module (React/TypeScript Module)
- API Gateway / BFF (Nginx/Envoy)
- EU Identity Provider (IdP)
- EU Compliance & Audit Logging Service
- EU Monitoring & APM Provider
- Anycast CDN / DDoS Protection Service (EU-PoPs)

## Relationships
- Admin UI Router & View Controller -> System Configuration Client (In-memory TS calls)
- Admin UI Router & View Controller -> Reporting & Analytics Dashboard Module (In-memory TS calls)
- System Configuration Client -> API Gateway / BFF (HTTPS/REST, TLS 1.3)
- Reporting & Analytics Dashboard Module -> API Gateway / BFF (HTTPS/REST, TLS 1.3)
- Admin Authentication & Session Manager -> EU Identity Provider (IdP) (OIDC/OAuth2, TLS 1.3)
- Audit & Telemetry Dispatcher -> EU Compliance & Audit Logging Service (Syslog/HTTPS, TLS 1.3)
- Audit & Telemetry Dispatcher -> EU Monitoring & APM Provider (OTLP/HTTPS, TLS 1.3)

## Technology Stack
- React/TypeScript SPA: Provides a responsive, maintainable single-page application framework for administrative interfaces.
- OpenID Connect SDK: Implements secure OIDC/OAuth2 authentication and multi-factor authentication flows.
- HTTPS/REST via TLS 1.3: Ensures encrypted, secure data transmission across all component interfaces.
- Syslog/HTTPS and OTLP/HTTPS: Standardizes compliance audit export and telemetry transmission to EU providers.

## Rationale
This component architecture enforces strict EU data residency and robust role-based access control required for public and academic institutions. Modular client-side components ensure high availability, auditability, and secure administrative oversight.