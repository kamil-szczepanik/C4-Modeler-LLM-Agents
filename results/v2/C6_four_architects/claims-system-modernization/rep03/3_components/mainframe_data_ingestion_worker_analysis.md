## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system while maintaining ongoing operations. Its core purpose is to incrementally migrate claim types to a modern Azure-based cloud architecture without disrupting legacy processing.

## Key Elements
- Mainframe Batch Poller (Azure Timer Trigger Function)
- Sequential File Parser (Python/Node.js Component)
- Data Transformation & Mapping Engine
- Ingestion Dispatcher
- Idempotency & Checkpoint Manager
- Batch Orchestration Controller (Azure Durable Functions)
- Ingestion Error Handler
- Mainframe Vault Credential Provider (Azure Key Vault Client)
- Integration & Sync Service (Azure Container Apps)
- Claims Database (Azure SQL Database)
- Notification & Document Store (Azure Blob Storage)
- Legacy Mainframe (SFTP Server / DB2)
- Core Rating & Underwriting Engine

## Relationships
- Mainframe Batch Poller -> Legacy Mainframe SFTP Server: Fetches daily batch extracts [SFTP]
- Mainframe Batch Poller -> Mainframe Vault Credential Provider: Retrieves secrets [Azure Managed Identity / HTTPS]
- Batch Orchestration Controller -> Sequential File Parser: Orchestrates parallel processing [Internal Binding]
- Sequential File Parser -> Ingestion Error Handler: Forwards malformed records [Internal Queue]
- Ingestion Error Handler -> Notification & Document Store: Persists poison messages [Azure Blob Storage]
- Data Transformation & Mapping Engine -> Core Rating & Underwriting Engine: Enriches claims data [REST/HTTPS]
- Data Transformation & Mapping Engine -> Idempotency & Checkpoint Manager: Verifies record uniqueness [DB Query]
- Idempotency & Checkpoint Manager -> Claims Database: Persists checkpoints [ADO.NET/HTTPS]
- Ingestion Dispatcher -> Integration & Sync Service: Publishes normalized events [Azure Service Bus]

## Technology Stack
- Azure Durable Functions: Coordinates parallel chunk processing within the rigid batch window
- Azure Timer Trigger Function: Initiates automated data extraction securely
- Python/Node.js: Parses fixed-width EBCDIC flat files efficiently
- Azure Key Vault: Secures SFTP and database credentials via managed identity
- Azure Service Bus: Guarantees reliable, decoupled messaging for data synchronization
- Azure Blob Storage: Stores error payloads for audit and manual remediation
- Azure SQL Database: Persists transaction states and claims data consistently

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while using managed Azure services to simplify cloud adoption for an inexperienced team. Durable Functions and checkpointing guarantee exact-once processing (R-04) within the strict nightly 6-hour batch window.