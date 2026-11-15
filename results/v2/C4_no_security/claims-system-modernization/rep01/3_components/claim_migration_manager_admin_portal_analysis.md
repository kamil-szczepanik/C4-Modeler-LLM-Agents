## Overview
[A secure hybrid cloud platform for modernizing a regional insurer's 30-year-old mainframe claims system via incremental migration over 3 years.]

## Key Elements
- Migration Operations Lead
- Claim Migration Manager / Admin Portal (.NET / C#)
- Migration Controller API
- Feature Management Service
- Pre-Flight Validation Engine
- Audit & Reconciliation Component
- Azure App Configuration
- Anti-Corruption Layer (ACL) Gateway
- Core Claims Domain (.NET / C#)
- Operational Data Store (Azure Database for PostgreSQL)
- Microsoft Entra ID

## Relationships
- Migration Operations Lead accesses Claim Migration Manager via HTTPS with Microsoft Entra ID SSO and PIM
- Claim Migration Manager invokes Migration Controller API using REST/gRPC
- Feature Management Service interfaces with Azure App Configuration using HTTPS
- Pre-Flight Validation Engine communicates with Anti-Corruption Layer Gateway and Operational Data Store using gRPC/REST
- Claim Migration Manager renders telemetry from Azure Managed Grafana and Azure Application Insights

## Technology Stack
- .NET / C#: Chosen for enterprise maintainability and team backend expertise
- Azure App Configuration: Provides atomic routing switches and state management for zero-downtime rollbacks
- Azure Database for PostgreSQL: Stores operational migration state and audit logs securely
- Azure Managed Grafana & Application Insights: Delivers real-time observability and migration metrics without custom charting overhead
- Microsoft Entra ID: Ensures secure single sign-on and privileged identity management for administrators

## Rationale
[The hybrid architecture isolates expensive mainframe changes while enabling incremental claim migration with a one-day rollback capability. Using managed Azure services mitigates the team's cloud experience gap while ensuring strict compliance, auditability, and zero data loss.]