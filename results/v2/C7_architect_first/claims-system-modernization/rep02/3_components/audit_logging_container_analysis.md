## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by migrating claim types to a hybrid cloud architecture. The Audit Logging Container provides secure, immutable event logging to guarantee zero lost or duplicated claims during the migration.]

## Key Elements
- [Audit Ingestion API (Azure Function, Node.js)]
- [PII Sanitizer & Normalizer (Lightweight container)]
- [Immutable Storage Writer (Azure Blob Storage with WORM Policy)]
- [Azure Key Vault HSM]
- [Azure Monitor and Application Insights]

## Relationships
- [Claims Processing Service invokes Audit Ingestion API via HTTPS and OAuth2/JWT using Azure Managed Identities]
- [Audit Ingestion API passes raw events to PII Sanitizer via internal queue]
- [PII Sanitizer writes encrypted objects to Immutable Storage Writer via Azure SDK (HTTPS)]
- [Azure Monitor collects telemetry from Audit Ingestion API and Sanitizer via HTTPS]

## Technology Stack
- [Azure Functions: Serverless execution to reduce operational overhead for a low-experience cloud team]
- [Azure Blob Storage WORM: Native time-based immutability policy ensuring regulatory compliance]
- [Azure Key Vault HSM: Customer-Managed Keys (CMK) for envelope encryption of sensitive claims data]
- [Terraform: Infrastructure as Code for automated deployment and WORM immutability validation]

## Rationale
[The architecture satisfies strict regulatory consistency (R-04) and security requirements while balancing the team's low cloud experience through managed services. Automated Terraform checks and WORM storage ensure tamper-resistant compliance to safely accelerate claim type migrations.]