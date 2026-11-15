## Overview
The Fraud Analyst SPA is a secure, React-based single-page application hosted on AWS S3 and CloudFront that provides fraud analysts and risk managers with case management and explainability tools. It connects to backend APIs over HTTPS to facilitate real-time payment reviews while adhering to PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
* Fraud Analyst SPA (React / Amazon S3 / Amazon CloudFront)
* Case Review Workspace Module (React Component)
* Analytics Dashboard Module (React Component)
* Explainability Renderer (React Sub-component)
* Case Management API (Node.js or Python/FastAPI / ECS Fargate)
* AWS Cognito (Identity Provider)

## Relationships
* Fraud Analyst SPA -> Case Management API: Managing analyst workflows, review queues, and transaction context [HTTPS/REST with OAuth2/OIDC via AWS Cognito]
* Fraud Analyst SPA (Analytics Module) -> Case Management API / Reporting Service: Fetching aggregated metrics and audit logs [HTTPS/REST via AWS Cognito]
* Fraud Analyst SPA (Case Review Module) -> Case Management API: Fetching transaction context and explainability payloads [HTTPS/REST via AWS Cognito]

## Technology Stack
* React: Used for building modular UI components with low maintenance overhead.
* Amazon S3 & Amazon CloudFront: Cost-effective static hosting with global content delivery and security headers.
* AWS Cognito: Manages authentication, RBAC claims, and short-lived JWT access tokens.
* Chart.js / Tailwind CSS: Lightweight visualization libraries for rendering explainability metrics.

## Rationale
This architecture fits the requirements by maintaining a low infrastructure footprint under the 25,000 EUR monthly budget for a 3-person engineering team. It also enforces strict security and auditability controls to meet PCI-DSS Level 1 compliance.