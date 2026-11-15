## Overview
The Modern Claims Platform gradually replaces a 30-year-old mainframe claims system via a hybrid architecture while legacy processing continues. It ensures seamless incremental migration of claim types without service disruption over a 3-year period.

## Key Elements
* Web Frontend
* API Gateway / Backend-for-Frontend (BFF)
* Core Claims Service
* Data Sync Engine
* Azure SQL Database
* Legacy Mainframe System
* Enterprise Identity Provider

## Relationships
* Web Frontend -> API Gateway / Backend-for-Frontend (BFF): HTTPS/TLS (REST/GraphQL)
* API Gateway / Backend-for-Frontend (BFF) -> Core Claims Service: gRPC/HTTP2 over mTLS
* Core Claims Service -> Azure SQL Database: TDS with encryption
* Modern Claims Platform -> Enterprise Identity Provider: OpenID Connect (OIDC)
* Modern Claims Platform -> Legacy Mainframe System: Encrypted TCP/MQ with mTLS via Enterprise Service Bus

## Technology Stack
* Azure Static Web Apps (React/TypeScript): Provides a responsive interface for users.
* Azure Container Apps (Node.js/Go): Hosts the BFF container to handle routing, caching, and token translation.
* Azure Container Apps (Java/Spring Boot or .NET): Powers the Core Claims Service domain logic.
* Azure SQL Database: Acts as the cloud system of record utilizing Transparent Data Encryption (TDE).
* Azure Service Bus & Azure Functions: Powers the Data Sync Engine for reliable messaging.

## Rationale
The hybrid architecture protects expensive mainframe integration points while safely migrating claim types incrementally. Containerized microservices on Azure provide the scalability required to meet performance goals despite legacy latency constraints.