## Overview
[The system is a real-time payment fraud screening platform that evaluates payment authorizations and manages suspicious cases. Its core purpose is to screen card-not-present transactions for fraud within strict latency limits while supporting auditability.]

## Key Elements
- Data Scientists and Fraud Analysts (Users)
- Rule & Model Distribution Service (Container)
- Model Validation & Compilation Worker (Component)
- Distribution Coordinator (Component)
- Distribution API (Component)
- Scoring Engine Container (Container)
- Amazon S3 and AWS SQS (Infrastructure)

## Relationships
- Model Validation & Compilation Worker -> Amazon S3: Stores signed artifacts [HTTPS/TLS]
- Distribution Coordinator -> Scoring Engine Container: Triggers hot-reloading [gRPC/AWS SQS]
- Distribution API -> Model Registry: Receives publish requests [REST/JSON]

## Technology Stack
- Python/Pydantic: Used for model validation due to strong typing and schema enforcement.
- Go: Used for the Distribution Coordinator for high performance and low resource consumption.
- AWS S3 and SQS: Used for artifact storage and asynchronous fan-out messaging within budget constraints.
- AWS KMS: Used for cryptographic signature verification and artifact encryption to satisfy PCI-DSS Level 1.

## Rationale
[This architecture enables zero-downtime model updates and strict cryptographic supply chain security. It meets PCI-DSS compliance and performance targets while remaining maintainable by a three-person engineering team.]