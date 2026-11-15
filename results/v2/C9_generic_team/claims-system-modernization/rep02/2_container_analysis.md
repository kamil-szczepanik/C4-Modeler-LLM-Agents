## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It maintains legacy operations while enabling modern online claim submissions and adjuster workflows.

## Key Elements
* **Users**: Customers, Brokers, Claims Adjusters
* **External Systems**: On-premises COBOL/DB2 Mainframe, Corporate Active Directory
* **Containers**: API Gateway / Anti-Corruption Layer (ACL), Event Broker, Caching / State Store, Data Synchronization / Reconciliation, Backend-for-Frontend (BFF), Centralized Logging & Monitoring, IAM / Token Service, Configuration & Secret Management, Worker / Background Processing

## Relationships
* **Customers & Brokers** -> **API Gateway / ACL**: HTTPS / REST for online claim submissions
* **Claims Adjusters** -> **BFF**: HTTPS / REST for the adjuster web application
* **BFF & Services** -> **API Gateway / ACL**: HTTPS / gRPC for internal orchestration and data retrieval
* **API Gateway / ACL** -> **COBOL/DB2 Mainframe**: Batch / Legacy protocols for system of record updates
* **Services** -> **Event Broker**: AMQP / MQTT for asynchronous event-driven claim-type migration
* **Services** -> **Caching / State Store**: TCP / Redis Protocol for low-latency read models
* **IAM / Token Service** -> **Active Directory**: OIDC / SAML for Single Sign-On authentication

## Technology Stack
* **Cloud Provider**: Microsoft Azure (West Europe region) with hybrid on-premises connectivity
* **API Gateway / ACL**: Custom microservices to decouple modern Azure components from rigid mainframe contracts
* **Event Broker**: Azure Service Bus for reliable asynchronous messaging and strangler migration support
* **Caching Layer**: Azure Redis Cache to meet sub-2-second UI performance targets despite slow mainframe latency
* **Identity & Access Management**: Azure Identity services integrated with corporate Active Directory for SSO
* **Configuration & Secret Management**: Azure Key Vault and App Configuration for secure credential and feature-flag handling
* **Background Processing**: Azure Functions / WebJobs for asynchronous reconciliation and event consumption

## Rationale
This hybrid architecture isolates the legacy COBOL/DB2 mainframe while introducing modern Azure containers to meet strict performance and consistency constraints. Dedicated caching, BFF, and ACL layers decouple UI responsiveness from slow mainframe responses, ensuring seamless incremental migration.