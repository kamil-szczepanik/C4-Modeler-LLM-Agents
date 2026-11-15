## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe while maintaining legacy processing. It uses an Azure-hosted cloud architecture to provide online claim submission and adjuster workflows while ensuring data consistency and strict security.

## Key Elements
- Customers and Brokers: External users submitting online claims
- Claims Adjusters: Internal users managing claims via web application
- Business Operations Managers: Internal users monitoring migration metrics
- Azure Container Apps: Hosting API Gateway, Web Apps, and Integration containers
- Azure SQL Database: Managed relational storage with TDE, column-level PII encryption, Dynamic Data Masking, and readable secondary replica
- On-Premises COBOL/DB2 Mainframe: Legacy system of record
- Azure Active Directory (Entra ID): Identity and access management provider

## Relationships
- Customers/Brokers -> API Gateway: Submits claims via HTTPS/TLS 1.3
- Claims Adjusters -> Claims Adjuster Web App: Manages claims via HTTPS
- Business Operations Managers -> Operations Portal: Views metrics via HTTPS
- API Gateway -> Azure SQL: Reads/writes relational data via TDS (Encrypted Connection)
- Integration Container -> On-Premises COBOL/DB2 Mainframe: Synchronizes claims data via secure messaging/APIs

## Technology Stack
- Azure SQL Database (Business Critical tier): Provides high IOPS, automated tuning, and readable secondary replicas for analytical workload isolation
- Azure Container Apps: Hosts microservices and web applications with low cloud-experience overhead
- Azure AD (Entra ID): Provides Single Sign-On (SSO) and Role-Based Access Control (RBAC)
- Azure Key Vault: Manages Customer-Managed Keys (CMK) for Transparent Data Encryption and Always Encrypted
- Microsoft Defender for SQL: Provides real-time anomaly detection and vulnerability assessment

## Rationale
This architecture uses a hybrid Azure setup with robust data isolation and automated synchronization to meet strict consistency (R-04) and performance (R-05) requirements during the three-year mainframe migration. Security controls like Azure AD RBAC, Dynamic Data Masking, and Customer-Managed Keys ensure regulatory compliance while protecting sensitive PII.