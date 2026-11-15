## Overview
The Library Management System is a comprehensive platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures strict EU data residency and high-performance search capabilities.

## Key Elements
* Library Patrons (Members)
* Librarians / Circulation Staff
* Library Administrators
* Library Management System (LMS)
* EU Identity Provider (IdP) (Keycloak / Auth0)
* EU Payment Gateway (Stripe EU / regional APIs)
* EU-compliant Notification Service
* EU Cloud Region Provider (AWS Frankfurt/Ireland / OVHcloud)
* Central Logging & Monitoring SIEM
* Web Application Firewall (WAF)

## Relationships
* Patrons, Staff, Admins -> Library Management System: HTTPS (TLS 1.3) via WAF
* Library Management System -> EU IdP: OIDC/OAuth2 over HTTPS
* Library Management System -> EU Payment Gateway: REST API over HTTPS with mTLS
* Library Management System -> EU Notification Service: Asynchronous REST API over HTTPS with mTLS
* Library Management System -> EU Cloud Provider & SIEM: Non-blocking audit logging and infrastructure telemetry

## Technology Stack
* EU Cloud Region Provider: AWS Frankfurt/Ireland or OVHcloud for data residency compliance
* EU Identity Provider: Keycloak or EU-hosted Auth0 for OAuth2/OIDC authentication
* Transport Security: TLS 1.3 and mTLS for all network communications
* Storage Encryption: AES-256 for data-at-rest within the EU boundary
* Architecture: Asynchronous event-driven patterns for non-blocking notifications and logging

## Rationale
This architecture guarantees strict regulatory compliance through localized EU infrastructure and mandatory data encryption standards. Furthermore, asynchronous processing and WAF protection ensure that performance requirements, specifically 99th-percentile search responses under 800ms, are consistently met.