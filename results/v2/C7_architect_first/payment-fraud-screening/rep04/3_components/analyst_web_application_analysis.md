## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations and provides case management for fraud analysts. Its core purpose is to block fraudulent transactions instantly while maintaining PCI-DSS Level 1 compliance and a 7-year audit trail.]

## Key Elements
* Fraud Analyst
* Analyst Web Application (React, TypeScript, MUI) hosted on AWS S3 and served via AWS CloudFront
* Backend-for-Frontend (BFF) proxy layer (AWS Lambda / API Gateway)
* Identity Provider (IdP)
* Case Management API (Go, Node.js/TypeScript, AWS ECS Fargate)

## Relationships
* Fraud Analyst -> Analyst Web Application: Performs case reviews [HTTPS]
* Analyst Web Application -> BFF proxy layer: Communicates for session and API requests [HTTPS]
* BFF proxy layer -> Identity Provider (IdP): Manages OIDC/PKCE token exchange [HTTPS]
* BFF proxy layer -> Case Management API: Forwards API requests [HTTPS with Bearer Token]

## Technology Stack
* React, TypeScript, MUI: Selected for the SPA frontend to ensure rapid UI development for the 3-engineer team.
* AWS S3 & CloudFront: Chosen for static asset hosting to eliminate idle infrastructure costs and stay within the 25,000 EUR/month budget.
* AWS Lambda / API Gateway: Implements the Backend-for-Frontend (BFF) pattern to isolate sensitive tokens.
* HttpOnly, Secure, SameSite=Strict Cookies: Utilized by the BFF for secure token storage to satisfy PCI-DSS Level 1 compliance (R-05).

## Rationale
[This architecture uses serverless frontend hosting and a BFF security pattern to strictly meet PCI-DSS Level 1 card data protection mandates and budget constraints. It empowers a 3-engineer team to operate reliably while supporting rapid fraud analyst workflows.]