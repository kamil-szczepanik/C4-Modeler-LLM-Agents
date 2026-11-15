## Overview
This system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claim submission and adjuster workflows while maintaining legacy synchronization.

## Key Elements
* Azure SQL Database
* Claim Transactional Store
* Integration Staging Store
* Row-Level Security & Access Management
* Azure Kubernetes Service
* Legacy Mainframe (On-Premises)
* Microsoft Entra ID
* Azure Private Endpoints

## Relationships
* Azure Kubernetes Service -> Claim Transactional Store: Executes parameterized SQL queries via TDS / SQL over TLS 1.3
* Claim Transactional Store -> Microsoft Entra ID: Authenticates requests using managed identities
* Integration Staging Store -> Legacy Mainframe (On-Premises): Syncs delta changes asynchronously via Change Data Capture (CDC) and data connectors
* Claim Transactional Store -> Azure SQL Database-Level Auditing: Writes security logs to Azure Storage/Log Analytics

## Technology Stack
* Azure SQL Database: Chosen for built-in High Availability and managed service benefits given limited cloud experience
* Temporal Tables (System-Versioned): Selected to track historical changes and satisfy auditability requirements
* Change Data Capture (CDC): Implemented to support the one-day rollback constraint (R-06)
* Microsoft Entra ID: Enforced for single sign-on (R-07) and secure database authentication
* Azure Private Endpoints: Deployed to isolate the database in a private subnet and prevent public access

## Rationale
The hybrid architecture balances low cloud team experience with strict consistency and rollback requirements. Leveraging native Azure SQL features minimizes custom code while ensuring secure coexistence with the legacy mainframe.