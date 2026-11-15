## Overview
The system provides a hybrid insurance claims modernization platform to gradually replace a legacy mainframe claims system. It ensures continuous claim processing while migrating specific claim types to modern cloud infrastructure.

## Key Elements
- Observability & Logging Container (Azure Application Insights)
- API Gateway Container (Azure Container Apps / API Management)
- Customer BFF & Adjuster BFF Containers (Azure App Service / Container Apps)
- Modular Monolith Container & Anti-Corruption Layer (ACL) Container
- OpenTelemetry SDKs & W3C Trace Context propagation headers
- Centralized audit log sink and OpenTelemetry Collector sidecars

## Relationships
- Observability & Logging Container collects telemetry from API Gateway, Customer BFF, Adjuster BFF, and Modular Monolith containers via Telemetry SDK [W3C Trace Context, HTTPS]
- Application containers emit structured JSON logs and traces to Application Insights [HTTPS]
- Security and data mutation events route to a dedicated audit log sink [Secure API]

## Technology Stack
- Azure Application Insights: Managed SaaS telemetry platform to minimize operational overhead for a cloud-inexperienced team.
- OpenTelemetry & W3C Trace Context: Standardized protocol for distributed tracing across hybrid boundaries.
- Terraform / Bicep (IaC): Infrastructure-as-Code for reproducible telemetry setups, alerts, and dashboards.
- Azure Key Vault & IAM Proxy: Secure secrets management and single sign-on integration.

## Rationale
This architecture minimizes operational complexity for a team with limited cloud experience by utilizing managed Azure services and standard telemetry protocols. It guarantees end-to-end visibility and rapid incident response during the phased hybrid migration.