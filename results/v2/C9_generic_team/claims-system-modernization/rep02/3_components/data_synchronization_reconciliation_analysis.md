## Overview
The system modernizes a 30-year-old regional insurer mainframe by gradually migrating claims to a hybrid cloud platform while maintaining the legacy COBOL/DB2 system as the system of record. It ensures zero data loss, strict consistency, and seamless 1-day rollbacks during the 3-year migration window.

## Key Elements
- Azure Functions / WebJobs (Data Synchronization and Reconciliation container)
- Azure Service Bus (Event Broker)
- Azure Redis Cache (Caching and State Store)
- Azure Blob Storage (Claim Check payload repository)
- Azure App Configuration and Key Vault (Configuration and Secrets)
- On-Premises COBOL/DB2 Mainframe (System of Record)

## Relationships
- Azure Functions synchronizes data with On-Premises COBOL/DB2 Mainframe via secure extraction files using the Adapter Pattern
- Azure Functions reads and writes state and cache data in Azure Redis Cache using the Idempotent Upsert Pattern
- Azure Functions offloads heavy payloads to Azure Blob Storage using the Claim Check Pattern
- Azure Service Bus routes asynchronous synchronization events and Dead Letter Queue messages

## Technology Stack
- Azure Functions & WebJobs: Serverless execution for reconciliation and background processing, chosen for operational simplicity.
- Azure Service Bus: Managed event broker providing reliable messaging, Dead Letter Queues, and isolation.
- Azure Redis Cache: Low-latency caching layer to store claim state and checksums for rapid comparison.
- Azure App Configuration: Externalized JSON/YAML mapping schemas to support configuration-driven field transformations without code deployments.

## Rationale
This architecture decouples the modern cloud platform from strict mainframe constraints using asynchronous reconciliation and isolation patterns. It accommodates the team's limited cloud experience while guaranteeing zero data loss, low-latency UI performance, and reliable 1-day rollbacks.