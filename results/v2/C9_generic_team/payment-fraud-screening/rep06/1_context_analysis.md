## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for suspicious transactions. It processes 3,000 TPS in AWS region eu-west-1 while adhering to PCI-DSS Level 1 compliance and a strict €25,000 monthly budget.

## Key Elements
* Payment Gateway (External System)
* Fraud Analysts (Actors)
* API Gateway with Fail-Open Circuit Breaker (Container)
* Stateless Scoring Service using Rust/Go and embedded ONNX model runtimes (Container)
* Case Management and Audit Service (Container)
* Decoupled Configuration Store for rules and model weights (Container)
* Managed Database / WORM Object Storage for 7-year tamper-evident audit logs (Container)
* Dead-Letter Queues (DLQs) for asynchronous isolation (Container)

## Relationships
* Payment Gateway invokes API Gateway via HTTPS using versioned OpenAPI contracts.
* API Gateway routes synchronous scoring requests to the Stateless Scoring Service via gRPC/HTTP.
* Stateless Scoring Service reads models and rules from the Decoupled Configuration Store.
* Stateless Scoring Service asynchronously pushes audit events and case data to DLQs and storage via AWS SDK.
* Fraud Analysts access the Case Management service via HTTPS.

## Technology Stack
* AWS (eu-west-1): Target cloud provider for managed infrastructure.
* Go or Rust: Compiled languages chosen for low memory footprint and predictable performance.
* ONNX: Embedded model runtime for sub-50ms P99 scoring latency without GPU clusters.
* Terraform: Infrastructure as Code for environment parity and PCI-DSS compliance automation.
* Managed AWS Services (DynamoDB / Aurora Serverless / S3 WORM): Chosen to minimize operational overhead for a three-engineer team.

## Rationale
The architecture achieves sub-50ms latency and high availability through compiled runtimes, managed AWS services, and a strict synchronous-asynchronous split. It satisfies stringent compliance and budget constraints using serverless cost controls, IaC automation, and immutable audit patterns suited for a three-engineer team.