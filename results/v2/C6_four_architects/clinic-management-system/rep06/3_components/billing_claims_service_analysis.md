## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMR, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
* Claim Processing Engine (.NET Core / MediatR)
* Invoice & Ledger API Controller (.NET Core ASP.NET Web API)
* Insurance Gateway Adapter (.NET Core HttpClient / Polly)
* Billing Data Repository (Entity Framework Core)
* Event Dispatcher Worker (.NET Core BackgroundService)
* Billing Audit Interceptor (EF Core SaveChangesInterceptor)
* Claim Event Consumer (.NET Core BackgroundService / MassTransit)
* Billing Local Cache Manager (StackExchange.Redis)
* PHI Masking & Tokenization Engine (.NET Core Middleware)
* Health & Circuit Breaker Health Check Endpoint (.NET Core HealthChecks)

## Relationships
* Invoice & Ledger API Controller -> External Clients: Handles synchronous billing requests and payment status queries [HTTPS]
* Insurance Gateway Adapter -> Insurance Payment Gateway: Processes insurance claims and payments [External HTTPS]
* Billing Data Repository -> Patient DB: Interfaces with PostgreSQL using connection pooling [SQL/TCP]
* Event Dispatcher Worker & Claim Event Consumer -> Async Message Broker: Publishes and consumes domain events [AMQP/TCP]
* Billing Audit Interceptor -> Audit & Compliance Log Shipper: Forwards immutable audit logs asynchronously [Fluentbit/Vector]
* Billing Local Cache Manager -> Distributed Cache: Temporarily stores tariff schedules and rules [Redis Protocol]

## Technology Stack
* .NET Core / ASP.NET Web API: Core runtime and framework for robust, high-performance microservices
* Entity Framework Core: ORM for type-safe database interactions with PostgreSQL
* MassTransit & RabbitMQ/Kafka: Messaging abstraction for reliable event-driven choreography
* Polly: Resilience library for transient fault handling and retries
* StackExchange.Redis: Distributed caching for low-latency tariff schedule lookups
* Kubernetes: Container orchestration ensuring active-active 99.99% uptime

## Rationale
This architecture uses a resilient, event-driven .NET Core design to meet strict HIPAA/GDPR compliance and 10-year data retention mandates. Active-active Kubernetes deployment with Polly and Redis ensures 99.99% availability and high performance.