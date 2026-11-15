## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It ensures strict EU data residency compliance while meeting high-performance search requirements.

## Key Elements
- Library Patrons (Students, Public)
- Librarians and Circulation Staff
- Library Administrators
- Library Management System (LMS)
- Identity Provider (Auth0 EU / Keycloak)
- Payment Gateway (Stripe EU)
- Notification Service (Twilio EU / SendGrid)
- Digital Content Providers (OverDrive/Libby APIs)
- EU-hosted Log & Metrics Aggregator (OpenTelemetry / Grafana Cloud EU)

## Relationships
- Patrons/Staff to LMS: HTTPS (TLS 1.3) via Web/Mobile
- LMS to Identity Provider: OIDC/OAuth2 over HTTPS
- LMS to Payment Gateway & Notification Service: HTTPS/REST
- LMS to Digital Content Providers: HTTPS/REST

## Technology Stack
- EU-region cloud infrastructure (AWS Frankfurt or Azure West Europe) for EU-only data residency
- Auth0 EU or Keycloak for OIDC/OAuth2 authentication and GDPR compliance
- Stripe EU for secure fine and fee processing
- OpenTelemetry collector / Grafana Cloud EU for EU-perimeter log and metric aggregation
- Internal caching/proxy layer for metadata search performance and rate limit mitigation

## Rationale
Hosting infrastructure and third-party integrations exclusively within the EU perimeter ensures strict adherence to data residency and GDPR constraints. Incorporating an internal caching layer and asynchronous ingestion workers guarantees sub-800ms search response times and resilience against external vendor outages.