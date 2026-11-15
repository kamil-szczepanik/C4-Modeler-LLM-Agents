## Overview
The Insurance Claims Modernization platform gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud architecture. It ensures zero data loss, sub-second adjuster performance, and rapid one-day rollbacks for migrated claim types.

## Key Elements
- Users: Customer, Broker, Claims Adjuster
- External Systems: Active Directory, Core Rating & Underwriting Engine, Payment Gateway, Notification Service, Legacy Mainframe
- Containers: Web Portal, Adjuster Web Application, API Gateway / BFF, Claims Management App, Claim Routing Service, Integration & Sync Service, Claims Database, Notification & Document Store, Mainframe Data Ingestion Worker, Observability & Audit Container
- Database Components: Claims Core Schema, Migration & Sync Staging Schema, Audit & History Table Store, Data Access Security & Abstraction Layer, Change Data Capture (CDC) & Index Management Engine, Database Migration & Versioning Controller

## Relationships
- Customer/Broker -> Web Portal: Submits claims [HTTPS / TLS 1.3]
- Adjuster Web Application -> API Gateway / BFF: Manages claims [HTTPS / REST]
- Claims Management App -> Claims Database: Reads/writes data [Entity Framework Core / TDS]
- Integration & Sync Service <-> Claims Database: Synchronizes state and reads change streams [TDS]
- Claims Database -> Observability & Audit Container: Sends telemetry [OpenTelemetry / HTTPS]

## Technology Stack
- Frontend: React / TypeScript on Azure Static Web Apps for responsive adjuster and customer portals
- Compute: Azure Container Apps, Azure Functions, and Node.js for scalable microservices and ingestion workers
- Database: Azure SQL Database with Transparent Data Encryption (TDE), CDC, and System-Versioned Temporal Tables for secure, consistent, and auditable storage
- Integration: Azure Service Bus and Azure Data Factory for reliable asynchronous messaging and hybrid mainframe synchronization

## Rationale
The hybrid architecture maintains the legacy mainframe as the system of record while incrementally migrating claim types using a strangler fig pattern. Azure SQL Database features (CDC, Temporal Tables, RLS) ensure strict transactional consistency, sub-second response times, and rapid rollback capabilities.