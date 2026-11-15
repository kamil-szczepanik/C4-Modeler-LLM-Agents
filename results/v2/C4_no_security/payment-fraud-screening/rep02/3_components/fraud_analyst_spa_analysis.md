## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time to prevent fraud. It provides an intuitive interface for fraud analysts to review suspicious transactions securely.

## Key Elements
- Fraud Analyst & Risk Manager (Person)
- Fraud Analyst SPA (React on Amazon S3 / CloudFront)
- Routing & Auth Module (TypeScript/React Router)
- Case Management View & Feedback Component (React)
- XAI Visualization Component (D3.js/Chart.js)
- API Client Layer (Axios/Fetch)
- Case Management Backend Container (Amazon ECS Fargate)
- AWS WAF & CloudFront Functions

## Relationships
- Fraud Analyst & Risk Manager -> Fraud Analyst SPA: Accesses UI [HTTPS/REST]
- Routing & Auth Module -> Fraud Analyst SPA: Manages OAuth2/OIDC sessions
- Case Management View & Feedback Component -> API Client Layer: Triggers data payloads [HTTPS/REST]
- API Client Layer -> Case Management Backend Container: Transmits API requests with OAuth2 bearer tokens [HTTPS/REST]
- AWS WAF -> Fraud Analyst SPA: Enforces CSP, HSTS, and rate-limiting at the edge

## Technology Stack
- React / TypeScript: Minimizes cognitive load for a 3-person engineering team
- Amazon S3 / CloudFront: Provides zero-maintenance, low-cost static asset delivery
- D3.js / Chart.js: Renders explainable AI (XAI) feature-contribution graphs
- Axios / Fetch: Handles secure communication with strict CORS and token-header injection
- AWS WAF: Secures the edge against malicious web traffic and enforces compliance headers

## Rationale
This architecture uses serverless static hosting to stay within the 25,000 EUR monthly budget and lean team constraints. Client-side tokenization and strict edge security enforce PCI-DSS compliance while delivering sub-second response times for fraud analysts.