## Overview
The Case Management & Rules Service manages fraud analyst reviews, case workflows, and zero-downtime rule updates for the Real-Time Payment Fraud Screening system. It ensures strict PCI-DSS compliance, tamper-evident audit logging, and efficient fraud mitigation within AWS.

## Key Elements
- Fraud Analysts and Compliance Officers (Persona)
- Risk Managers / Fraud Team Leads (Persona)
- Case Workflow Controller (Component)
- Rule Authoring Engine (Component)
- Audit Logger (Component)
- Data Masking Proxy (Component)
- Decision Metadata Extractor (Component)
- Approval Workflow Interceptor (Component)

## Relationships
- Fraud Analysts -> Case Workflow Controller [HTTPS/REST]
- Rule Authoring Engine -> AWS AppConfig [HTTPS/AWS SDK]
- Case Workflow Controller -> Audit Logger [Internal Go Function Call]
- Audit Logger -> Amazon SQS [HTTPS/AWS SDK]

## Technology Stack
- Go: Chosen for high performance, low memory footprint, and suitability for the 3-engineer team.
- AWS AppConfig: Provides managed, zero-downtime rule configuration storage and state polling.
- Amazon SQS with DLQ: Ensures reliable message delivery and tamper-evident audit logging.
- AWS X-Ray: Enforces distributed tracing to monitor P99 latencies within budget.

## Rationale
This component architecture optimizes operational simplicity for a 3-engineer team by leveraging managed AWS services. It strictly enforces security and auditability constraints while maintaining high performance and zero-downtime rule updates.