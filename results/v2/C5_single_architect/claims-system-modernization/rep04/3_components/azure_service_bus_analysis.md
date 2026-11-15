## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe with an Azure-based cloud system. It maintains hybrid operations for up to three years while ensuring zero data loss and seamless fallback capabilities.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Azure Static Web Apps (React Web App)
- Azure Container Apps (.NET Core API Gateway, Migration Router, Mainframe Integration Adapter)
- Azure Service Bus (Claim Submission Topic, Mainframe Relay Queues, Dead-Letter Subsystems, Routing Filter Rules)
- Azure SQL Managed Instance
- Legacy Mainframe (COBOL/DB2)
- Azure Active Directory

## Relationships
- Customers & Brokers -> Azure Static Web Apps: Submits claims via HTTPS
- Claims Adjusters -> Azure Static Web Apps: Manages claims via HTTPS
- Migration Router -> Azure Service Bus (Claim Submission Topic): Publishes events via AMQP/TLS
- Azure Service Bus -> Mainframe Integration Adapter: Forwards messages via AMQP/HTTPS
- Mainframe Integration Adapter -> Legacy Mainframe: Syncs data via TCP/IP

## Technology Stack
- Azure Service Bus: Chosen for native Sessions, Duplicate Detection, and Dead-Lettering to meet zero data loss requirements (R-04) with minimal custom code.
- Azure Container Apps & .NET Core: Provides scalable, microservices-ready hosting for integration layers.
- Azure SQL Managed Instance: Acts as the primary modern data store for migrated claim types.
- Azure Active Directory: Enables centralized Single Sign-On (R-07).

## Rationale
This hybrid architecture decouples modern cloud workflows from the rigid legacy mainframe using robust messaging patterns. It isolates expensive mainframe dependencies while empowering incremental claim type migration and rapid fallback mechanisms.