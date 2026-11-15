## Overview
The Case Management Backend manages the review workflow for suspicious payment authorizations routed to fraud analysts. It ensures secure, compliant, and auditable handling of flagged cases while meeting strict regulatory standards.

## Key Elements
- **Case API Controller**: Exposes REST endpoints for the Fraud Analyst UI.
- **Workflow Orchestrator**: Manages state transitions for open, under review, escalated, and resolved cases.
- **Audit Logger Component**: Records analyst actions and case mutations durably.
- **Queue Consumer Service**: Consumes flagged cases from message queues.
- **Tokenization Filter / Redaction Component**: Scrubs and masks sensitive cardholder data.

## Relationships
- **Fraud Analyst UI** -> **Case API Controller**: Communicates via HTTPS/REST.
- **Queue Consumer Service** -> **Workflow Orchestrator**: Triggers new cases via In-Memory Java Method Calls.
- **Workflow Orchestrator** -> **Tokenization Filter / Redaction Component**: Passes payloads via In-Memory calls.
- **Tokenization Filter / Redaction Component** -> **Audit & Decision Store**: Persists sanitized data via PostgreSQL protocol.
- **Queue Consumer Service** -> **AWS SQS**: Ingests queue messages using AWS SDK.

## Technology Stack
- **Java (Spring Boot)**: Selected for enterprise-grade transaction management, deterministic memory handling, and robust security frameworks.
- **PostgreSQL**: Used for tamper-evident data storage and 7-year audit retention.
- **AWS SQS**: Provides reliable asynchronous queue messaging.

## Rationale
This architecture uses enterprise Java frameworks to guarantee transactional integrity and PCI-DSS compliance. Internal redaction components ensure strict data privacy while maintaining a comprehensive audit trail.