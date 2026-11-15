## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS (eu-west-1) to prevent fraud while maintaining PCI-DSS Level 1 compliance. It enables fraud analysts and risk managers to review suspicious payments via a secure web interface.

## Key Elements
- Fraud Analysts & Risk Managers (Users)
- Case Management Web App (React SPA hosted on Amazon S3 and distributed via Amazon CloudFront)
- Authentication & Session Manager Component (TypeScript, AWS Amplify / Cognito SDK)
- Case Queue & Review Dashboard Component (React, TanStack Table)
- Audit & Reporting Portal Component (React, Recharts)
- API Client Layer (Axios/Fetch Wrapper)
- Case Management Backend (Node.js, Go)
- AWS Cognito (Identity Provider)

## Relationships
- Fraud Analysts & Risk Managers -> Case Management Web App: Accesses UI via HTTPS (TLS 1.3)
- Case Management Web App -> Case Management Backend: Sends API requests via HTTPS / REST using JWTs
- Authentication & Session Manager Component -> AWS Cognito: Handles OIDC token exchange and authentication via HTTPS
- Case Management Web App -> Amazon S3 / CloudFront: Hosted and delivered securely via HTTPS

## Technology Stack
- React SPA: Chosen for responsive UI and cost efficiency under a 25,000 EUR monthly infrastructure budget.
- Amazon CloudFront & S3: Used for secure, low-latency global static asset delivery.
- AWS Cognito & AWS Amplify SDK: Implements OIDC authentication, RBAC, and session management.
- TanStack Table & Recharts: Provides high-throughput case feeds and audit reporting visualizations.
- Axios/Fetch Wrapper: Implements centralized API interception and secure token injection.

## Rationale
This component architecture enforces strict PCI-DSS compliance and role-based access control by keeping all sensitive card data masked and ephemeral. It satisfies performance and budget constraints by leveraging serverless AWS static hosting and secure, scalable API interactions.