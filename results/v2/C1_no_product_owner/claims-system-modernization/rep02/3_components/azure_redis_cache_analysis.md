## Overview
This system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by gradually migrating claim types to a modern hybrid cloud architecture. It maintains uninterrupted legacy processing while providing a web-based adjuster workspace and customer portal.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Customer Portal (Azure Static Web Apps, React)
- Adjuster Workspace (Azure Container Apps, Node.js/React)
- API Gateway (Azure Container Apps)
- Adjuster Backend Service (Java/Spring Boot, Anti-Corruption Layer)
- Azure SQL Database (Azure SQL Database, Spring Data JPA)
- Azure Redis Cache (Premium Tier P1)
- Azure Service Bus (with Dead-Letter Queues)
- Mainframe Integration Adapter (mTLS)
- Azure Key Vault
- Legacy Mainframe (COBOL/DB2)

## Relationships
- Customer Portal -> API Gateway: Submits online claims [HTTPS/REST]
- Adjuster Workspace -> API Gateway: Handles claims and views data [HTTPS/REST]
- API Gateway -> Adjuster Backend Service: Routes application traffic [gRPC/HTTPS]
- Adjuster Backend Service -> Azure SQL Database: Persists modern claim data [JDBC/TLS]
- Adjuster Backend Service -> Azure Redis Cache: Caches session data and materialized claim views [RESP/TLS]
- Adjuster Backend Service -> Mainframe Integration Adapter: Bridges legacy claim operations [mTLS]
- Mainframe Integration Adapter -> Legacy Mainframe: Exchanges batch and sync data [SNA/DB2 Protocols]
- Adjuster Backend Service -> Azure Service Bus: Publishes asynchronous domain events [AMQP]

## Technology Stack
- **Azure Redis Cache (Premium Tier P1):** Provides master-replica high availability, VNet integration, and persistent memory caching to satisfy sub-second latency requirements.
- **Java / Spring Boot:** Powers the Adjuster Backend Service with enterprise maintainability and robust integration libraries.
- **Azure Container Apps:** Hosts microservice containers, simplifying deployment for a cloud-inexperienced team.
- **Azure SQL Database:** Acts as the modern relational store with Spring Data JPA for ACID compliance.
- **Microsoft Entra ID:** Secures single sign-on and RBAC access across all cloud components.

## Rationale
The hybrid architecture isolates expensive mainframe dependencies while introducing a modern, cloud-native tier to meet performance and maintainability goals. This approach enables incremental claim-type migration without exceeding the strict nightly batch window or risking data consistency.