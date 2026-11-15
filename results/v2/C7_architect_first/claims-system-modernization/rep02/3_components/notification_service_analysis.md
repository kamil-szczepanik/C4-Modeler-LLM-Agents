## Overview
[A modern hybrid cloud Notification Service extracts claim events via Azure Service Bus to deliver multi-channel, secure updates to customers and brokers.]

## Key Elements
* Notification Router Component (Java/Spring Boot)
* Preference Resolution Component (Java/Spring Boot backed by Redis)
* Template Engine Component (Java)
* Azure Communication Adapter Component (Azure SDK for Java)
* Delivery Status Tracker Component (Cosmos DB)

## Relationships
* Claims Processing Service -> Notification Router (AMQP via Azure Service Bus)
* Notification Router -> Preference Resolution Component (REST/gRPC with Redis cache)
* Template Engine -> Azure Communication Adapter (Spring Application Events)
* Azure Communication Adapter -> Azure Communication Services (HTTPS / TLS 1.3)

## Technology Stack
* Java / Spring Boot: Aligns with existing claims services to minimize technology sprawl
* Azure Service Bus: Provides reliable asynchronous message queuing and DLQ alerting
* Azure Communication Services: Delivers native multi-channel cloud notifications
* Cosmos DB: Tracks message delivery states asynchronously with CMK encryption
* Redis: Caches user notification preferences to prevent latency bottlenecks

## Rationale
[This modular, resilient architecture ensures secure, compliant multi-channel communication while supporting gradual claim migration without extending batch windows.]