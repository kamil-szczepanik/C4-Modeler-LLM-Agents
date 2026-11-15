## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a legacy mainframe with a modern Azure cloud solution. It ensures seamless claim processing and business continuity during a three-year migration.]

## Key Elements
- Operations and Support Teams, Engineering Leads
- Observability Service
- OpenTelemetry Collector Component (Azure Container Apps)
- Azure Monitor Exporter Component
- Managed Prometheus Exporter Component
- Grafana Visualization Component (Azure Managed Grafana)
- Secure Hybrid Ingress Component (Azure Private Link, VPN/ExpressRoute)

## Relationships
- .NET and Node.js containers transmit telemetry to OpenTelemetry Collector Component via OTLP over gRPC/HTTP
- OpenTelemetry Collector Component routes logs and traces to Azure Monitor Exporter Component
- OpenTelemetry Collector Component forwards metrics to Managed Prometheus Exporter Component
- Grafana Visualization Component queries Azure backends via PromQL and Azure Monitor APIs
- On-premise legacy mainframe and ACL Gateway transmit telemetry via Secure Hybrid Ingress Component using Azure Private Link and VPN/ExpressRoute

## Technology Stack
- Azure Container Apps: Hosts the OpenTelemetry Collector for scalable ingestion without managing infrastructure.
- Azure Application Insights & Azure Monitor: Captures APM traces and application logs with reduced operational overhead.
- Azure Managed Prometheus: Ingests operational metrics while abstracting underlying storage maintenance.
- Azure Managed Grafana: Provides unified, business-centric dashboards for incident management.
- OpenTelemetry (OTLP): Standardizes telemetry instrumentation across .NET and Node.js to prevent vendor lock-in.
- Azure Private Link & VPN/ExpressRoute: Secures hybrid telemetry ingestion from on-premise components.

## Rationale
- This architecture minimizes operational complexity and maintenance overhead for a team with limited cloud experience by leveraging fully managed Azure services. It guarantees business continuity and strict consistency (R-04) through unified, real-time observability across the hybrid environment.