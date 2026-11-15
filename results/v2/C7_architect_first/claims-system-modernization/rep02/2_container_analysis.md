## Overview
[This system modernizes a 30-year-old regional insurer mainframe by gradually migrating claim types to a hybrid cloud platform while ensuring zero data loss and uninterrupted legacy processing.]

## Key Elements
* Customers and Brokers (External Actors)
* Claims Adjusters (External Actors)
* Insurer Active Directory (External System)
* On-Premises COBOL/DB2 Mainframe (External System)
* API Gateway / BFF (Node.js/TypeScript Container)
* Customer Portal and Adjuster Workspace (React Web Apps in Azure Static Web Apps)
* Claims Processing Service (Java Spring Boot Container)
* Integration Bridge (Apache Camel / Azure Integration Services Container)
* Reference Data & Policy Cache (Redis Container)
* Notification Service (Azure Communication Services Container)
* Audit Logging Container (WORM Storage)
* Document & Evidence Management Service (Azure Blob Storage Container)
* Self-Service Dashboard Backend

## Relationships
* Customers/Brokers to API Gateway/BFF via HTTPS/REST
* API Gateway to Insurer Active Directory via OpenID Connect (OIDC) for Single Sign-On
* Adjuster Workspace to Redis Cache via gRPC for sub-2s performance
* Claims Processing Service to Integration Bridge via Azure Service Bus (asynchronous messaging)
* Integration Bridge to On-Premises Mainframe via IPsec VPN, ExpressRoute, and mTLS

## Technology Stack
* Azure West Europe & On-Premises Mainframe: Hybrid cloud provider setup matching regional constraints.
* Azure Container Apps: Container hosting platform with horizontal pod autoscaling for the Claims Processing Service and Integration Bridge.
* Node.js/TypeScript & Java Spring Boot: Core runtime languages for BFF and microservices.
* React: Frontend framework for web applications.
* Apache Camel & Azure Service Bus: Middleware and message brokering to respect strict mainframe constraints.
* Azure Key Vault & Managed Identities: Secure credential management without static secrets.

## Rationale
[This hybrid architecture decouples the modern Azure web layer from the legacy mainframe via an integration bridge, meeting strict performance and consistency mandates. It ensures low risk through incremental claim migration, isolated caching, and a rapid 1-day fallback mechanism.]