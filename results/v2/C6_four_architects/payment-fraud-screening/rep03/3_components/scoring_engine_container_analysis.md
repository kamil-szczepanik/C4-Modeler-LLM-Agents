## Overview
This system provides real-time payment fraud screening for card-not-present transactions, evaluating authorizations and managing reviews while ensuring strict compliance. It processes up to 3,000 requests per second within sub-50ms latencies on AWS.

## Key Elements
- API Handler Component (Go, net/http / gRPC)
- Sanitization & Tokenization Guard Component (Go)
- Feature Fetcher Component (Go concurrency primitives)
- Circuit Breaker & Fallback Component (Go)
- Inference Engine Component (C++ via cgo, ONNX Runtime)
- Model Loader Component (Go)
- Decision Explainer Component (Go)
- Audit & Persistence Component (Go, AWS SDK)
- External Systems: AWS ALB, ML Feature Store, Tokenization Proxy Container (AWS Nitro Enclaves), Amazon DynamoDB, Amazon S3 Object Lock

## Relationships
- AWS ALB -> API Handler Component: Routes external authorization traffic [HTTPS/gRPC]
- API Handler Component -> Sanitization & Tokenization Guard Component: Internal Go call
- Sanitization & Tokenization Guard Component -> Tokenization Proxy Container: Tokenizes card data [gRPC/mTLS over internal VPC]
- Feature Fetcher Component -> ML Feature Store: Retrieves real-time features [gRPC]
- Feature Fetcher Component -> Circuit Breaker & Fallback Component: Go error handling / interface call
- Circuit Breaker & Fallback Component -> Inference Engine Component: Passes feature vector [Go function call]
- Model Loader Component -> Inference Engine Component: Hot-swaps models [In-memory pointer swap]
- Inference Engine Component -> Decision Explainer Component: In-memory Go struct passing
- Decision Explainer Component -> Audit & Persistence Component: Asynchronous event emission via Go channel
- Audit & Persistence Component -> Amazon DynamoDB / Amazon S3 Object Lock: Writes hot state and tamper-evident audit logs [AWS SDK]

## Technology Stack
- Go: Chosen for high concurrency and low-latency API handling and feature orchestration.
- C++ via cgo & ONNX Runtime: Executes compiled fraud scoring models in-memory for microsecond-level latency.
- AWS ECS Fargate: Provides a fixed-budget, serverless container execution environment.
- Amazon S3 Object Lock & DynamoDB: Ensures tamper-evident, 7-year audit log retention for regulatory compliance.
- AWS Nitro Enclaves: Isolates tokenization to achieve PCI-DSS Level 1 compliance.

## Rationale
This architecture leverages in-memory C++ inference and asynchronous logging to consistently achieve sub-50ms P99 latency under high throughput. Isolated tokenization enclaves and tamper-evident S3 storage satisfy stringent PCI-DSS Level 1 and auditability mandates within a fixed budget.