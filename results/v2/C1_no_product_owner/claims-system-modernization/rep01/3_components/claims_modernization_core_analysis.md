## Overview
[The system modernizes a regional insurer's 30-year-old mainframe claims platform using a hybrid cloud architecture. It gradually migrates claim types while maintaining uninterrupted legacy processing.]

## Key Elements
- Claims Portal (React on Azure App Service)
- Azure API Management (BFF)
- Claims Modernization Core (Java Spring Boot on Azure Kubernetes Service)
- Claim Ingestion Component (Spring MVC)
- Migration Router Component (Spring Cloud Gateway / custom bean)
- Legacy Mainframe Adapter Component (Spring Integration / SOAP-over-HTTP with Resilience4j)
- Claim Management Component (Spring Data JPA)
- Security Policy Component (RBAC/ABAC)
- Outbox Pattern Component
- Integration & Sync Engine (Azure Service Bus)
- State Store (Azure SQL Database Managed Instance)
- Legacy Mainframe System (COBOL/DB2 on-premise)
- Active Directory / Azure AD

## Relationships
- Claims Portal -> Azure API Management: Forwards user requests [HTTPS]
- Azure API Management -> Claims Modernization Core: Forwards validated requests [HTTPS / OAuth2]
- Claim Ingestion Component -> Migration Router Component: Forwards validated claims [Internal Method Call]
- Migration Router Component -> Claim Management Component: Processes modern claims [Internal Method Call]
- Migration Router Component -> Legacy Mainframe Adapter Component: Routes to legacy [Internal Method Call]
- Claim Management Component -> Outbox Pattern Component: Persists domain events transactionally [Internal Method Call]
- Outbox Pattern Component -> Integration & Sync Engine: Publishes asynchronous messages [AMQP over TLS / Managed Identity]
- Claims Modernization Core -> State Store: Communicates for persistence [TDS over TLS with TDE]
- Legacy Mainframe Adapter Component -> Legacy Mainframe System: SOAP/HTTP communication [SOAP-over-HTTP]

## Technology Stack
- Frontend: React hosted on Azure App Service for responsive adjuster screens
- Core Backend: Java Spring Boot running on Azure Kubernetes Service (AKS) for elastic microservice scalability
- Database: Azure SQL Database Managed Instance for transactional state storage and consistency
- Messaging: Azure Service Bus for asynchronous event-driven integration
- Integration & Resilience: Spring Integration, Resilience4j circuit breakers, and OpenTelemetry for distributed tracing
- Security: Azure AD, OAuth2/OIDC, Azure Key Vault, mTLS via Linkerd/Istio service mesh

## Rationale
[This hybrid architecture decouples the legacy mainframe using a strangler-fig pattern, enabling incremental claim type migrations. It guarantees data consistency and low-latency adjuster experiences while accommodating the team's cloud skill level through managed Azure services.]