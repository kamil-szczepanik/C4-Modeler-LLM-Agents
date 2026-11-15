## Overview
[The Clinic Management System is a hybrid-cloud healthcare platform providing patient registration, EMR, scheduling, and billing. Its core purpose is to deliver 99.99% available, HIPAA-compliant clinical and financial operations.]

## Key Elements
- Billing & Scheduling Service (Node.js / TypeScript container)
- Scheduling Engine Component with Rescheduling & Waitlist Sub-component
- Billing & Estimation Engine Component
- Notification Dispatcher Component
- Data Storage Layer (PostgreSQL with WORM audit storage)
- Apache Kafka & Redis (Redlock)
- Istio Service Mesh & API Gateway (Kong / NGINX Ingress)

## Relationships
- API Gateway -> Billing & Scheduling Service: HTTP routing
- Billing & Scheduling Service -> Data Storage Layer: TLS-encrypted SQL
- Billing & Scheduling Service -> Insurance Payment Gateways: Asynchronous messaging via Apache Kafka
- Scheduling Engine Component -> Billing & Estimation Engine Component: In-process TypeScript function calls
- Notification Dispatcher Component -> Patient Portal: Server-Sent Events / WebSocket via API Gateway

## Technology Stack
- Node.js / TypeScript: Runtime and language for the container and internal components
- Redis: Distributed locking (Redlock) and state management for HPA
- Apache Kafka: Asynchronous event messaging and DLQ for claims
- Istio Service Mesh: Mutual TLS (mTLS), circuit breaking, and rate limiting
- HashiCorp Vault: Dynamic secret injection for databases and APIs

## Rationale
[This architecture uses a hybrid-cloud Node.js microservices approach backed by Redis distributed locks and Kafka to meet strict 99.99% availability and high-performance requirements. Robust Istio mesh controls, vault-managed secrets, and HIPAA-compliant encryption ensure security and regulatory compliance.]