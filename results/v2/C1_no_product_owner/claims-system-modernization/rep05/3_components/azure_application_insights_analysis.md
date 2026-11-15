## Overview
This system modernizes an on-premises COBOL/DB2 mainframe insurance claims platform by introducing a hybrid cloud architecture. Azure Application Insights provides centralized observability and distributed tracing across the platform.

## Key Elements
- Azure Application Insights
- Telemetry Ingestion Engine
- Log Analytics Workspace Storage
- Application Map Generator
- Availability and Alerting Sub-component
- Live Metrics Stream
- Diagnostic Export & Archive Sub-component
- Claims Web Application, API Gateway & BFF, Integration & Anti-Corruption Layer

## Relationships
- Claims Web App, BFF, and Functions -> Telemetry Ingestion Engine [HTTPS/OpenTelemetry]
- Telemetry Ingestion Engine -> Log Analytics Workspace Storage [Internal Azure Storage Protocol]
- Telemetry Ingestion Engine -> Application Map Generator [Internal Stream Processing]
- Telemetry Ingestion Engine -> Live Metrics Stream [In-Memory Telemetry Broadcast]
- Alerting & Synthetic Monitoring -> Log Analytics Workspace Storage [KQL Queries]
- Log Analytics Workspace Storage -> Diagnostic Export & Archive Sub-component [Azure Storage SDK]

## Technology Stack
- Azure Application Insights: Centralized observability platform to monitor hybrid latency bottlenecks.
- OpenTelemetry: Standardized protocol for collecting distributed traces and metrics.
- Kusto Query Language (KQL): Used for rapid querying and retention analysis within log storage.
- Azure Blob Storage: Long-term telemetry archiving with Customer-Managed Keys via Azure Key Vault.
- Azure Private Link: Secures telemetry transit by bypassing the public internet.

## Rationale
This architecture establishes robust observability to manage the complexity of a hybrid cloud migration with a low-experience cloud team. Security and data governance controls ensure PII scrubbing and compliance for sensitive insurance claims.