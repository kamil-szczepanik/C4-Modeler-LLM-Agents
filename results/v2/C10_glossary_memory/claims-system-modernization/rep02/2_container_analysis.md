## Overview
[The system is a modern cloud platform that gradually replaces a legacy mainframe claims system through a hybrid architecture. Its core purpose is to enable incremental claim type migration while ensuring zero data loss and maintaining business continuity.]

## Key Elements
* Web Frontend
* API Gateway / Backend-for-Frontend (BFF)
* Core Claims Service
* Data Sync Engine
* Azure SQL Database
* Enterprise Identity Provider
* Legacy Mainframe System

## Relationships
* Web Frontend -> API Gateway / Backend-for-Frontend (BFF): HTTPS/TLS (REST/GraphQL)
* API Gateway / Backend-for-Frontend (BFF) -> Core Claims Service: HTTPS/TLS (gRPC/REST)
* Core Claims Service -> Azure SQL Database: TDS (Tabular Data Stream) with encryption
* Data Sync Engine <-> Legacy Mainframe System: Encrypted TCP/MQ with mTLS via Enterprise Service Bus
* Web Frontend -> Enterprise Identity Provider: OpenID Connect (OIDC)

## Technology Stack
* React/TypeScript on Azure Static Web Apps: Serves adjusters and customers with a responsive interface
* Azure Container Apps (Node.js/Go): Implements API Gateway/BFF for caching and async orchestration
* Azure Container Apps (Java/Spring Boot or .NET): Hosts Core Claims Service domain logic
* Azure Service Bus & Azure Functions: Powers Data Sync Engine for reliable messaging
* Azure SQL Database: Acts as cloud system of record with Transparent Data Encryption (TDE)

## Rationale
[This hybrid architecture decouples modern web clients from legacy mainframe latency to meet strict performance targets. Managed cloud services reduce operational burden for a team with limited cloud experience while ensuring reliable data synchronization.]