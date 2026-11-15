## Overview
A cloud-native Library Management System that provides cataloguing, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU data residency while maintaining high-performance search capabilities.

## Key Elements
* **Library Patrons (Members):** Users accessing self-service search and loan management.
* **Librarians:** Staff managing cataloguing and circulation.
* **Library Administrators:** Oversight users tracking reporting and usage.
* **Library Management System (LMS):** Central cloud-native SaaS software boundary.
* **Payment Gateway:** External system processing fines via Stripe/Adyen.
* **Notification Service:** External provider for reminders via SMTP/APNs/FCM.
* **Digital Content Providers:** External sources for streaming via OverDrive/Adobe DRM.
* **Identity Provider (IdP):** External system handling OIDC/OAuth 2.0 authentication.

## Relationships
* **Users to LMS:** HTTPS (TLS 1.3) via web and mobile UI.
* **LMS to Payment Gateway:** REST/JSON over HTTPS.
* **LMS to Notification Service:** SMTP/APNs/FCM over EU-hosted infrastructure.
* **LMS to Digital Content Providers:** LTI and REST over HTTPS.
* **LMS to Identity Provider:** OpenID Connect (OIDC) / OAuth 2.0 over HTTPS.

## Technology Stack
* **Cloud Platform:** AWS Frankfurt/Azure West Europe for EU-only data residency constraint.
* **Authentication:** OpenID Connect (OIDC) / OAuth 2.0 for institutional SSO and EU privacy compliance.
* **Monitoring:** Prometheus-compatible metrics over HTTPS for <800ms search latency tracking (R-05).
* **Compliance & Infrastructure:** Terraform and OPA for continuous compliance-as-code and geo-fenced CI/CD.

## Rationale
The cloud-native SaaS deployment in EU regions strictly satisfies regional data residency mandates and GDPR. Dedicated OIDC integration, circuit breakers, and Prometheus monitoring ensure institutional security, high availability, and performance SLAs.