## Overview
The system modernizes a 30-year-old regional insurer mainframe claims platform by migrating claim types gradually to a cloud-based architecture. It ensures zero data loss during hybrid co-existence using a dedicated background reconciliation service.

## Key Elements
- Reconciliation Job Scheduler (Quartz/Spring Batch Scheduler)
- Mainframe Data Reader (Spring Batch component using On-Premise Integration Agent)
- Modern DB Reader (Spring Data JPA)
- Discrepancy Analyzer (Java Streams)
- Alert & Compensation Publisher (Azure Service Bus Client)
- Audit Log Repository Writer (Spring Data JDBC)

## Relationships
- Reconciliation Job Scheduler triggers Mainframe Data Reader and Modern DB Reader via in-process method calls.
- Mainframe Data Reader queries the On-Premise Integration Agent via REST over TLS 1.3.
- Modern DB Reader queries the Modern Claims Database via JDBC over TLS 1.3.
- Discrepancy Analyzer passes data to Audit Log Repository Writer synchronously via JDBC.
- Discrepancy Analyzer emits alerts to Alert & Compensation Publisher asynchronously via Azure Service Bus.

## Technology Stack
- Java / Spring Batch: Provides robust, predictable chunk-processing for batch consistency.
- Azure Service Bus: Asynchronous message broker for reliable discrepancy alerts and compensating transactions.
- Azure SQL Database: Modern relational persistence layer for audit logs and claims data.
- REST over TLS 1.3: Secure protocol for communication with the On-Premise Integration Agent.

## Rationale
This architecture guarantees strict data consistency and zero claim loss during the hybrid migration phase. It respects the legacy mainframe constraints and limited cloud experience by utilizing familiar Java enterprise batch tooling.