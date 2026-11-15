## Overview
Modernizes a 30-year-old regional insurer's legacy mainframe claims platform through a hybrid cloud architecture. Enables incremental claim type migration while ensuring zero data loss and maintaining legacy system operations.

## Key Elements
- **Users**: End Customers & Brokers, Claims Adjusters, Operations Managers & Migration Auditors
- **External Systems**: Legacy Mainframe (COBOL/DB2), Identity Provider (Active Directory / Entra ID), Centralized Audit Sink
- **Containers**: Web Frontend (SPA), Claims API Gateway, Core Claims Service, Mainframe Anti-Corruption Layer (ACL), Integration & Transformation Worker, Operational Observability & Dead-Letter Container
- **Worker Components**: Kafka Event Consumer, Schema & Policy Mapper, Idempotency & State Manager, Mainframe Protocol Dispatcher, Reconciliation & Audit Publisher

## Relationships
- **Kafka Event Consumer** reads from **Mainframe Anti-Corruption Layer** via Apache Kafka / AMQP (SASL/SCRAM or mTLS)
- **Schema & Policy Mapper** queries **Idempotency & State Manager** via TLS-encrypted TCP (port 6380)
- **Schema & Policy Mapper** sends payloads to **Mainframe Protocol Dispatcher** via gRPC/HTTPS
- **Schema & Policy Mapper** emits telemetry to **Reconciliation & Audit Publisher** via OpenTelemetry SDK
- **Reconciliation & Audit Publisher** exports metrics to **Operational Observability & Dead-Letter Container** via HTTPS
- **Integration & Transformation Worker** retrieves secrets from **Azure Key Vault** via Managed Identities (HTTPS)

## Technology Stack
- **Azure Static Web Apps & React**: Powers the modern Web Frontend SPA for adjuster efficiency
- **Azure Container Apps**: Hosts scalable microservices and workers with KEDA-based scaling
- **Azure Event Hubs (Kafka)**: Bridges legacy and modern messaging via Apache Kafka protocol
- **Azure Cache for Redis**: Provides high-performance state storage for idempotency and duplicate prevention
- **Polly**: Implements circuit breaking for robust mainframe integration protection
- **OpenTelemetry & Azure Monitor**: Delivers distributed tracing and reconciliation observability

## Rationale
This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while enabling gradual, low-risk claim migration. Idempotent processing and strict circuit breakers protect system consistency and legacy constraints during the 3-year transition.