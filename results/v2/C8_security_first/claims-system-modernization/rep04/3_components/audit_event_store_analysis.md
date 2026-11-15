## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform while ensuring zero data loss and uninterrupted daily operations. It processes online claims, provides an adjuster web application, and maintains strict regulatory compliance.

## Key Elements
- Claim Processing Core (Azure Container Apps)
- Event Ingestion Engine (Azure Functions / .NET 8)
- Operational Event Store (Azure Cosmos DB for NoSQL)
- Audit & Compliance Archive (Azure SQL Ledger)
- Adjuster Web App (Azure Container Apps)
- Compliance Officers

## Relationships
- Claim Processing Core sends domain events to Event Ingestion Engine via AMQP over Azure Service Bus
- Event Ingestion Engine writes to Operational Event Store via HTTPS/TCP over Private Endpoint
- Event Ingestion Engine writes to Audit & Compliance Archive via T-SQL over Private Endpoint
- Compliance Officers query Audit & Compliance Archive via SQL over Private Endpoint

## Technology Stack
- Azure Container Apps: Scalable runtime for microservices without deep cloud orchestration complexity
- Azure Functions (.NET 8): Serverless event ingestion with managed identity integration
- Azure Cosmos DB for NoSQL: Partitioned operational data store ensuring sub-second event retrieval
- Azure SQL Ledger: Cryptographically secure, tamper-evident audit trail meeting strict regulatory requirements
- Azure Service Bus: Reliable message broker providing dead-letter queues and backpressure handling

## Rationale
This hybrid architecture isolates complex legacy mainframe dependencies while establishing a modern, secure, and compliant cloud foundation. It successfully balances strict regulatory immutability demands with high-performance operational requirements for claims adjusters.