## Overview
The system is a hybrid cloud platform that modernizes a 30-year-old regional insurer mainframe claims system. It incrementally migrates claim types while keeping the legacy system as the system of record.

## Key Elements
- Customer Portal (React SPA)
- Adjuster Workspace (React SPA)
- API Gateway (Azure API Management) with Authentication Validator, Dynamic Route Orchestrator, Rate Limiter & Circuit Breaker, and Claim-Type Feature Flag Evaluator
- Claims Core Container (.NET / Azure Container Apps)
- Integration & ACL Container (Azure Functions)
- Read Model Projector (Azure Functions / .NET)
- Adjuster Read Database (Azure Cosmos DB)
- Message Broker (IBM MQ)
- Azure Active Directory

## Relationships
- Customer Portal -> API Gateway: Routes frontend traffic [HTTPS]
- Adjuster Workspace -> API Gateway: Routes frontend traffic [HTTPS]
- API Gateway -> Azure Active Directory: Validates JWT tokens [OpenID Connect]
- API Gateway -> Claims Core Container: Forwards requests and enforces mTLS [HTTPS / Mutual TLS]
- API Gateway -> Integration & ACL Container: Forwards unmigrated and fallback claim requests [HTTPS / JSON]

## Technology Stack
- Azure API Management: Edge routing, rate limiting, and mTLS enforcement to secure downstream services.
- Azure Container Apps (.NET): Hosts scalable modern claims core processing logic.
- Azure Functions: Executes asynchronous read projections and integration/ACL translation.
- Azure Cosmos DB: Provides low-latency read models for adjuster screens.
- Azure Active Directory: Delivers centralized Single Sign-On and identity management.
- IBM MQ: Handles asynchronous message brokering with the legacy mainframe.

## Rationale
The hybrid architecture protects the fragile legacy mainframe using an API Gateway circuit breaker and rate limiter while enabling incremental claim type migration. It satisfies strict performance and security constraints by isolating modernization changes and leveraging managed Azure cloud services.