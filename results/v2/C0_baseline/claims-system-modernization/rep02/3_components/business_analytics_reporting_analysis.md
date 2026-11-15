## Overview
[The system modernizes a regional insurer's legacy claims platform through a hybrid migration architecture, enabling phased claim type transitions while maintaining the 30-year-old mainframe as the system of record.]

## Key Elements
- Finance & Operations Executives
- Business Analytics & Reporting Container
- ETL Ingestion Worker (`Azure Functions / Python`)
- Transform & Load Component (`Azure Data Factory`)
- Data Warehouse Store (`Azure SQL Database`)
- Semantic & Reporting Model (`Power BI Embedded`)

## Relationships
- ETL Ingestion Worker reads from Azure Service Bus Topics via AMQP and Legacy Mainframe via SFTP/DB2 dump
- ETL Ingestion Worker writes to Azure SQL Staging Schema via T-SQL
- Transform Component updates Data Warehouse Store via T-SQL Stored Procedures
- Power BI Embedded queries Data Warehouse Store via T-SQL with Row-Level Security

## Technology Stack
- Azure SQL Database: Provides relational storage and star schema for unified reporting with minimal cloud learning curve
- Azure Data Factory: Manages declarative data pipelines to ensure processing finishes within the 23:00-05:00 batch window
- Azure Functions (Python): Executes lightweight event ingestion and mainframe batch extraction workers
- Power BI Embedded: Delivers role-based executive dashboards with Entra ID pass-through RLS
- Azure Key Vault & Managed Identities: Secures credentials and enforces zero-hardcoded-secret policies

## Rationale
[This architecture bridges the legacy-to-cloud gap by establishing a secure, isolated staging and data warehouse layer that unifies mainframe and modern cloud data without violating the strict 3-year mainframe system of record constraint. It accommodates the team's low cloud experience through managed Azure services while enforcing enterprise-grade security and regional compliance.]