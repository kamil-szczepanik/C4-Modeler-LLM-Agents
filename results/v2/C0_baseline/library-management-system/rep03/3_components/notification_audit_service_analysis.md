## Overview
- System: Notification & Audit Service within the Library Management System.
- Purpose: Dispatches multi-channel patron notifications and maintains tamper-evident audit logs ensuring EU data residency and GDPR compliance.

## Key Elements
- Notification & Audit Service (Python / FastAPI Container)
- Event Consumer Component (Background worker)
- Audit Processor Component (Compliance & logging)
- Notification Dispatcher Component (Multi-channel gateway)
- Preference Repository Access Component (User settings)
- External: Message Broker (Kafka / RabbitMQ), Relational DB (PostgreSQL), Centralized Observability & SIEM Platform, Payment Gateway and Notification Service, HashiCorp Vault

## Relationships
- Event Consumer -> Message Broker: Consumes domain events [Kafka / RabbitMQ] via mTLS
- Audit Processor -> Centralized Observability & SIEM Platform: Forwards audit logs via TLS/Syslog
- Notification Dispatcher -> Payment Gateway and Notification Service: Dispatches alerts via HTTPS/REST (TLS 1.3)
- Preference Repository Access -> Relational DB (PostgreSQL): Queries user preferences via JDBC/SQL over mTLS

## Technology Stack
- Python / FastAPI: High-performance async service framework
- Redis / Local Durable Queues: Prevents message loss between internal components
- HashiCorp Vault: Dynamic secret injection and encryption key management
- Prometheus: Consumer lag and dispatch latency metrics

## Rationale
- Durable queuing and decoupled components guarantee at-least-once delivery for the 60-second notification SLA.
- Cryptographically signed audit logs and strict mTLS satisfy EU data residency and GDPR PII protection mandates.