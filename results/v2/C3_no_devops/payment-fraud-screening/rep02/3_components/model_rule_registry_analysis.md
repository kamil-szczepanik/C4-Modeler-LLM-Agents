## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud within strict latency limits and provides case management for fraud analysts. The Model & Rule Registry component enables zero-downtime updates and maintains secure, auditable version control for fraud rules and scoring models.

## Key Elements
- Risk Managers (User Persona)
- Registry API Service (Python, FastAPI)
- Registry Core Engine (Python, FastAPI)
- Metadata Catalog (PostgreSQL, AWS RDS)
- Artifact Storage (Amazon S3 with Object Lock)
- Event Dispatcher (Amazon SQS / EventBridge)
- Supporting Services (AWS Cognito, AWS Secrets Manager, AWS KMS)

## Relationships
- Risk Managers -> Registry API Service: Uploads and approves rules via HTTPS/REST with MFA authentication
- Registry API Service -> Registry Core Engine: Invokes validation and publishing workflow via internal Python function calls
- Registry Core Engine -> Artifact Storage: Writes immutable artifacts using S3 API
- Registry Core Engine -> Metadata Catalog: Persists version lineage and active-state pointers via SQL/JDBC
- Registry Core Engine -> Event Dispatcher: Publishes model release notifications via SQS API
- Registry Core Engine -> AWS Secrets Manager: Retrieves code-signing certificates via AWS SDK

## Technology Stack
- Python with FastAPI: Chosen for the Registry API Service and Core Engine to ensure high-performance schema validation and workflow orchestration.
- Amazon S3 with Object Lock: Provides immutable, tamper-evident artifact storage to meet 7-year auditability constraints.
- PostgreSQL (AWS RDS): Manages version lineage, metadata catalogs, and active-state pointers.
- AWS Cognito: Enforces multi-factor authentication and role-based access control for Risk Managers.
- AWS Secrets Manager: Securely manages code-signing certificates with rotation policies.
- AWS KMS: Encrypts artifacts at rest using customer-managed keys.

## Rationale
This component architecture enforces strict maker-checker segregation and cryptographic validation, ensuring that only verified, secure models reach production without downtime. Additionally, it guarantees PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail while supporting instant rollbacks for risk mitigation.