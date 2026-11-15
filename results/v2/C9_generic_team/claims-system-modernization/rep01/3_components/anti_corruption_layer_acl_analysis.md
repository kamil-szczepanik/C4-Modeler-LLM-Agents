## Overview
[Hybrid Insurance Claims Modernization Platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern .NET Core web application while maintaining data consistency. The system leverages an Anti-Corruption Layer (ACL) to decouple legacy latency and schema constraints from modern user experiences.]

## Key Elements
* Customers and Brokers
* Claims Adjusters
* Azure Hosted API Gateway
* Claim Ingestion & Validation Module (.NET Core / Modular Monolith)
* Anti-Corruption Layer (ACL) (.NET Core / Modular Monolith)
* Read-Model Cache (Azure Cache / In-Memory Database)
* Data Synchronization Worker (.NET Background Worker)
* Feature Flag Management Module (Azure App Configuration)
* Centralized Observability & Audit Logging Module (Azure Monitor / Application Insights)
* On-Premises COBOL/DB2 Mainframe

## Relationships
* Customers and Brokers -> Azure Hosted API Gateway: Submit claims via HTTPS/REST
* Claims Adjusters -> Azure Hosted API Gateway: Handle claims via HTTPS/REST
* Azure Hosted API Gateway -> Claim Ingestion & Validation Module: Route traffic via Internal Routing
* Claim Ingestion & Validation Module -> Anti-Corruption Layer (ACL): Forward validated claims payloads via Internal Routing
* Anti-Corruption Layer (ACL) -> On-Premises COBOL/DB2 Mainframe: Translate and dispatch claim data via Restricted Legacy Interfaces
* Feature Flag Management Module -> Anti-Corruption Layer (ACL): Dynamically toggle claim-type routing via Azure App Configuration

## Technology Stack
* Microsoft Azure: Cloud provider for scalability and managed services
* .NET Core: Framework for modular monolith and worker components
* Azure Service Bus: Asynchronous messaging between distributed components
* Azure Key Vault: Secure management of secrets and connection strings
* Polly (.NET): Circuit breaker and resilience patterns for legacy integration
* Flyway / Entity Framework: Database migration and schema versioning

## Rationale
[The hybrid architecture isolates expensive, high-latency legacy systems via an Anti-Corruption Layer (ACL) and asynchronous outbox patterns, ensuring zero data loss and sub-2-second adjuster screen loads. This approach empowers a team with limited cloud experience to incrementally migrate claim types and execute rapid rollbacks within one day.]