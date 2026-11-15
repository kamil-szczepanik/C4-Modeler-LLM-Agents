## Overview
This system modernizes a regional insurer's 30-year-old claims mainframe by migrating claim types incrementally to an Azure-hosted platform. It ensures reliable hybrid integration while keeping the legacy system as the primary database of record.

## Key Elements
- Customers and Brokers: External users submitting online claims
- Claims Adjusters: Internal users managing claims via the web application
- On-Premise COBOL/DB2 Mainframe: Legacy system of record
- On-Premise Active Directory: Identity provider for Single Sign-On
- Web Application (SPA) & Backend-for-Frontend (BFF): Modern user interface layer
- Claim Management Core: Business logic container for processed claims
- Anti-Corruption Layer (ACL): Integration bridge translating modern events for the mainframe
- Azure Service Bus: Asynchronous message broker isolating hybrid latency

## Relationships
- Customers/Brokers -> Web Application (SPA): HTTPS / TLS for online claim submission
- Web Application (SPA) -> Backend-for-Frontend (BFF): HTTPS REST / JSON
- Backend-for-Frontend (BFF) -> Claim Management Core: Internal REST / gRPC
- Claim Management Core -> Azure Service Bus: Publishes and subscribes events [AMQP]
- Anti-Corruption Layer (ACL) -> Azure Service Bus: Publishes and subscribes events [AMQP]
- Anti-Corruption Layer (ACL) -> On-Premise COBOL/DB2 Mainframe: Secure Mainframe Protocols

## Technology Stack
- Azure App Service: Hosts containerized microservices (BFF, Core, ACL) for rapid deployment
- Azure Service Bus: Asynchronous message broker with outbox pattern and dead-letter queues to guarantee exactly-once processing (R-04)
- Azure Application Insights: Distributed tracing using Correlation IDs across hybrid boundaries
- Azure Active Directory: Single sign-on authentication enforcing enterprise security (R-07)
- Azure Storage: Implements the Valet Key pattern to offload heavy payloads and preserve broker throughput

## Rationale
The hybrid event-driven architecture decouples modern Azure components from legacy mainframe constraints and latency. This ensures safe incremental migration, strict data consistency, and rapid one-day fallback capabilities per claim type.