## Overview
[The hybrid system gradually replaces a legacy 30-year-old mainframe claims platform with a modern cloud-native modular monolith while maintaining continuous operations. It enables online claims submission and adjuster management while ensuring zero data loss and seamless legacy fallback.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- COBOL/DB2 Mainframe (System of Record)
- API Gateway Container (Azure Container Apps / API Management)
- Customer BFF Container (Azure App Service / Container Apps)
- Adjuster BFF Container (Azure App Service / Container Apps)
- Modular Monolith Container (Azure App Service / Container Apps)
- Anti-Corruption Layer (ACL) Container (Azure Container Apps)
- Routing / Feature Flag Container (Container Apps)
- Data Sync / Reconciliation Container (Azure Container Apps)
- Asynchronous Messaging & Caching Layer (Azure Service Bus and Redis)
- IAM Proxy / Token Exchange Container (Container Apps)
- Observability & Logging Container (Azure Application Insights)
- Configuration & Secrets Management Container (Azure Key Vault)

## Relationships
- Customers and Brokers -> API Gateway Container: Submits claims [HTTPS/REST]
- Claims Adjusters -> API Gateway Container: Manages claims [HTTPS/REST]
- API Gateway Container -> Customer BFF Container: Routes customer traffic [HTTP/REST]
- API Gateway Container -> Adjuster BFF Container: Routes adjuster traffic [HTTP/REST]
- Routing / Feature Flag Container -> Modular Monolith Container: Forwards routed traffic [Internal REST/gRPC]
- Modular Monolith Container -> Anti-Corruption Layer (ACL) Container: Communicates with legacy system [Internal REST/gRPC]
- Anti-Corruption Layer (ACL) Container -> COBOL/DB2 Mainframe: Synchronizes legacy claims [SNA / IBM MQ / Batch]
- Modular Monolith Container -> Asynchronous Messaging & Caching Layer: Utilizes for async processing and caching [AMQP and Redis Protocol]
- Observability & Logging Container -> Modular Monolith Container: Collects telemetry [Telemetry SDK]

## Technology Stack
- Azure App Service / Container Apps: Hosts modern micro-containers with low initial cloud operational overhead.
- Azure Service Bus & Redis: Provides reliable async messaging and low-latency read caching to bypass mainframe latency.
- Hexagonal / Clean Architecture: Isolates domain logic from infrastructure to facilitate future service extraction.
- NetArchTest / ArchUnit: Enforces strict internal module boundaries and dependency rules automatically via CI/CD.
- Azure App Configuration & Key Vault: Manages centralized feature flags and secrets to support one-day rollbacks.

## Rationale
[A modular monolith architecture reduces distributed systems complexity for a team with limited cloud experience while maintaining strict internal boundaries for future extraction. Hybrid integration patterns, outbox/inbox mechanisms, and feature flags guarantee regulatory consistency, sub-2-second UI responses, and rapid legacy rollback capabilities.]