## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure platform. The Feature/Routing Service manages dynamic, zero-downtime routing of claim types between the modern platform and the legacy mainframe.

## Key Elements
- **Routing Controller**: REST API entry point handling inbound API Gateway requests, JSON schema validation, and audit logging.
- **Feature Toggle Engine**: In-memory cache evaluating claim types against migration flags.
- **Routing Dispatcher**: Forwards requests using Polly policies and circuit breakers.
- **Audit Logger Component**: Middleware emitting routing decisions to Azure Monitor.
- **Azure App Configuration**: Stores migration flags using Managed Identity sync.
- **Claims Core Services & Integration/ACL Worker**: Downstream processing targets.

## Relationships
- **Claims API Gateway -> Routing Controller**: Routes API requests [HTTPS / JSON, TLS 1.3, JWT]
- **Routing Controller -> Feature Toggle Engine**: Checks claim status [In-Process]
- **Feature Toggle Engine -> Azure App Configuration**: Syncs migration flags [HTTPS, Managed Identity]
- **Routing Dispatcher -> Claims Core Services**: Forwards modern claims [HTTPS / JSON, mTLS]
- **Routing Dispatcher -> Integration / Anti-Corruption Layer (ACA Worker)**: Forwards legacy claims [HTTPS / JSON, mTLS]
- **Routing Controller -> Audit Logger Component**: Emits routing decisions [In-Process]

## Technology Stack
- **.NET 8 / C#**: Chosen for containerized microservices running in Azure Container Apps due to team familiarity and robust ecosystem.
- **Azure Container Apps**: Provides simple serverless container management with built-in revision management, traffic splitting, and mTLS.
- **Azure App Configuration**: Enables dynamic feature toggling without application redeployments.
- **Polly**: Provides resilient circuit breaking and automatic fail-safe routing to the legacy mainframe.
- **Bicep**: Used for Infrastructure as Code to automate deployments and prevent configuration drift.

## Rationale
This architecture ensures zero-downtime incremental migration and a one-day rollback capability per claim type while keeping the system of record intact. It incorporates secure, fault-tolerant routing with automated fail-safes to protect business continuity and prevent lost claims during the hybrid transition.