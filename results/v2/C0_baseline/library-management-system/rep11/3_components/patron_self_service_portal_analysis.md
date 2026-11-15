## Overview
The Library Management System provides a secure, self-service portal for EU library patrons to catalogue items, manage active loans, and settle fines. It is architected for high performance and strict EU data residency compliance.

## Key Elements
* Library Patrons (Students, researchers, public members)
* Patron Self-Service Portal (React / TypeScript SPA)
* Integration Gateway (Kong / Envoy API Gateway)
* Catalogue Search Component, Account & Loan Management Component, Fine Payment Component, Session State Coordinator, ErrorBoundary Wrapper
* External Systems: EU Identity Provider, EU Payment Gateway, EU Cloud Region Provider, Central Logging & Monitoring SIEM, Web Application Firewall (WAF)

## Relationships
* Patron Self-Service Portal -> Integration Gateway: API requests and payment tokens via HTTPS / REST over TLS 1.3
* Fine Payment Component -> EU Payment Gateway: Direct client-side SDK tokenization
* Session State Coordinator -> EU Identity Provider: Authentication via OIDC/OAuth2 with HttpOnly, SameSite=Strict cookies
* Patron Self-Service Portal -> Central Logging & Monitoring SIEM: Structured JSON logs and metrics via OpenTelemetry

## Technology Stack
* React / TypeScript SPA: Hosted via CDN with immutable deployments for rapid patron engagement
* HttpOnly, SameSite=Strict Cookies: Managed via Integration Gateway to mitigate XSS and securely handle session tokens
* EU Cloud Region Provider: Enforces EU-only data residency constraints for storage and hosting
* OpenTelemetry: Streamlines structured logging and metrics while stripping PII for SIEM observability

## Rationale
The component-based SPA architecture ensures a highly responsive search experience meeting the <800ms performance requirement. Client-side payment tokenization and strict cookie handling isolate PCI-DSS scope and protect against browser vulnerabilities.