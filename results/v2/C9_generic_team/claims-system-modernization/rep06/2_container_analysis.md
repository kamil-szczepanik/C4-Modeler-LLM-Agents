## Overview
The system is a modern, hybrid insurance claims platform that incrementally replaces a 30-year-old COBOL/DB2 mainframe. It enables online claims submission and adjuster management while maintaining zero data loss and strict legacy interoperability.

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- Web Application (SPA)
- Backend-for-Frontend (BFF)
- Claim Management Core
- Anti-Corruption Layer (ACL)
- Data Synchronization / ETL Service
- Feature Flag / Routing Service
- Message Broker (Azure Service Bus)
- Cache / Read Model Store
- Observability / Monitoring (Azure Application Insights)
- On-Premise COBOL/DB2 Mainframe (System of Record)
- On-Premise Active Directory

## Relationships
- Customers, Brokers, and Adjusters interact with Web Application via HTTPS/REST (SSO via Active Directory)
- Web Application communicates with Backend-for-Frontend (BFF) via HTTPS/REST
- BFF communicates with Claim Management Core and Anti-Corruption Layer (ACL) via HTTPS/REST
- Anti-Corruption Layer (ACL) exchanges data with On-Premise COBOL/DB2 Mainframe via secure mainframe protocols
- Claim Management Core and ACL publish/subscribe events via Azure Service Bus
- Data Synchronization / ETL Service replicates state with On-Premise COBOL/DB2 Mainframe and Cache / Read Model Store

## Technology Stack
- Azure App Service: Hosts cloud containers, reducing operational overhead for cloud-inexperienced teams
- Azure Service Bus: Manages asynchronous messaging to isolate hybrid network latency
- Azure Application Insights: Provides centralized observability across cloud and on-premise boundaries
- HTTPS/REST: Standardizes synchronous application and API communication
- Managed Cloud Databases: Provides reliable persistence with automated point-in-time recovery

## Rationale
This hybrid architecture isolates expensive mainframe dependencies via an Anti-Corruption Layer and asynchronous messaging, ensuring strict zero-data-loss and one-day rollback constraints. Utilizing managed Azure services minimizes operational complexity for a team with limited cloud experience.