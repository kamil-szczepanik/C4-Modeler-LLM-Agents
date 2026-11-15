## Overview
The Library Management System is a solution for public and academic libraries to catalogue items and manage circulation while adhering to EU-only data residency. The Audit Container ensures regulatory compliance, tamper-proof event logging, and system trust.

## Key Elements
* Audit Container (Go)
* Audit Database (PostgreSQL with Row-Level Security)
* Message Broker (Apache Kafka/RabbitMQ)
* SIEM / Log Forwarder (Filebeat / Syslog)
* Admin Dashboard
* System Administrators & Compliance Officers

## Relationships
* Message Broker -> Audit Container (Go): Consumes security events via mTLS and SASL/SCRAM [Kafka Protocol]
* Audit Container (Go) -> Audit Database (PostgreSQL): Persists append-only WORM records via TLS 1.3 [TCP/SQL]
* Audit Container (Go) -> SIEM / Log Forwarder: Forwards audit logs for compliance reporting [Syslog/HTTPS]
* Audit Container (Go) -> Admin Dashboard: Exposes Prometheus health metrics for ingestion uptime [HTTP]

## Technology Stack
* Go: Chosen for high performance and lightweight concurrency in event processing
* PostgreSQL: Provides immutable WORM persistence and Row-Level Security for EU compliance
* Apache Kafka/RabbitMQ: Enables decoupled, reliable event ingestion with dead-letter queue support
* Prometheus: Powers ingestion throughput and consumer lag monitoring via `/metrics` endpoints
* Kubernetes: Manages container deployment, scaling, and graceful shutdown via SIGTERM traps

## Rationale
This architecture fits the requirements by strictly isolating compliance logic into a secure, hardened WORM container. It guarantees EU data residency and tamper resistance through cryptographic hash chaining while offloading reporting to external SIEM tools.