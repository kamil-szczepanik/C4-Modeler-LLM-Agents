## Overview
The system provides real-time payment fraud screening and case management for card-not-present transactions on AWS eu-west-1. It screens payment authorizations, routes suspicious transactions, and supports secure analyst reviews while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- **Case Management Backend**: NestJS (Node.js/TypeScript) container handling analyst workflows, routing, and audit exports.
- **Case API Router**: Sub-component enforcing JWT validation, RBAC, rate limiting, and input sanitization.
- **Data Masking Interceptor**: Sub-component stripping Primary Account Numbers (PAN) to ensure analysts never see full card data.
- **Case Workflow Engine**: Sub-component managing state transitions, bulk resolutions, and analyst SLA tracking.
- **Audit & Compliance Exporter**: Sub-component generating cryptographically signed compliance extracts for 7-year auditability.
- **Feature Store & Metadata DB**: PostgreSQL (RDS) persisting case states, audit logs, and operational metrics.
- **Fraud Analysts & Risk Managers**: Primary and secondary human users accessing the system.
- **Regulators / Audit & Compliance System**: External system receiving signed audit trails.

## Relationships
- **Case Management Web App -> Case Management Backend**: Sends API requests for case management and review workflows [HTTPS / REST, AWS Cognito OAuth 2.0 / OIDC]
- **Case API Router -> AWS Cognito**: Validates JSON Web Tokens (JWT) for authentication [HTTPS / OIDC]
- **Case Workflow Engine -> Feature Store & Metadata DB (RDS)**: Persists case states, analyst notes, and SLA timestamps [TCP / PostgreSQL Wire Protocol]
- **Audit & Compliance Exporter -> Amazon S3 Object Lock**: Reads tamper-evident decision logs [HTTPS / AWS SDK]
- **Audit & Compliance Exporter -> Regulators / Audit & Compliance System**: Pushes cryptographically signed compliance extracts [HTTPS / REST]

## Technology Stack
- **Node.js with NestJS**: Chosen for the Case Management Backend to provide modular architecture, dependency injection, and easy interceptors for data masking within a small three-engineer team.
- **PostgreSQL (Amazon RDS)**: Relational database secured with AWS KMS customer-managed keys for transactional state and metadata storage.
- **AWS Cognito & Secrets Manager**: Provides OAuth 2.0/OIDC authentication, RBAC, and secure private key storage for audit signing.
- **Amazon S3 Object Lock**: Ensures tamper-evident, 7-year retention of decision and audit logs to satisfy regulatory requirements.

## Rationale
This architecture uses modular NestJS components and managed AWS services to securely handle sensitive financial data within a strict 25,000 EUR monthly budget. The design isolates compliance, audit, and masking functions to meet PCI-DSS Level 1 mandates and 7-year auditability constraints while remaining operable by a three-engineer team.