## Overview
[Centralized Logging & Monitoring provides operational visibility, distributed tracing, and compliance auditing across the hybrid Azure and legacy mainframe architecture. It mitigates the team's limited cloud experience through automated governance, managed PaaS services, and proactive synthetic monitoring.]

## Key Elements
- Azure Monitor (Managed PaaS for metrics, logs, and alerts)
- API Gateway / Anti-Corruption Layer (ACL) with Log-Scrubbing Middleware
- Azure App Configuration and Azure Key Vault (Dynamic log-level toggling)
- CI/CD Log Schema Validation Linter
- Azure Blob Storage (Cold archival for compliance audit trails)

## Relationships
- Microservices & ACL to Azure Monitor via HTTPS / OpenTelemetry using W3C Trace Context headers
- API Gateway / ACL to Legacy COBOL/DB2 Mainframe via Synchronous Protocol / Batch with injected correlation IDs
- Azure Monitor to On-Call Notification Channels via HTTPS / Webhooks for actionable alerts
- Azure Monitor to Azure Blob Storage via Automated Scheduled Export for log archival

## Technology Stack
- Azure Monitor / Application Insights: Chosen for managed PaaS capabilities to minimize operational overhead for a cloud-inexperienced team.
- OpenTelemetry / W3C Trace Context: Selected for standardized distributed tracing across hybrid boundaries without modifying legacy COBOL code.
- JSON Structured Logging: Enforced via CI/CD linters to ensure maintainability and consistent log parsing.
- Bicep / Terraform: Utilized for Infrastructure-as-Code to codify alert rules, dashboards, and retention policies, preventing configuration drift.

## Rationale
[This architecture ensures zero data loss and compliance during hybrid operations by combining strict log governance, PII scrubbing, and distributed tracing across the Azure-mainframe boundary. It empowers the cloud-inexperienced team with automated dashboards, dynamic log-level toggling, and IaC-managed observability.]