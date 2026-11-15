## Overview
This system provides real-time payment fraud screening for card-not-present transactions with sub-50ms latency. It ensures strict PCI-DSS compliance while maintaining high availability and auditable decision trails.

## Key Elements
- **Envoy Proxy:** Edge container handling TLS 1.3 termination, tokenization, routing, and phased circuit breaking.
- **Scoring Engine Container:** Go-based container executing fraud models.
- **Case Management API Container:** Node.js with NestJS container for analyst reviews.
- **Audit & Compliance Ledger Container:** Tamper-evident logging service.
- **Infrastructure Services:** AWS ECS Fargate, AWS Network Load Balancer, Amazon ElastiCache, Amazon Aurora PostgreSQL, AWS QLDB, and AWS Secrets Manager.

## Relationships
- **Payment Gateway -> Envoy Proxy:** Real-time payment authorization screening via [TLS 1.3 / gRPC].
- **Envoy Proxy -> Scoring Engine Container:** Routes authorization requests via [Internal gRPC over mTLS].
- **Envoy Proxy -> Fallback Rules Engine Container:** Routes requests during initial outage phase via [Internal gRPC].
- **Envoy Proxy -> AWS Secrets Manager:** Fetches and rotates TLS certificates via [AWS API].

## Technology Stack
- **Envoy Proxy:** C++ native core with statically compiled filters for sub-millisecond edge routing and minimal memory footprint.
- **AWS ECS with Fargate:** Container orchestration to right-size workloads within the 25,000 EUR monthly budget.
- **Go:** High-performance language for the Scoring Engine meeting the 50ms P99 latency threshold.
- **Node.js with NestJS:** Robust backend framework for the Case Management API.
- **AWS QLDB:** Tamper-evident ledger providing the required 7-year audit trail.

## Rationale
The architecture uses a high-performance C++ edge proxy and Go scoring engine to meet strict 50ms P99 latency at scale. A phased fallback strategy balances security requirements with the 1-minute availability SLA.