## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud within strict performance and compliance constraints. It provides real-time scoring, case management for analysts, and tamper-evident audit logging on AWS.

## Key Elements
- **API Handler (`Go`)**: Manages inbound gRPC requests from the API Gateway.
- **Token Sanitizer (`Go`)**: Redacts and tokenizes raw Primary Account Numbers (PAN).
- **Rule Engine (`Go`)**: Evaluates deterministic business rules in-memory.
- **Model Runner (`Go` + ONNX Runtime)**: Executes compiled machine learning models locally.
- **Audit Logger (`Go`)**: Asynchronously generates and persists tamper-evident decision logs.
- **Data Store (`Amazon Aurora PostgreSQL`)**: Stores transactional data and audit logs.

## Relationships
- API Gateway -> API Handler: Routes authorization requests via gRPC.
- API Handler -> Token Sanitizer: Passes raw requests via synchronous in-process calls.
- Token Sanitizer -> Rule Engine & Model Runner: Forwards sanitized feature vectors via synchronous in-process calls.
- Rule Engine & Model Runner -> Audit Logger: Dispatches event data via Go channels.
- Audit Logger -> Data Store: Writes audit logs via TCP.

## Technology Stack
- **Go**: Chosen for high concurrency and low memory footprint to meet P99 < 50ms latency at 3,000 RPS.
- **ONNX Runtime**: Enables low-latency in-process machine learning model execution without network hops.
- **Amazon Aurora PostgreSQL**: Provides reliable, ACID-compliant storage for transactions and 7-year audit requirements.
- **AWS ECS Fargate**: Minimizes operational overhead for a 3-engineer team within a 25,000 EUR monthly budget.

## Rationale
This architecture achieves sub-50ms latency and high availability by executing scoring logic in-process without network overhead. It strictly enforces PCI-DSS compliance and 7-year auditability while remaining maintainable for a three-engineer team.