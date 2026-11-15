## Overview
[The Staff Dashboard Container provides library staff and administrators secure, low-latency interfaces for circulation management, cataloging, and operational monitoring. It ensures strict EU data residency while maintaining high performance and strict audit compliance.]

## Key Elements
* Librarians & Library Administrators
* Staff Dashboard Container (Kubernetes, EU-hosted)
* Notification Container (Kubernetes, Kafka/SQS, EU-hosted)
* External Payment Gateway
* Interlibrary Loan (ILL) Network
* WORM Storage Sink
* Fluentbit Sidecar

## Relationships
* Librarians -> Staff Dashboard Container: Manages library operations [HTTPS (TLS 1.3)]
* Library Administrators -> Staff Dashboard Container: Configures and administers system [HTTPS (TLS 1.3)]
* Staff Dashboard Container -> External Payment Gateway: Processes financial transactions with circuit breaker [HTTPS, strict egress]
* Staff Dashboard Container -> Notification Container: Triggers notifications [mTLS via SPIFFE/SPIRE]
* Staff Dashboard Container -> Kafka/SQS: Asynchronous batch processing [TLS]
* Fluentbit Sidecar -> WORM Storage Sink: Streams immutable audit logs [Encrypted TCP]

## Technology Stack
* Kubernetes: Container orchestration for horizontal auto-scaling (HPA) and resource isolation
* Kafka / SQS: Message broker for asynchronous batch processing and decoupled queuing
* OpenTelemetry: Distributed tracing across external payment and notification services
* Fluentbit: Sidecar log shipping for immutable WORM audit trails
* DPoP (Demonstrating Proof-of-Possession): Cryptographic token binding for secure staff sessions
* Vault: Ephemeral runtime secret management for API keys

## Rationale
[This architecture balances high-throughput operational requirements with strict EU data residency and PCI-DSS security constraints. Asynchronous processing and circuit breakers protect backend stability while maintaining cryptographic audit immutability.]