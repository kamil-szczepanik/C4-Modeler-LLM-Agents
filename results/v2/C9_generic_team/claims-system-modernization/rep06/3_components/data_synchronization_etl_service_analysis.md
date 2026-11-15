## Overview
[The Data Synchronization / ETL Service replicates and transforms state between the on-premise mainframe and cloud read models using managed Azure components. It ensures strict consistency and reliable hybrid data pipelines during incremental claim migrations.]

## Key Elements
- Data Synchronization / ETL Service (Azure Compute / ETL)
- On-Premise COBOL/DB2 Mainframe (System of Record)
- Cache / Read Model Store (Managed Cloud Database / Cache)
- Azure Service Bus (Message Broker & DLQ)
- Azure Application Insights (Observability)
- Azure App Configuration (Centralized Configuration Store)

## Relationships
- Data Synchronization / ETL Service -> On-Premise COBOL/DB2 Mainframe (System of Record): Extracts batch data and state via Secure Mainframe Protocols / ETL [ETL / Secure Protocols]
- Data Synchronization / ETL Service -> Cache / Read Model Store: Upserts transformed data and read models via Database Replication [Database Replication]
- Data Synchronization / ETL Service -> Azure Service Bus: Routes failed messages to Dead-Letter Queues (DLQs) using AMQP [AMQP]
- Data Synchronization / ETL Service -> Azure Application Insights: Publishes telemetry, lag metrics, and error rates via HTTPS [HTTPS]

## Technology Stack
- Azure App Service / Container Instances: Hosts the ETL service with modular adapters, supporting the team's cloud transition.
- Azure Service Bus: Provides resilient message brokering, circuit breakers, and Dead-Letter Queues (DLQs) to handle transient failures within the 23:00–05:00 batch window.
- Azure Application Insights: Delivers real-time observability, SLA tracking, and error logging for pipeline monitoring.
- Azure App Configuration: Stores centralized pipeline parameters, batch sizes, and feature toggles to enable rapid operational adjustments without code deployments.

## Rationale
- The architecture utilizes proven managed cloud tooling and modular adapters to offset the team's limited cloud experience while strictly adhering to the 6-hour batch window constraint.
- Idempotent upserts, automated reconciliation jobs, and bi-directional synchronization triggers guarantee data consistency and support rapid one-day rollbacks for migrated claim types.