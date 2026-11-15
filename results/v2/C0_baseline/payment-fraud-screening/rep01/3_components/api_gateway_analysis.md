## Overview
The system provides real-time card-not-payment fraud screening for a mid-size payment processor and enables analysts to review suspicious transactions. It processes authorizations with sub-50ms latency while maintaining PCI-DSS Level 1 compliance and a strict budget.

## Key Elements
- Merchants / Payment Gateways
- AWS API Gateway (HTTP APIs)
- AWS WAF
- Edge Tokenizer Lambda Component
- Amazon DynamoDB
- Scoring Engine (AWS Lambda, Go)
- Case Management (ECS Fargate, Node.js/React)
- Amazon Aurora Serverless v2 PostgreSQL
- Fraud Analyst

## Relationships
- Merchant / Payment Gateway -> AWS API Gateway: Submits payment authorizations [HTTPS/TLS, OAuth2/API Keys]
- AWS API Gateway -> AWS WAF: Inspects inbound traffic for threats [AWS WAF Integration]
- AWS API Gateway -> Amazon DynamoDB: Validates idempotency keys and throttling limits [AWS SDK]
- AWS API Gateway -> Scoring Engine: Forwards tokenized payloads for fraud evaluation [gRPC over mTLS]
- Scoring Engine -> Amazon Aurora Serverless v2 PostgreSQL: Reads rules and stores immutable audit trails [PostgreSQL Protocol]

## Technology Stack
- AWS API Gateway (HTTP APIs): Edge routing, schema validation, and rate limiting within budget
- AWS WAF: Edge protection against DDoS and injection attacks without violating latency SLAs
- Amazon DynamoDB: Stateless idempotency and throttling tracking minimizing operational overhead for 3 engineers
- AWS Lambda (Go): High-performance edge tokenization and real-time scoring within 50ms P99 constraint
- Amazon Aurora Serverless v2 PostgreSQL: Relational storage for case management and immutable audit logs

## Rationale
The serverless and managed AWS architecture meets the strict 50ms P99 latency and PCI-DSS Level 1 compliance requirements while operating comfortably within the 25,000 EUR monthly budget. Furthermore, managed services minimize operational overhead, enabling a lean team of three engineers to maintain the platform securely.