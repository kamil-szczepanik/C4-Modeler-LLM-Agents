## Overview
The Model/Rule Manager container processes zero-downtime updates for fraud scoring models and rules using a Python and FastAPI service. It securely ingests, validates, signs, and distributes model artifacts while maintaining tamper-evident audit logs.

## Key Elements
- **Data Scientists / Risk Managers**: External users uploading rules and models
- **API Controller**: FastAPI routes handling incoming rule and model upload requests
- **Validator & Compiler**: Validates ONNX compatibility and rule payloads
- **Model Registry Manager**: Stores versioned artifacts and applies cryptographic signatures
- **Distribution Publisher**: Broadcasts model/rule update events and handles automated rollbacks
- **Audit Log Service**: Captures immutable deployment metadata
- **Amazon S3**: Immutable WORM storage with Object Lock and AWS KMS encryption
- **Amazon MSK Serverless**: Event bus for zero-downtime propagation
- **Fraud Scoring Engine**: Consumes updates via Kafka protocol

## Relationships
- Data Scientists -> API Controller: Uploads rules and models via `HTTPS (OAuth2/OIDC via AWS IAM, mTLS)`
- API Controller -> Audit Log Service: Records deployment events via synchronous internal calls
- Validator & Compiler -> Model Registry Manager: Passes verified artifacts via internal function calls
- Model Registry Manager -> Amazon S3: Persists signed bundles via `AWS SDK (HTTPS)`
- Distribution Publisher -> Amazon MSK Serverless: Publishes reload events via `Kafka Protocol`

## Technology Stack
- **Python / FastAPI**: Chosen for rapid development and asynchronous API handling suitable for a 3-person team
- **Amazon S3 with Object Lock**: Implements WORM storage to meet the 7-year tamper-evident audit requirement without database overhead
- **Amazon MSK Serverless**: Enables scalable, serverless event-driven rule distribution
- **AWS KMS**: Secures model artifacts at rest with customer-managed keys
- **ONNX Runtime**: Standardizes model evaluation formats across services

## Rationale
This architecture minimizes operational overhead for a 3-person engineering team by leveraging serverless AWS components while satisfying PCI-DSS Level 1. Strict payload validation and cryptographic signing ensure secure, zero-downtime updates without risking performance SLAs or regulatory compliance.