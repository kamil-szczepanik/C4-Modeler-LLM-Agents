## Overview
[Gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. Ensures continuous legacy processing while migrating claim types over three years.]

## Key Elements
* Customers, Brokers, Claims Adjusters, Support Agents
* COBOL/DB2 Mainframe System of Record
* Azure Application Gateway / NGINX
* Modern Web Application (React, ASP.NET Core)
* Azure Cache for Redis
* Azure Service Bus
* Azure Kubernetes Service (AKS)
* Azure Key Vault

## Relationships
* Customer/Broker/Adjuster -> Azure Application Gateway: HTTPS/TLS 1.3
* Azure Application Gateway -> Modern Web Application: mTLS / HTTP
* Modern Web Application -> Azure Cache for Redis: TCP / Redis Protocol
* Modern Web Application -> Azure Service Bus: AMQP
* Modern Web Application -> COBOL/DB2 Mainframe: REST / Batch API

## Technology Stack
* React & ASP.NET Core: Frontend and backend for responsive adjuster/customer UI
* Azure Kubernetes Service (AKS): Container orchestration to abstract cloud complexity
* Azure Service Bus: Asynchronous messaging for reliable hybrid integration
* Azure Cache for Redis: Low-latency caching to meet sub-2-second load times
* Terraform: Infrastructure as Code for environment consistency
* Azure Key Vault: Secure management of secrets via Managed Identities

## Rationale
[A hybrid architecture using Azure Kubernetes Service and Azure Service Bus decouples the new frontend from the legacy mainframe while ensuring strict consistency. This design isolates expensive mainframe interactions, satisfies stringent performance and security constraints, and enables incremental claim type migration.]