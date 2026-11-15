## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe while maintaining continuous legacy processing. It provides modern cloud capabilities for customers, brokers, and adjusters while ensuring zero data loss and strict SLA compliance during the 3-year migration.

## Key Elements
- **Customers and Brokers**: External users submitting claims online.
- **Claim Adjusters**: Internal users managing claims via the new web application.
- **Compliance & Audit Officers**: Internal users accessing read-only audit trails.
- **New Claims Platform**: Modern cloud-native microservices hosted in Azure West Europe using Azure Container Apps.
- **Legacy Mainframe**: On-premise 30-year-old COBOL/DB2 system acting as the system of record.
- **Azure Service Bus**: Managed message broker in Azure acting as a decoupled integration buffer.
- **Active Directory**: On-premise enterprise identity provider.

## Relationships
- Customers, Brokers, Claim Adjusters, and Compliance Officers -> New Claims Platform: HTTPS (Web/Mobile UI)
- New Claims Platform -> Azure Service Bus: AMQP / HTTPS for asynchronous claims synchronization
- New Claims Platform <-> Legacy Mainframe: Asynchronous messaging / ETL via Azure Service Bus, constrained by a maximum of one interface change per quarter
- New Claims Platform -> Active Directory: OAuth2 / OpenID Connect via Azure AD Connect with Hybrid Conditional Access

## Technology Stack
- **Azure Container Apps**: Container hosting to mitigate low cloud maturity risks compared to raw Kubernetes.
- **Azure Service Bus**: Enterprise integration bus providing dead-letter queues and circuit breakers for hybrid messaging.
- **Anti-Corruption Layer (ACL)**: Architectural pattern for data sanitization, schema transformation, and enabling the one-day switch-back requirement.
- **Azure Application Insights**: Distributed tracing tool for diagnosing hybrid latency bottlenecks.
- **WORM Storage Policies**: Immutable storage sinks in Azure for compliance audit trails.

## Rationale
The hybrid Azure and on-premise architecture isolates expensive mainframe dependencies while delivering sub-2-second web application performance. Managed cloud services and an Anti-Corruption Layer minimize operational complexity for an inexperienced cloud team while strictly fulfilling migration, security, and zero-data-loss constraints.