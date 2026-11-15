## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages case reviews for analysts. It ensures PCI-DSS Level 1 compliance, sub-50ms decision latency, and 7-year tamper-evident auditability within a fixed infrastructure budget.

## Key Elements
- **API Controller**: FastAPI endpoints handling administrative requests over HTTPS.
- **Rule & Model Validator**: Validates rule syntax and ONNX model compatibility.
- **Sandbox Evaluator**: Tests models against historical regression fixtures.
- **Version Registry**: Manages semantic versioning and metadata backed by Amazon Aurora PostgreSQL.
- **Artifact Bundler**: Packages models, configurations, and rules into immutable archives.
- **Distribution Publisher**: Publishes rule sets and ONNX binaries via Amazon S3 and Amazon SNS.
- **Audit Event Emitter**: Emits cryptographically signed audit logs via Amazon SQS.

## Relationships
- API Controller -> Rule & Model Validator [In-memory function call]
- Rule & Model Validator -> Version Registry [SQL/ORM over TLS]
- Rule & Model Validator -> Sandbox Evaluator [In-memory function call]
- Sandbox Evaluator -> Amazon Aurora PostgreSQL [Read historical test fixtures via SQL/ORM over TLS]
- Sandbox Evaluator -> Artifact Bundler [In-memory function call]
- Artifact Bundler -> Distribution Publisher [In-memory function call]
- Distribution Publisher -> Real-Time Scoring Engine [AWS SNS / HTTPS webhook]
- API Controller & Version Registry -> Audit Event Emitter [Internal Event bus]
- Audit Event Emitter -> Audit Worker [Amazon SQS over TLS]

## Technology Stack
- **Python / FastAPI**: Chosen for native Pydantic validation and ONNX runtime ecosystem support.
- **Amazon Aurora PostgreSQL**: Provides robust relational storage for version metadata and test fixtures.
- **Amazon S3 & SNS**: Enables decoupled, reliable distribution of model bundles and atomic hot-reloading.
- **Amazon SQS**: Securely queues tamper-evident audit logs for downstream processing.

## Rationale
This architecture enables zero-downtime model updates and strict audit trails while keeping maintenance overhead minimal for a three-person team. The design ensures cost-efficiency within the 25,000 EUR monthly AWS budget in eu-west-1.