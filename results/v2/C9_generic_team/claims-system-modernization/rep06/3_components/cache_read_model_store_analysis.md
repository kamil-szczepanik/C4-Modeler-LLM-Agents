## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud platform. The architecture ensures continuous claims processing, data consistency, and rapid iterative migration.

## Key Elements
- Customers and Brokers (External Users)
- Claims Adjusters (Internal Users)
- On-Premise COBOL/DB2 Mainframe (System of Record)
- On-Premise Active Directory (Identity Provider)
- Web Application (SPA) (Azure App Service)
- Backend-for-Fronend (BFF) (Azure App Service)
- Claim Management Core (Azure App Service)
- Anti-Corruption Layer (ACL) (Azure App Service)
- Data Synchronization / ETL Service (Azure Service)
- Feature Flag / Routing Service (Azure App Service)
- Message Broker (Azure Service Bus)
- Cache / Read Model Store (Managed Cloud Database / Cache)
- Observability / Monitoring (Azure Application Insights)

## Relationships
- Customers and Brokers -> Web Application (SPA) [HTTPS]
- Claims Adjusters -> Web Application (SPA) [HTTPS]
- Web Application (SPA) -> Backend-for-Frontend (BFF) [HTTPS/REST]
- Backend-for-Frontend (BFF) -> Claim Management Core [HTTPS/gRPC]
- Claim Management Core -> Message Broker (Azure Service Bus) [AMQP]
- Claim Management Core -> Anti-Corruption Layer (ACL) [HTTPS/REST]
- Anti-Corruption Layer (ACL) -> On-Premise COBOL/DB2 Mainframe [Secure Mainframe Protocols]
- Data Synchronization / ETL Service -> Cache / Read Model Store [Database Replication]
- Backend-for-Frontend (BFF) -> Cache / Read Model Store [TCP/Redis Protocol]
- All Services -> Observability / Monitoring (Azure Application Insights) [Telemetry SDK]

## Technology Stack
- Azure App Service: Hosts containerized microservices due to managed simplicity for teams with limited cloud experience.
- Azure Service Bus: Asynchronous message broker ensuring reliable event delivery and decoupling during hybrid operations.
- Azure Application Insights: Provides real-time performance telemetry to guarantee sub-2-second UI load times.
- Managed Cloud Database / Cache: Delivers fast read performance for adjuster screens and decouples read models from mainframe latency.
- Azure Active Directory: Centralized identity provider enforcing secure Single Sign-On (SSO).

## Rationale
The hybrid architecture isolates the expensive, legacy mainframe via an Anti-Corruption Layer while modernizing user interfaces on Azure. Strict CQRS, event-driven synchronization, and caching meet strict performance, consistency, and rapid rollback requirements.