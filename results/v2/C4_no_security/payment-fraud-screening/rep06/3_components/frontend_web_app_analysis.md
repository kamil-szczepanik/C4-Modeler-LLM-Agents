## Overview
The system provides real-time payment fraud screening for a mid-size payment processor and includes a secure case management frontend for fraud analysts. It is designed to evaluate card-not-present transactions, enforce PCI-DSS Level 1 compliance, and maintain a strict 7-year audit trail.

## Key Elements
- Frontend Web App (React SPA)
- Authentication & Session Manager (TypeScript, OIDC/OAuth2)
- Case Management Dashboard (React, Tailwind CSS)
- Rule & Model Configurator (React)
- API Client Layer (Axios/Fetch)
- AWS S3 & CloudFront (CDN)
- AWS WAF & AWS Cognito
- Case Management & Analytics API

## Relationships
- Case Management Dashboard -> API Client Layer: Invokes RESTful operations [HTTPS/REST, JSON]
- Rule & Model Configurator -> API Client Layer: Submits dry-run simulations and rule updates [HTTPS/REST, JSON]
- Authentication & Session Manager -> AWS Cognito: Authenticates analysts and manages OIDC tokens [HTTPS/OAuth2]
- Frontend Web App (CloudFront/S3) -> Case Management & Analytics API: Communicates via strict CORS-enforced [HTTPS]
- AWS WAF -> CloudFront distribution: Blocks web exploits and enforces rate-limiting at the edge [HTTPS]

## Technology Stack
- React SPA & TypeScript: Powers a responsive, modular user interface with low maintenance overhead for a 3-engineer team.
- AWS S3 & CloudFront: Provides secure, serverless static asset hosting to minimize operational toil and fit the 25,000 EUR monthly budget.
- AWS Cognito: Delivers managed OIDC/OAuth2 authentication and RBAC session handling.
- AWS WAF: Secures the edge distribution against OWASP Top 10 vulnerabilities and brute-force attacks to ensure PCI-DSS compliance.

## Rationale
This architecture leverages serverless static hosting and managed AWS security services to minimize operational overhead, fitting a 3-engineer team and a strict 25,000 EUR monthly budget. It strictly isolates sensitive payment data through tokenization and secure TLS boundaries, satisfying PCI-DSS Level 1 and 7-year auditability requirements.