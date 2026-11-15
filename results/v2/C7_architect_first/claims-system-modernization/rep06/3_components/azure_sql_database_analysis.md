## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old mainframe with a modern web application while ensuring uninterrupted legacy processing.]

## Key Elements
*   [Web Portal (SPA): React, TypeScript, Azure Static Web Apps]
*   [Adjuster Workspace: Web Application for claims adjusters]
*   [API Gateway / Router: YARP reverse proxy]
*   [Claims Core Service: Spring Boot, Java, Azure Container Apps]
*   [Integration & Sync Engine: Apache Kafka, Azure Service Bus]
*   [Azure SQL Database: Azure SQL Database, Azure Managed Identity, TDE]
*   [Audit & Activity Trail Service: Dedicated Microservice]

## Relationships
*   [Customers and Brokers -> Web Portal (SPA): Submits claims via HTTPS]
*   [Claims Adjusters -> Adjuster Workspace: Manages claims via HTTPS]
*   [Web Portal & Adjuster Workspace -> API Gateway / Router: Routes traffic via HTTPS / REST]
*   [API Gateway / Router -> Claims Core Service: Forwards requests via HTTP/gRPC]
*   [Claims Core Service -> Azure SQL Database: Reads/writes claim aggregates via JDBC/TDS (Port 1433) over Azure Private Endpoint]
*   [Claims Core Service <-> Legacy Mainframe: Synchronizes data via Apache Kafka and Azure Service Bus]

## Technology Stack
*   [Azure SQL Database (Serverless tier): Minimizes cloud experience overhead while providing strong consistency and auto-scaling]
*   [Azure AD Managed Identity: Enforces passwordless authentication and eliminates embedded credentials]
*   [Azure Private Endpoint: Secures database network isolation by disabling public internet access]
*   [Always Encrypted with Secure Enclaves: Protects sensitive PII at rest and in transit]

## Rationale
[This hybrid architecture satisfies strict consistency and zero-data-loss constraints (R-04) while mitigating the team's low cloud experience through managed services. It enables incremental claim type migration (R-03) and rapid one-day rollbacks (R-06) without impacting the legacy mainframe.]