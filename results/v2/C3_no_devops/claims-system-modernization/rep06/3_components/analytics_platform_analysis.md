## Overview
[The Analytics Platform provides real-time reporting, auditing, and migration tracking for the modern insurance claims system. It ensures business continuity by monitoring dual-system performance during the three-year mainframe migration.]

## Key Elements
* Business Operations Managers and Claims Executives
* Azure Event Hubs
* Azure Stream Analytics
* Azure Synapse Analytics (Dedicated SQL Pool)
* Power BI Embedded
* Azure Functions
* Azure Key Vault and Log Analytics

## Relationships
* Azure Kubernetes Service / Azure SQL Database -> Azure Event Hubs [AMQP over TLS 1.3]
* Azure Functions -> Azure Synapse Analytics [T-SQL via TDS/TLS 1.3]
* Azure Synapse Analytics -> Power BI Embedded [Direct Query / HTTPS via TLS 1.3]
* Analytics Platform -> Azure Key Vault [Managed Identity / HTTPS]

## Technology Stack
* Azure Event Hubs: Ingests real-time CDC streams using AMQP for high throughput
* Azure Stream Analytics: Processes in-transit validation checks to satisfy R-04
* Azure Synapse Analytics: Stores historical claim metrics with Row-Level Security and dynamic data masking
* Power BI Embedded: Renders the Migration Executive Dashboard with Azure Entra ID SSO
* Azure Functions: Executes serverless reconciliation logic without custom ETL infrastructure

## Rationale
[This managed-service-heavy architecture minimizes custom code to accommodate the team's low cloud experience. It provides secure, real-time visibility to satisfy strict auditability and compliance requirements during the hybrid migration.]