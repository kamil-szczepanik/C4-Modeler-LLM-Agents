## Overview
[The Notification Worker Container handles asynchronous notifications and event-driven workflows for the Library Management System. Its core purpose is to deliver timely updates on items, due dates, and reservations while strictly enforcing EU data residency and GDPR compliance.]

## Key Elements
- Notification Worker Container (Go)
- Event Consumer Engine (Go / Sarama/Segmentio)
- Notification Preferences & Consent Manager
- Template & Personalization Engine
- Dispatch Router & Circuit Breaker
- Retry & Dead-Letter Queue (DLQ) Manager
- Message Broker (Apache Kafka / RabbitMQ)
- EU-hosted PostgreSQL & Redis Cache
- External EU Email/SMS Gateways (SendGrid/Twilio EU endpoints)

## Relationships
- Event Consumer Engine -> Message Broker: Consumes domain events [TLS-secured gRPC/AMQP with SASL/SCRAM-V5 and mTLS]
- Event Consumer Engine -> Notification Preferences & Consent Manager: Validates consent [In-Process Function Call / gRPC]
- Notification Preferences & Consent Manager -> Template & Personalization Engine: Forwards filtered payloads [In-Process Function Call]
- Dispatch Router -> EU Email/SMS Gateways: Sends notifications [TLS 1.3 HTTPS/REST with certificate pinning]
- Retry & DLQ Manager -> EU-hosted PostgreSQL: Audits failed messages and drops unconsented events [AES-256 encrypted connection]

## Technology Stack
- Go: Chosen for high-throughput, concurrent event processing and low latency.
- Apache Kafka / RabbitMQ: Used for reliable, decoupled asynchronous event streaming.
- Redis & PostgreSQL: Utilized for consent caching and DLQ auditing, secured with AES-256 encryption-at-rest and EU-only residency.
- TLS 1.3 & mTLS: Implemented for zero-trust transport security across all internal and external communication.

## Rationale
[This architecture ensures sub-60-second notification delivery while rigorously maintaining EU data residency and GDPR Article 21 compliance. Internal component decomposition isolates consent validation and data minimization, protecting patron PII before external gateway transmission.]