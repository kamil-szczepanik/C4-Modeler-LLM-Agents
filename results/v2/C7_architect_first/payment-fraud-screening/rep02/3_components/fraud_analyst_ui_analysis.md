## Overview
The Fraud Analyst UI is a React Single Page Application hosted on Amazon S3 and delivered via Amazon CloudFront to review suspicious payments. It enables fraud analysts to manage queues, inspect transactions, update rules, and submit feedback while enforcing PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts
- Authentication Module (React / AWS Amplify, AWS Cognito)
- Case Dashboard & Queue (React, TanStack Table)
- Transaction Inspector with Decision Feedback Widget (React)
- Rule & Model Management Panel (React)
- Case Management Backend (Node.js / TypeScript, Amazon ECS Fargate)
- Observability Service (AWS RUM, AWS X-Ray)

## Relationships
- Fraud Analysts -> Authentication Module [HTTPS / Browser]
- Authentication Module -> Case Dashboard & Queue [In-memory state via React Context API]
- Case Dashboard & Queue, Transaction Inspector, Rule Management Panel -> Case Management Backend [HTTPS / REST with Authorization: Bearer JWT]
- Decision Feedback Widget -> Case Management Backend [HTTPS / REST]

## Technology Stack
- React SPA: Chosen for rich interactive UI capabilities within a lean three-engineer team constraint.
- Amazon S3 & CloudFront: Selected for static asset delivery, maintaining a budget under 25,000 EUR/month.
- AWS Cognito: Utilized for MFA, session management, and short-lived JWTs.
- AWS RUM & OpenTelemetry: Deployed for client-side observability and performance tracking.

## Rationale
This architecture fits requirements by maintaining a low-overhead, highly secure single-repository SPA that integrates seamlessly with backend services. It ensures PCI-DSS compliance, strict role-based access, and reliable case management within the fixed infrastructure budget.