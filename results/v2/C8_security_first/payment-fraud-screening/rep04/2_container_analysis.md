## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, providing sub-50ms scoring decisions while maintaining PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail. It balances strict financial security, high availability, and operational efficiency within a fixed 25,000 EUR/month budget managed by a three-engineer team.

## Key Elements
*   **Fraud Analysts**: Users who review suspicious payments via the case management interface.
*   **Compliance & Audit Officer**: Users who verify tamper-evident audit logs and system decisions.
*   **Envoy Proxy**: Ingress container handling external TLS 1.3 termination and gRPC routing.
*   **Scoring Engine Container**: Stateless microservice executing real-time fraud models with a local heuristic fallback engine.
*   **Case Management API Container**: Handles analyst workflows and review queues.
*   **Audit & Compliance Ledger Container**: Captures immutable decision payloads, inputs, and model versions.
*   **Amazon Aurora PostgreSQL & AWS QLDB**: Managed databases for operational data and tamper-evident audit trails.
*   **Amazon ElastiCache / SQS**: Buffers audit data and decouples real-time payment ingestion.
*   **AWS ECS on EC2**: Container orchestration platform in region eu-west-1.

## Relationships
*   **Payment Gateway** calls **Envoy Proxy** via TLS 1.3 for real-time payment authorization screening (R-01).
*   **Envoy Proxy** routes authorization requests to **Scoring Engine Container** using internal gRPC over mTLS.
*   **Scoring Engine Container** publishes asynchronous audit events to **Amazon ElastiCache / SQS** to protect sub-50ms latency.
*   **Audit & Compliance Ledger Container** consumes events from queue and writes tamper-evident records to **AWS QLDB** (R-06).
*   **Fraud Analysts** access **Case Management API Container** via corporate IdP authentication to review flagged transactions (R-02).
*   **Case Management API Container** reads and writes operational state to **Amazon Aurora PostgreSQL** via TLS.

## Technology Stack
*   **Cloud Provider**: AWS (Region: eu-west-1) chosen for robust managed compliance services and regional availability.
*   **Container Orchestration**: AWS ECS on EC2 for precise cost control and resource governance within the 25,000 EUR/month budget.
*   **Ingress & Routing**: Envoy Proxy for secure, high-performance edge termination and gRPC traffic distribution.
*   **Scoring Service**: Go for high-throughput, low-latency execution ensuring P99 latency remains below 50ms (R-04).
*   **Case Management API**: Node.js with NestJS for rapid development of analyst workflows.
*   **Stream Buffering**: Amazon ElastiCache / SQS to decouple audit logging without the operational toil of Kafka.
*   **Data & Audit Storage**: Amazon Aurora PostgreSQL and AWS QLDB for relational data and tamper-evident 7-year audit logs (R-06).

## Rationale
The architecture utilizes stateless Go microservices on AWS ECS on EC2 to achieve the required 3,000 TPS and sub-50ms P99 latency while strictly respecting the 25,000 EUR monthly budget and three-engineer team constraint. By integrating a local heuristic fallback engine, mTLS isolation, and AWS QLDB, the system satisfies stringent PCI-DSS Level 1 compliance and 7-year auditability without compromising availability or introducing critical points of failure.