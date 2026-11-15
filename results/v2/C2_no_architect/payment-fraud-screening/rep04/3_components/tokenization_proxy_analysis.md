## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations for a mid-size payment processor. Its core purpose is to screen transactions, route suspicious payments to analysts, and maintain PCI-DSS compliance under strict latency limits.]

## Key Elements
- Real-Time Scoring Engine (AWS ECS Fargate, ECS Service Connect)
- Tokenization Proxy (AWS ECS Fargate)
- AWS KMS and AWS CloudHSM
- Payment Gateway / Shoppers
- Fraud Analysts & Risk Managers

## Relationships
- Payment Gateway -> Real-Time Scoring Engine: Sends authorization requests [HTTPS/JSON]
- Real-Time Scoring Engine -> Tokenization Proxy: Tokenizes sensitive payment data [gRPC with mTLS]
- Tokenization Proxy -> AWS KMS / CloudHSM: Performs format-preserving cryptographic tokenization [AWS SDK / TLS]

## Technology Stack
- Compute: AWS ECS Fargate for containerized microservices deployment within the 25,000 EUR budget
- Security: AWS KMS and AWS CloudHSM for stateless vaultless format-preserving encryption satisfying PCI-DSS Level 1
- Protocol: gRPC with mTLS via AWS Private CA for low-latency, secure internal communication
- Language: Go for the Tokenization Proxy to ensure high performance and minimal memory footprint

## Rationale
[This architecture enforces strict PCI-DSS Level 1 compliance and secure cryptographic isolation without violating the 50ms P99 latency requirement or the 25,000 EUR monthly budget constraint. Stateless vaultless tokenization eliminates vulnerable database caches, protecting sensitive data while meeting high-throughput demands.]