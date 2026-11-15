## Overview
The Notification Engine is a lightweight Go-based component of the Library Management System that consumes asynchronous events to dispatch multi-channel patron and staff alerts. It ensures GDPR compliance, high availability, and performance across EU data residency constraints.

## Key Elements
*   **Event Consumer:** Go service using Sarama or amqp091-go for asynchronous message ingestion.
*   **Preference Router:** Evaluates patron communication rules using a local cache.
*   **Preference Cache:** Go Ristretto in-memory store for patron preferences.
*   **Template Engine:** Go `html/template` for localized, PII-safe messaging.
*   **Dispatchers:** Go modules using `sony/gobreaker` circuit breakers for external channels.
*   **Audit & History Logger:** Asynchronous writer for delivery states.
*   **External Gateways:** SMTP (Email), Twilio/SMPP (SMS), and Firebase/APNs (Push).

## Relationships
*   *Event Consumer -> Message Broker*: Consumes asynchronous events [AMQP/Kafka]
*   *Event Consumer -> Preference Router*: Forwards event payloads [Go Channel]
*   *Preference Router -> Preference Cache*: Queries cached patron preferences [In-Memory]
*   *Preference Router -> Template Engine*: Requests compiled, localized messages [In-Memory]
*   *Template Engine -> Dispatchers*: Passes rendered payloads [Go Structs]
*   *Dispatchers -> External Gateways*: Delivers notifications [TLS 1.3 / HTTPS / SMTP]
*   *Dispatchers -> Audit & History Logger*: Reports delivery status [Go Channel]
*   *Audit & History Logger -> Primary Database*: Persists delivery audit logs [SQL/TCP]

## Technology Stack
*   **Go:** Selected for lightweight execution, fast startup, and concurrency primitives.
*   **RabbitMQ/Kafka:** Message broker for decoupled, asynchronous event-driven architecture.
*   **Ristretto:** Local in-memory cache to prevent database bottlenecks during traffic spikes.
*   **TLS 1.3 & Vault:** Secures transit data and manages encrypted third-party credentials.
*   **KEDA & Kubernetes:** Enables horizontal autoscaling driven by consumer lag metrics.

## Rationale
This architecture guarantees low-latency, resilient notification delivery while strictly adhering to EU data residency and GDPR mandates. Local caching, circuit breakers, and asynchronous logging prevent cascading failures and protect database performance during peak operational loads.