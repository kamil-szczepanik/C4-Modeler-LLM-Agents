## Overview
The Circulation Service is a Spring Boot Java enterprise container within the Library Management System, responsible for enforcing lending policies, managing loans, processing fines, and triggering notifications while ensuring EU data residency compliance.

## Key Elements
- Loan Management Component (Spring Boot Java)
- Fine & Fee Component (Spring Boot Java)
- Policy Engine Component (Spring Boot Java)
- Notification Dispatcher Component (Spring Boot Java)
- PostgreSQL
- Third-Party Payment Processor
- Event Bus (Apache Kafka / RabbitMQ)

## Relationships
- Web Application / API Gateway -> Circulation Service: Routes circulation queries and commands [gRPC / REST]
- Loan Management Component -> PostgreSQL: Persists transaction history [JDBC, TLS 1.3, EU region]
- Fine & Fee Component -> Third-Party Payment Processor: Processes fine payments [HTTPS/REST, OAuth2, mTLS, Certificate Pinning]
- Loan Management Component -> Notification Dispatcher Component: Dispatches internal domain events [Spring Application Events]
- Notification Dispatcher Component -> Event Bus: Publishes notification-bound events [AMQP / Kafka, mTLS, Application-level Envelope Encryption]
- Circulation Service -> Observability Backend: Exports distributed traces [OpenTelemetry]

## Technology Stack
- Spring Boot Java: Provides a robust foundation for enterprise microservices
- PostgreSQL: Stores transaction history securely within the EU region with AES-256 PII encryption
- Resilience4j: Implements circuit breakers and exponential backoff retry policies for external payment calls
- OpenTelemetry: Mandates distributed tracing across HTTP and AMQP boundaries
- HashiCorp Vault / Cloud-Native Secrets Store: Manages secure runtime secret injection and automated rotation

## Rationale
This architecture enforces strict domain boundaries and EU data residency while maintaining high availability and resilience. Decoupled asynchronous event publishing protects core transaction latency and ensures seamless patron self-service workflows.