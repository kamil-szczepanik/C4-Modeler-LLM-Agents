## Overview
[A hybrid insurance claims platform replacing a legacy mainframe while ensuring seamless data consistency and sub-second adjuster UI response times.]

## Key Elements
- Azure Application Insights
- Azure Container Apps / App Service
- Azure API Gateway & WAF
- Azure Blob Storage
- Azure Key Vault
- On-Premise COBOL/DB2 Mainframe

## Relationships
- Azure Application Insights -> Azure Container Apps / App Service: Telemetry collection [HTTPS]
- Azure API Gateway -> Azure Container Apps / App Service: Client requests [HTTPS]
- Azure Container Apps / App Service -> On-Premise COBOL/DB2 Mainframe: Hybrid claim sync [HTTPS / TLS 1.3]
- Azure Application Insights -> Azure Blob Storage: Telemetry export archive [HTTPS]

## Technology Stack
- Azure Application Insights: Centralized telemetry, distributed tracing, and business SLA dashboarding
- Terraform / Bicep: Infrastructure-as-Code for consistent environment provisioning and drift prevention
- Azure Blob Storage: Long-term immutable telemetry archiving for insurance compliance
- Azure Key Vault: Customer-managed key management for secure telemetry export encryption

## Rationale
- The architecture uses managed cloud telemetry to mitigate high operational risks for a team with low cloud experience.
- Strict data encryption, PII masking, and hybrid correlation support regulatory compliance and strict consistency guarantees during the 3-year migration.