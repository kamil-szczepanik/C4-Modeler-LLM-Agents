## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized clinics. It ensures HIPAA and GDPR compliance with 99.99% high availability.]

## Key Elements
* Billing Specialist & Clinic Administrator (Users)
* Billing Operations UI Container (React / Nginx)
* Billing & Integration Service (FastAPI)
* API Gateway (Kong / Node.js)
* Enterprise Identity Provider (IdP)

## Relationships
* API Gateway -> Billing Operations UI Container: Routes billing traffic [HTTPS]
* Billing Operations UI Container -> Billing & Integration Service: Communicates for billing and real-time updates [HTTPS/REST, SSE with JWT]
* Billing Operations UI Container -> Enterprise Identity Provider (IdP): Authenticates users [OIDC / OAuth 2.0]

## Technology Stack
* React: Frontend framework for dynamic billing dashboards and component-level RBAC.
* Nginx: Web server delivering the SPA, terminating TLS 1.3, and injecting strict security headers.
* FastAPI: Backend service powering billing operations and insurance claim submissions.
* Server-Sent Events (SSE): Protocol for real-time claim status push updates over HTTPS.

## Rationale
[This architecture uses a secure React and Nginx Single Page Application behind an API Gateway to deliver a responsive, low-latency UI for billing specialists. Enforcing strict security controls like HttpOnly cookies, RBAC, and TLS 1.3 ensures full HIPAA and GDPR compliance.]