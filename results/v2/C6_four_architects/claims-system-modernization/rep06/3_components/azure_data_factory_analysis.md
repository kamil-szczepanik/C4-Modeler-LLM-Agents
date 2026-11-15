## Overview
[The system modernizes a 30-year-old mainframe insurance claims platform via a hybrid cloud architecture, gradually migrating claim types while maintaining legacy parity. It ensures zero data loss, strict batch compliance, and seamless multi-system integration.]

## Key Elements
* Mainframe Extraction Pipeline (ADF Pipeline)
* Staging Blob Storage (Azure Data Lake Storage Gen2)
* Transformation & Ingestion Flow (ADF Mapping Data Flows)
* Reconciliation & Error-Handling Pipeline (ADF Pipeline)
* Monitoring & Alerting Trigger (ADF Tumbling Window / Azure Monitor)
* Self-Hosted Integration Runtime (SHIR) Cluster (Multi-node active-active)
* Dead-Letter & Quarantine Container (Azure Blob Storage)
* Mainframe Schema Registry (Azure Purview / ADF Dataset Metadata)

## Relationships
* Mainframe Extraction Pipeline reads from On-Premises COBOL/DB2 Mainframe via SHIR Cluster [JDBC / Encrypted TLS over HTTPS]
* Mainframe Extraction Pipeline pushes payloads to Staging Blob Storage [HTTPS]
* Transformation & Ingestion Flow writes to Azure SQL Database [T-SQL/JDBC via Managed Private Endpoint]
* Transformation & Ingestion Flow writes invalid payloads to Dead-Letter & Quarantine Container [REST/HTTPS]
* Transformation & Ingestion Flow reads schema definitions from Mainframe Schema Registry [Metadata API]
* Monitoring & Alerting Trigger invokes Mainframe Extraction Pipeline [Internal ADF Control Plane]
* Mainframe Integration Adapter Container invokes Mainframe Extraction Pipeline [Azure Event Grid / ADF REST API]

## Technology Stack
* Azure Data Factory: Orchestrates ETL, CDC, and batch workflows due to robust hybrid connectivity options
* Azure Data Lake Storage Gen2: Temporarily holds raw parquet files to optimize processing within the strict batch window
* Azure Blob Storage: Provides append blobs for isolating malformed records in the Dead-Letter quarantine
* Azure SQL Database: Stores modern claim data accessed by the Adjuster Workspace via Entity Framework Core
* ADF Self-Hosted Integration Runtime: Secures on-premises mainframe communication without opening inbound firewall ports

## Rationale
[The hybrid architecture utilizes a multi-node SHIR cluster and staging blobs to respect the rigid 6-hour batch window and network boundaries. Automated reconciliation pipelines and idempotency layers guarantee zero data loss and strict consistency without requiring expensive legacy mainframe modifications.]