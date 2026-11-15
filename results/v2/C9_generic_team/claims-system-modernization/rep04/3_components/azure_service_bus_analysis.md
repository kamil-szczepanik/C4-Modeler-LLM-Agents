## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old mainframe. It enables online claim submission and adjuster workflows while maintaining zero data loss and supporting incremental claim migrations.

## Key Elements
- Customers and Brokers: External users submitting claims online
- Claims Adjusters: Internal users managing claims via the web application
- On-Premises COBOL/DB2 Mainframe: Legacy system of record
- Active Directory: Identity provider for Single Sign-On
- Azure Container Apps: Hosts the Backend-for-Frontend (BFF), Modular Monolith, and Anti-Corruption Layer (ACL)
- Azure Service Bus: Asynchronous message broker with topic-per-claim-type routing
- Azure Cosmos DB / Redis: Data persistence and caching layers
- Azure Blob Storage: Storage for large binary claim attachments
- Azure Key Vault: Secrets management

## Relationships
- Customers and Brokers interact with the BFF via HTTPS/TLS for claim submission
- Claims Adjusters interact with the BFF via HTTPS/TLS for claim management
- BFF communicates with the Modular Monolith via gRPC/REST
- Modular Monolith and Anti-Corruption Layer exchange messages via Azure Service Bus using AMQP
- Anti-Corruption Layer communicates with the On-Premises COBOL/DB2 Mainframe via legacy protocols
- Containers authenticate to Azure services using Azure Managed Identities

## Technology Stack
- Azure Service Bus: Chosen for guaranteed at-least-once delivery, competing consumers, and zero data loss
- Azure Container Apps: Selected for hosting modern microservices with minimal cloud operational overhead
- Bicep/Terraform: Used for Infrastructure-as-Code (IaC) to prevent deployment drift
- Azure Blob Storage: Utilized for offloading binary attachments to maintain message broker throughput
- W3C Trace Context: Implemented for distributed tracing and observability across hybrid boundaries
- Polly: Utilized for standardized circuit breaker and retry policies in consumer workers

## Rationale
This hybrid architecture isolates complex legacy mainframe integrations behind an Anti-Corruption Layer while modernizing the claims experience in Azure. It guarantees zero data loss and enables rapid one-day rollbacks per claim type to satisfy strict migration constraints.