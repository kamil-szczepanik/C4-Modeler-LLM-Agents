## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare clinics. It provides secure, highly available clinical and financial operations while adhering to strict HIPAA, GDPR, and 10-year data retention mandates.

## Key Elements
* **API Gateway / BFF**: Kong / Node.js
* **Billing & Claims Service**: .NET Core / C# container housing internal components
* **Claims Processor Component**: .NET Core / C# managing adjudication and clearinghouse formatting
* **Payment Integration Component**: .NET Core / C# handling secure tokenization and payment processing
* **Billing API Facade Component**: ASP.NET Web API exposing endpoints and handling event publication
* **Financial Audit & Archive Component**: .NET Core / C# managing immutable, encrypted audit logs
* **Data & Messaging**: PostgreSQL, Apache Kafka, Redis
* **External Systems**: Payment Gateway, Lab & Imaging Systems, Notification Service, External IdP

## Relationships
* **API Gateway / BFF -> Billing API Facade Component**: Routes internal billing requests [gRPC]
* **Billing API Facade Component -> Apache Kafka**: Publishes domain events like `ClaimSubmitted` [TLS / Kafka Protocol]
* **Claims Processor Component -> PostgreSQL**: Reads and writes transactional ledger data [TCP/SQL]
* **Payment Integration Component -> Payment Gateway**: Processes secure financial transactions [HTTPS / REST]
* **Financial Audit & Archive Component -> Apache Kafka**: Consumes domain events for audit logging [TLS]

## Technology Stack
* **.NET Core / C#**: Chosen for the Billing & Claims Service for enterprise-grade performance and type safety.
* **PostgreSQL with EF Core**: Selected for robust transactional ledger integrity and ACID compliance.
* **Apache Kafka**: Deployed for asynchronous, decoupled event-driven communication using TLS.
* **gRPC**: Utilized for low-latency, high-performance internal service-to-service communication.
* **AES-256**: Implemented at rest across storage tiers to satisfy strict healthcare security constraints.

## Rationale
This architecture ensures 99.99% availability via an active-active hybrid design and strict separation of transactional and auditing concerns. The outbox pattern paired with PostgreSQL and Kafka guarantees financial data consistency and durability across regional failovers.