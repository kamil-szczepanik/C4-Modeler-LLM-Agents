## Overview
The system is an Azure SQL Database component within a hybrid insurance claims modernization platform. Its core purpose is to securely store relational claims data with strict per-module schema separation while gradually migrating claim types from the legacy mainframe.

## Key Elements
- Azure SQL Database: Primary relational data store for the modular monolith platform.
- Azure App Service: Container executing application logic and communicating with the database.
- CI/CD Pipeline (Azure DevOps / GitHub Actions): Automated deployment and testing runner.
- Managed Identity: Cloud-native authentication mechanism.

## Relationships
- Azure App Service -> Azure SQL Database: Reads and writes claim data [Tabular Data Stream over TLS]
- CI/CD Pipeline -> Azure SQL Database: Applies isolated schema migrations [SQL via Azure Bicep / Terraform]
- Azure Active Directory -> Managed Identity: Provisions secure authentication tokens [OAuth 2.0 / OpenID Connect]

## Technology Stack
- Azure SQL Database: Relational database providing built-in Point-In-Time Restore (PITR), Query Store, and temporal tables for robust data safety and auditing.
- Azure Bicep / Terraform: Infrastructure as Code for reliable, repeatable environment provisioning.
- FluentMigrator / Entity Framework Core Migrations: Automated database migration tools for isolated schema deployments.
- Managed Identities: Passwordless authentication securing connections between App Service and Azure SQL.

## Rationale
This architecture uses automated schema migrations and strict access controls to mitigate risks for a team with limited cloud experience. Built-in database features like temporal tables, PITR, and isolation strategies ensure zero data loss (R-04) and rapid rollback capabilities (R-06).