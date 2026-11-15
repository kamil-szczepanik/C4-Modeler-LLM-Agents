## Overview
The Observability Service provides monitoring, tracing, and logging for the Real-Time Payment Fraud Screening System on AWS. It ensures strict compliance with PCI-DSS requirements, a 7-year audit trail, and low operational overhead.

## Key Elements
- Telemetry Collector: AWS Distro for OpenTelemetry (ADOT) sidecar
- Metrics & Tracing Backend: Amazon CloudWatch Metrics & AWS X-Ray
- Log Ingestion & Retention Manager: Amazon CloudWatch Logs and Amazon S3 with S3 Object Lock (Compliance Mode)
- Operations Dashboard: Amazon CloudWatch Dashboards
- Synthetic Monitoring: CloudWatch Synthetic Canaries

## Relationships
- Fraud Scoring Engine -> Telemetry Collector: Sends masked traces and metrics via gRPC over TLS 1.3
- Telemetry Collector -> Amazon CloudWatch & AWS X-Ray: Forwards sanitized metrics and traces over TLS 1.3
- Fraud Analysts -> Operations Dashboard: Views business and technical KPIs via HTTPS

## Technology Stack
- AWS Distro for OpenTelemetry (ADOT): Chosen for local payload scrubbing to protect cardholder data (PANs)
- Amazon CloudWatch & AWS X-Ray: Selected for native AWS integration, minimizing tool sprawl for a 3-engineer team
- Amazon S3 Object Lock: Implemented in Compliance Mode to guarantee tamper-evident 7-year audit retention
- CloudWatch Syntheticanary: Deployed for continuous uptime validation against the 1-minute availability SLA

## Rationale
This native AWS observability stack respects the 25,000 EUR monthly budget while keeping operational toil minimal for a 3-engineer team. It rigorously satisfies PCI-DSS security rules and the 7-year auditability mandate through automated log lifecycle management and immutable storage.