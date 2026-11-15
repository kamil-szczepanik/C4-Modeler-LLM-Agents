## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides a case management interface for analysts. It processes payments securely while maintaining strict compliance, auditability, and budgetary constraints.

## Key Elements
- Fraud Analysts (System Users)
- External Payment Gateway (External System)
- API Gateway / Ingestion Service (Container)
- Scoring Engine (Container)
- Case Management & Admin UI (Container)
- Amazon S3 with Object Lock (Storage)
- Amazon SQS (Message Queue)
- AWS ECS with Fargate (Orchestration)

## Relationships
- External Payment Gateway sends authorization requests to API Gateway / Ingestion Service via HTTPS/REST.
- API Gateway / Ingestion Service forwards scoring payloads to Scoring Engine via gRPC/Protobuf.
- Scoring Engine writes tamper-evident audit logs to Amazon S3 with Object Lock via AWS SDK.
- Fraud Analysts interact with Case Management & Admin UI via HTTPS/REST.
- Scoring Engine delegates asynchronous failure events to Amazon SQS.

## Technology Stack
- AWS Fargate: Container orchestration to maintain low operational overhead for a three-person team.
- Rust, Go, or Java with embedded ML runtimes: High-performance backend technologies to ensure P99 latency below 50 ms.
- Amazon S3 with Object Lock: WORM storage to meet the 7-year tamper-evident audit requirement.
- Amazon SQS: Dead-letter queue for reliable asynchronous event processing without blocking primary transaction paths.
- OpenAPI/Protobuf: Strict API contract definitions to prevent schema drift between services.

## Rationale
The architecture limits container count and leverages AWS managed services to minimize operational toil for a three-person team within a €25,000 monthly budget. High-performance runtimes, circuit breakers, and rolling deployments ensure strict P99 latency, high availability, and PCI-DSS compliance.