## Overview
[The Insurance Claims Modernization Platform gradually replaces a 30-year-old COBOL/DB2 mainframe system with a modern cloud-native hybrid architecture to support incremental claim type migration while maintaining zero claim loss.]

## Key Elements
• Claims Portal (React on Azure App Service)
• Azure API Management (BFF)
• Claims Modernization Core (Java Spring Boot on Azure Kubernetes Service)
• Integration & Sync Engine (Azure Service Bus)
• State Store (Azure SQL Database Managed Identity)
• Sync Orchestrator (Apache Camel on Azure Kubernetes Service)
• Mainframe Adapter (Apache Camel + IBM MQ Client on Azure Kubernetes Service)
• Reconciliation Worker (Python on Azure Functions)
• Legacy Mainframe System (COBOL/DB2 on-premise)
• Active Directory (Identity Provider)

## Relationships
• Claims Portal -> Azure API Management: HTTPS/REST with JWT authentication
• Azure API Management -> Claims Modernization Core: HTTPS/gRPC
• Claims Modernization Core -> Integration & Sync Engine: AMQP over Azure Service Bus with OpenTelemetry headers
• Sync Orchestrator -> Mainframe Adapter: gRPC/HTTP/2 over mTLS within Azure Kubernetes Service
• Mainframe Adapter -> Legacy Mainframe System: IBM MQ over IPsec VPN/ExpressRoute with mTLS
• Reconciliation Worker -> State Store: T-SQL via Azure Managed Identity over TLS 1.3

## Technology Stack
• Azure Kubernetes Service: Hosts modern containerized microservices and integration runtimes
• Apache Camel: Provides enterprise integration patterns and message routing
• Azure Service Bus: Manages asynchronous messaging, pub/sub, and backpressure queuing
• Azure SQL Database Managed Identity: Stores transaction state securely with Transparent Data Encryption
• Azure Functions: Executes serverless nightly data reconciliation scripts

## Rationale
[This hybrid architecture decouples modern cloud services from legacy batch constraints using resilient message queuing and integration adapters. It ensures strict data consistency and seamless incremental migration without risking core business operations.]