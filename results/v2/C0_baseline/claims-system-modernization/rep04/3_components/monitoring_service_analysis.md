## Overview
[The Monitoring Service provides distributed tracing, telemetry ingestion, and hybrid observability for the Insurance Claims Modernization platform. It ensures system reliability, fast adjuster response times, and audit compliance across the hybrid cloud-mainframe environment.]

## Key Elements
- [Telemetry Collector Component (Application Insights SDK / OpenTelemetry)]
- [Telemetry Processor Component (Application Insights Telemetry Initializer)]
- [Log Analytics Workspace (Azure Log Analytics)]
- [Alert Action Groups (Azure Monitor Action Groups)]
- [Mainframe Integration Webtest (Azure Application Insights Availability Tests)]

## Relationships
- [Backend Service -> Telemetry Collector: Forwards application traces and metrics via HTTPS / OpenTelemetry]
- [Telemetry Collector -> Telemetry Processor: Passes raw telemetry for sanitization in-memory]
- [Telemetry Processor -> Log Analytics Workspace: Persists sanitized logs and metrics via Azure Internal Storage API]
- [Log Analytics Workspace -> Alert Action Groups: Evaluates KQL rules to trigger notifications via Azure Event Grid]
- [Mainframe Integration Webtest -> Mainframe Integration Adapter: Periodically pings integration path via HTTPS]

## Technology Stack
- [Azure Application Insights: Core APM tool for distributed tracing and availability tests]
- [OpenTelemetry / Application Insights SDK: Standardized telemetry generation across .NET Core services]
- [Azure Log Analytics: Underlying data store utilizing Kusto Query Language (KQL) for log aggregation and migration dashboards]
- [Azure Monitor Action Groups: Automated alert routing integrating with PagerDuty and webhooks]
- [Azure Key Vault: Manages customer-managed keys (CMK) for log storage encryption]

## Rationale
- [The architecture centralizes telemetry to maintain strict data consistency and PII masking during hybrid cloud migration. It balances the team's limited cloud experience with robust observability to protect critical batch windows and business SLAs.]