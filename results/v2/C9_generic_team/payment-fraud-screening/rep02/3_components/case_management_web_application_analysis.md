## Overview
The Case Management Web Application provides a secure interface for fraud analysts to review suspicious payment transactions. It utilizes a lightweight Backend-for-Frontend architecture to ensure strict data masking and compliance.

## Key Elements
- Fraud Analyst (Human User)
- Case Management Web Application (AWS ECS on Fargate BFF container)
- Frontend Static Assets (AWS S3 & Amazon CloudFront SPA)
- Downstream Services (Async Event Bus & Tamper-Evident Audit Storage)
- Monitoring & Security (AWS CloudWatch, AWS X-Ray, AWS Inspector/Trivy)

## Relationships
- Fraud Analyst -> Amazon CloudFront: Accesses review interface [HTTPS/TLS]
- Case Management Web Application -> Async Event Bus: Consumes case events and publishes analyst resolutions [AWS SQS/SNS]
- Case Management Web Application -> Audit & Compliance Storage: Writes immutable audit logs of analyst actions [S3 API/HTTPS]
- AWS CloudWatch -> Case Management Web Application: Scrapes RED method operational metrics [CloudWatch Agent]

## Technology Stack
- AWS ECS on Fargate: Hosts the Backend-for-Frontend API with low operational overhead
- Amazon S3 & CloudFront: Hosts decoupled SPA frontend static assets to reduce container load
- Redis: Manages stateless session storage for horizontal scaling
- OpenAPI: Enforces schema validation and contract testing between BFF and services
- AWS X-Ray & CloudWatch: Provides distributed tracing and RED method metrics monitoring
- Trivy / AWS Inspector: Performs automated vulnerability scanning and SBOM management

## Rationale
This architecture decouples static UI assets from backend API logic, minimizing resource consumption and keeping operational overhead manageable for a three-engineer team. It enforces strict data tokenization and immutable audit logging at the BFF boundary, ensuring full PCI-DSS Level 1 compliance and 7-year auditability within budget.