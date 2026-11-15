## Overview
The Case Management UI is a React Single Page Application hosted on AWS S3 and CloudFront that provides fraud analysts with tools to review suspicious payment transactions. It delivers secure queue prioritization, masked card data rendering, and decision explainability visualization while complying with PCI-DSS Level 1.

## Key Elements
- Fraud Analyst (Person)
- Case Management UI (React Container)
  - Authentication Wrapper Component
  - Dashboard & Queue View Component
  - Case Detail & Explainability View Component
  - Action & Audit Logger Component
- Case Management Backend (Node.js Container)
- Identity Provider (IdP) (External System)

## Relationships
- Fraud Analyst -> Authentication Wrapper: Authenticates session [HTTPS / OIDC]
- Authentication Wrapper -> Identity Provider (IdP): Manages OIDC session [HTTPS / OIDC]
- Dashboard & Queue View -> Case Management Backend: Fetches prioritized queues and SLA metrics [HTTPS / REST]
- Case Detail & Explainability View -> Case Management Backend: Retrieves transaction details and model feature attributions [HTTPS / REST]
- Action & Audit Logger -> Case Management Backend: Submits analyst decisions and audit payloads [HTTPS / REST]

## Technology Stack
- React SPA: Chosen for rapid analyst workflows and streamlined component architecture.
- AWS S3 & CloudFront: Selected for zero operational overhead, global caching, and strict CSP header enforcement.
- HttpOnly, SameSite=Strict Cookies: Mandated for secure OIDC token storage against XSS.

## Rationale
This architecture fits the requirements by maintaining strict PCI-DSS scope separation and auditability within a 3-engineer team capacity. Leveraging managed AWS services and stateless frontend components keeps infrastructure costs well below the 25,000 EUR monthly budget.