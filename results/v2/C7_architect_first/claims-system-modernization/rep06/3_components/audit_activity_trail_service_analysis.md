## Overview
The system modernizes a regional insurer's claims platform using a hybrid cloud architecture to replace a 30-year-old mainframe. The Audit & Activity Trail Service ensures regulatory compliance and secure traceability across all workflows.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Compliance Officers and Support Managers
- Web Portal (React, TypeScript, Azure Static Web Apps)
- Adjuster Workspace
- API Gateway / Router (YARP reverse proxy)
- Claims Core Service (Spring Boot, Java, Azure Container Apps)
- Audit & Activity Trail Service (Dedicated Microservice)
- Azure Cosmos DB (SQL API)
- Azure Service Bus

## Relationships
- Claims Core Service -> Azure Service Bus: Publishes audit events [AMQP]
- Azure Service Bus -> Audit & Activity Trail Service: Insumes audit events asynchronously [AMQP]
- Audit & Activity Trail Service -> Azure Cosmos DB: Persists append-only logs [TLS / Spring Data JPA]
- Compliance Reporting Interface -> Audit & Activity Trail Service: Queries audit trails [REST / HTTPS with Azure AD PIM/MFA]
- Audit & Activity Trail Service -> Azure Data Lake: Streams change feeds for reporting [Encrypted TLS]

## Technology Stack
- Java 17 / Spring Boot: Core runtime for microservices, aligning with team expertise
- Azure Cosmos DB (SQL API): Immutable append-only storage for high-volume compliance logs
- Azure Service Bus: Asynchronous messaging to decouple audit logging from primary transaction paths
- Azure Active Directory (Azure AD) PIM & MFA: Secures read-access governance for compliance officers
- Azure Key Vault: Provides envelope encryption for PII protection within audit payloads

## Rationale
Asynchronous event ingestion via Azure Service Bus prevents compliance logging from blocking critical claim workflows, protecting system performance and sub-2-second screen load targets. Cosmos DB and Azure AD access governance satisfy strict insurance compliance and data privacy mandates without overwhelming a cloud-inexperienced team.