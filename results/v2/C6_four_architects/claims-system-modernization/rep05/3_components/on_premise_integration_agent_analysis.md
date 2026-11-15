## Overview
Hybrid modernization platform gradually replacing a legacy mainframe insurance claims system. Enables cloud-native claim processing while maintaining legacy system of record integrity.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Azure API Management
- React Claims Web App
- Java Spring Boot Claims Core Service
- Azure Functions Anti-Corruption Layer
- Azure SQL Database & Azure Cache for Redis
- Azure Service Bus
- On-Premise Integration Agent (Inbound Listener, Mainframe Protocol Adapter, Outbound Poller, Circuit Breaker & Retry Manager, Local State Store, Health & Telemetry Monitor)
- Legacy COBOL/DB2 Mainframe
- Active Directory

## Relationships
- Customers & Brokers -> Azure API Management: Online claim submission [HTTPS over TLS]
- Claims Adjusters -> Claims Web App: Adjuster workflows [HTTPS over TLS]
- Claims Web App -> Claims Core Service: REST API [HTTPS over TLS]
- Claims Core Service -> Azure SQL Database: Relational persistence [T-SQL over TLS]
- Claims Core Service -> Azure Service Bus: Asynchronous messaging [AMQP over TLS]
- Azure Service Bus -> On-Premise Integration Agent: Hybrid messaging [AMQP/HTTPS over TLS]
- On-Premise Integration Agent -> Legacy Mainframe: Legacy transactions & queries [CICS/DB2 connectors, TCP/IP over SSL]

## Technology Stack
- Frontend: React hosted on Azure Static Web Apps
- Backend Services: Java / Spring Boot on Azure App Service
- Database: Azure SQL Database & Azure Cache for Redis
- Messaging: Azure Service Bus
- Integration Agent: Apache Camel, Resilience4j, H2 Database, Micrometer (Java)
- Identity: Active Directory SSO

## Rationale
Decouples modern cloud workloads from the legacy mainframe via an anti-corruption layer and hybrid integration agent. Guarantees zero data loss and fault-tolerant communication during incremental migration.