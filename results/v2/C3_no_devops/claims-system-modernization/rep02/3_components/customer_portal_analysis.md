## Overview
The Customer Portal is a React single-page application hosted on Azure Static Web Apps that enables end customers and brokers to submit online claims and track statuses. It serves as the primary modern digital interface within a hybrid cloud claims modernization platform.

## Key Elements
- End Customers
- Brokers
- Customer Portal (React SPA / Azure Static Web Apps)
- Claim Submission Controller
- Status Dashboard View
- Auth Client Module (MSAL.js)
- Feedback & Support Widget
- Azure API Management

## Relationships
- End Customers -> Customer Portal: Submits claims and views status via HTTPS (TLS 1.3)
- Brokers -> Customer Portal: Manages claims and tracks submissions via HTTPS (TLS 1.3)
- Customer Portal -> Azure API Management: Consumes services and synchronizes drafts via HTTPS/REST (OAuth 2.0 / OpenID Connect with PKCE)

## Technology Stack
- React SPA: Chosen for responsive, declarative UI development and mobile browser compatibility
- Azure Static Web Apps: Selected for globally distributed, cost-effective frontend hosting
- MSAL.js: Implements secure in-memory token handling via OAuth 2.0 Authorization Code Flow with PKCE
- Tailwind CSS: Ensures strict mobile responsiveness for field brokers
- Azure API Management: Secures and rate-limits backend API traffic

## Rationale
This architecture decouples the public-facing digital experience from the legacy mainframe while enforcing strict security controls like in-memory token storage. It ensures a responsive, PII-compliant, and mobile-ready portal for users during the multi-year migration.