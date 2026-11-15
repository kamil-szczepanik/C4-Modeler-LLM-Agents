## Overview
The system is a hybrid cloud insurance claims modernization platform that incrementally replaces a legacy COBOL/DB2 mainframe while preserving core system-of-record operations. It securely routes customer submissions and adjuster workflows through Azure while managing legacy integration constraints.

## Key Elements
- **Users**: Customer / Broker, Claims Adjuster
- **External Systems**: Active Directory / Azure AD, Mainframe COBOL/DB2 System
- **Containers**: Web Application Container (React/Node.js on Azure App Service), API Gateway / Integration Container (Azure API Management), Claims Core Service Container (Java/Spring Boot on Azure Container Apps), Data & Caching Container (Azure Cosmos DB + Redis), Mainframe Adapter Container (Azure Service Bus with Dead Letter Queues)
- **Mainframe Adapter Components**: Inbound Message Router, Batch Window Gatekeeper, Mainframe Connector Client, DLQ Management Service, Audit & Compliance Interceptor, DLQ Notification Publisher

## Relationships
- Customer / Broker -> Web Application Container [HTTPS / TLS 1.3]
- Claims Adjuster -> Web Application Container [HTTPS / Single Sign-On via Active Directory]
- Web Application Container -> API Gateway / Integration Container [HTTPS / REST]
- API Gateway -> Claims Core Service Container [gRPC / Internal Network]
- Claims Core Service Container -> Mainframe Adapter Container [AMQP / Azure Service Bus]
- Mainframe Adapter Container -> Mainframe COBOL/DB2 System [IBM MQ / TCP/IP over Azure ExpressRoute]

## Technology Stack
- **Cloud Platform**: Microsoft Azure (West Europe) and On-Premise Hybrid
- **Compute**: Azure App Service, Azure Container Apps (Java / Spring Boot)
- **Messaging & Integration**: Azure Service Bus, IBM MQ
- **Data & Storage**: Azure Cosmos DB, Redis, Azure Blob Storage, Azure Key Vault
- **Observability**: Azure Application Insights, OpenTelemetry, Prometheus

## Rationale
This hybrid architecture isolates brittle legacy mainframe interfaces behind an asynchronous messaging adapter, guaranteeing system consistency and quick rollback capabilities. The chosen technology stack leverages managed Azure services to minimize operational complexity for a cloud-novice team while meeting strict performance and security constraints.