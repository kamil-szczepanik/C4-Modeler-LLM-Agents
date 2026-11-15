## Overview
[The system modernizes a regional insurer's claims platform via a hybrid architecture, gradually replacing the legacy mainframe while ensuring continuous processing.]

## Key Elements
- Azure API Management
- Claims Processing Service (Java, Spring Boot, Azure Container Apps)
- Azure SQL Database
- Azure Service Bus
- Azure Key Vault
- Azure Active Directory (Entra ID)
- Azure Application Insights

## Relationships
- Azure API Management -> Claims Processing Service: Dynamic claim-type routing [HTTPS / VNet]
- Claims Processing Service -> Azure SQL Database: ACID-compliant transaction persistence and outbox pattern [TDS]
- Claims Processing Service -> Azure Service Bus: Asynchronous event publishing [AMQP]
- Claims Processing Service -> Azure Key Vault: Secret and credential retrieval [HTTPS / Managed Identity]

## Technology Stack
- Azure Container Apps: Chosen for simple container orchestration suited to low cloud experience teams.
- Spring Boot: Selected for opinionated microservice boilerplate and robust ecosystem integration.
- Azure SQL Database: Provides reliable relational persistence with local outbox table support for R-04.
- Resilience4j: Implements circuit breakers and caching adapters to mitigate mainframe latency (R-05).
- Azure Active Directory: Enforces OAuth 2.0 / OpenID Connect Single Sign-On (R-07).

## Rationale
[The hybrid architecture decouples frontend clients from the legacy mainframe via API Management, enabling seamless, gradual claim-type migration within 3 years. Utilizing managed Azure services and standard enterprise patterns (Outbox, Circuit Breaker) minimizes operational risk for a team with limited cloud experience.]