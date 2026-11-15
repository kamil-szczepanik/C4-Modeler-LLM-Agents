## Overview
Component-level architecture for the Billing & Claims Microservice within the Clinic Management System. Manages secure invoice generation, insurance claim processing, and real-time payment operations.

## Key Elements
- ClaimsController (.NET ASP.NET Core Web API)
- BillingEngine (.NET Class Library)
- ClaimsProcessor (.NET Class Library)
- ClearinghouseAdapter (.NET HttpClient/WCF)
- PaymentGatewayClient (.NET HttpClient with Polly)
- DataRepository (Entity Framework Core)
- EventPublisher (.NET / Confluent.Kafka)
- BillingAuditInterceptor (EF Core Interceptor)

## Relationships
- ClaimsController -> BillingEngine & ClaimsProcessor: In-memory C# method calls
- ClaimsProcessor -> ClearinghouseAdapter: External integration [HTTPS / SOAP]
- BillingEngine -> PaymentGatewayClient: External integration [HTTPS / REST]
- DataRepository -> BillingAuditInterceptor: Intercepts save operations for HIPAA logging
- EventPublisher -> Apache Kafka: Asynchronous event publishing [CloudEvents]

## Technology Stack
- .NET 8 / ASP.NET Core: High-performance microservice framework
- Entity Framework Core: Database ORM and persistence mapping
- Polly: Resilience and circuit-breaking for external HTTP clients
- Confluent.Kafka: Asynchronous messaging integration
- IHttpClientFactory: Manages HTTP client lifetimes and prevents socket exhaustion

## Rationale
Modular component separation isolates external integration volatility and enforces strict business orchestration rules. Centralized EF Core interceptors and DI scoping guarantee HIPAA compliance, audit traceability, and 99.99% availability.