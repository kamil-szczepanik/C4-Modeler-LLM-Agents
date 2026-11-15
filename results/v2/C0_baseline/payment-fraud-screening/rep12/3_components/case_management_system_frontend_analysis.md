## Overview
- Provides a React-based single-page application hosted on Amazon S3 and delivered via Amazon CloudFront for fraud analysts and risk managers.
- Enables case management, transaction reviews, and zero-downtime rule updates while strictly enforcing data masking for PCI-DSS compliance.

## Key Elements
- Fraud Analysts and Risk Managers (Users)
- Case Management System Frontend (React SPA on AWS S3 + CloudFront)
- Case Queue Component (React Component)
- Transaction Details Component (React Component)
- Rule Management Component (React Component)
- Audit Log Viewer Component (React Component)
- Amazon API Gateway / Case Management System API (Backend Services)
- AWS WAF (Security)

## Relationships
- Users access the frontend over HTTPS via Amazon CloudFront.
- Frontend communicates with backend services using HTTPS / JSON REST API with short-polling via React Query.
- AWS WAF inspects inbound requests at CloudFront to protect against attacks.

## Technology Stack
- React SPA: UI framework for a responsive single-page application experience.
- React Query: Manages state and short-polling data fetching.
- Amazon S3 & CloudFront: Static asset hosting and content delivery within budget constraints.
- AWS WAF: Edge security to mitigate DDoS and XSS risks.
- HttpOnly Cookies: Secure session token storage.

## Rationale
- Stateless short-polling and server-less static hosting minimize infrastructure complexity for a three-engineer team.
- Strict client-side masking and HttpOnly token management ensure PCI-DSS compliance and robust security.