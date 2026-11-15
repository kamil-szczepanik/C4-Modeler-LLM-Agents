## Overview
[The Case Management & Admin UI system provides fraud analysts with a secure interface to review suspicious payment authorizations, manage cases, and update fraud rules without downtime. It is deployed on AWS to maintain strict PCI-DSS compliance and support 7-year auditability.]

## Key Elements
* Fraud Analysts
* Case Management & Admin UI (Web UI)
* Backend-For-Frontend (BFF) Container (AWS Fargate)
* Single Page Application (SPA) Frontend (AWS CloudFront / Amazon S3)
* AWS Cognito
* Amazon CloudWatch

## Relationships
* Fraud Analysts -> Case Management & Admin UI (SPA): Accesses interface [HTTPS]
* SPA -> BFF Container: Communicates via API calls [HTTPS/REST]
* BFF Container -> AWS Cognito: Authenticates users and manages sessions [OIDC/HTTPS]
* BFF Container -> Downstream Services: Fetches and updates case data [HTTPS/REST]
* BFF and SPA -> Amazon CloudWatch: Emits structured logs and distributed traces [AWS SDK]

## Technology Stack
* AWS CloudFront and Amazon S3: Hosts the SPA for cost-effective global delivery
* React or Vue: Lightweight frontend framework for high-performance rendering
* Ant Design or MUI: Pre-built component library to accelerate development with a 3-engineer team
* AWS Fargate (ECS): Runs the BFF container to securely handle session management and API aggregation
* AWS Cognito: Managed identity provider for secure Role-Based Access Control (RBAC)
* Pact and Playwright: Automated contract and end-to-end testing frameworks for CI/CD pipeline reliability

## Rationale
[This architecture leverages serverless and managed AWS services to minimize operational overhead for a three-engineer team while strictly enforcing PCI-DSS compliance. The BFF pattern and secure cookie management protect sensitive payment data while ensuring robust auditability.]