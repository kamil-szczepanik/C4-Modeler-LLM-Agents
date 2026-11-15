## Overview
The Compliance/Audit Lambda container is a serverless AWS function responsible for ensuring GDPR and CCPA compliance through secure event ingestion, policy validation, data redaction, and audit reporting. It processes security and data-access events to maintain regulatory adherence for the Online Bookstore.

## Key Elements
- **Event Router**: TypeScript component multiplexing incoming events from Amazon EventBridge and Amazon MSK.
- **Compliance Policy Validator**: TypeScript rule-evaluation component checking retention and consent rules.
- **Audit Log Ingestor**: Node.js/TypeScript component utilizing AWS SDK to consume security and data-access events.
- **GDPR/CCPA Data Redactor**: Component executing erasure, anonymization, and PII scrubbing.
- **Compliance Report Generator**: Component aggregating audit trails and building scheduled reports.

## Relationships
- *Event Router* dispatches payloads to *Audit Log Ingestor*, *GDPR/CCPA Data Redactor*, and *Compliance Policy Validator* via in-memory function calls.
- *Compliance Policy Validator* triggers *GDPR/CCPA Data Redactor* via in-memory calls when regulatory thresholds are met.
- *Audit Log Ingestor* consumes events from *Amazon MSK* via TCP/TLS.
- *GDPR/CCPA Data Redactor* queries/mutates *Amazon Aurora Global Database* and *Amazon DynamoDB* via SQL/NoSQL protocols over TLS.
- *Compliance Report Generator* writes exports to *Amazon S3* via HTTPS and reads immutable metadata from *Amazon Athena* via HTTPS (AWS SDK).

## Technology Stack
- **AWS Lambda**: Serverless compute container providing a short-lived execution context.
- **Node.js / TypeScript**: Standardized runtime across all internal components to minimize cold-start latency.
- **AWS SDK**: Protocol library used for secure HTTPS/TLS communication with AWS services.

## Rationale
Standardizing on a unified Node.js/TypeScript runtime within AWS Lambda minimizes cold-start latency and eliminates polyglot overhead. Localizing validation and routing in-memory before executing destructive database mutations guarantees strict GDPR/CCPA guardrails.