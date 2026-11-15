## Overview
[Document & Evidence Management Service manages secure, asynchronous processing of claims evidence for the Insurance Claims Modernization platform. It enables scalable, direct-to-cloud uploads with integrated malware scanning and strict WORM-compliant storage policies.]

## Key Elements
- Document API Controller (Spring Boot / Java Component)
- SAS Token Issuer Component
- Metadata Registrar Component
- Virus Scanning Processor (Azure Function / ClamAV Container)
- Storage Gateway (Azure Blob SDK)
- Azure Blob Storage (Quarantine Container and Trusted Evidence WORM Container)
- Azure Event Grid (with Dead Letter Queue)
- Customer Portal & Adjuster Workspace (React Web Apps)

## Relationships
- Customer Portal / Adjuster Workspace -> SAS Token Issuer (HTTPS/REST) for upload permissions
- Customer Portal -> Azure Blob Storage (HTTPS) for direct-to-blob upload using SAS tokens
- Customer Portal -> Metadata Registrar (HTTPS/REST) to finalize upload registration
- Claims Processing Service -> Document API Controller (HTTPS/REST) for evidence linking
- Azure Blob Storage -> Azure Event Grid -> Virus Scanning Processor (Event-driven trigger)
- Virus Scanning Processor -> Azure Blob Storage (HTTPS/Azure SDK) to move clean files to Trusted Container

## Technology Stack
- Java Spring Boot: Core runtime for API controllers providing robust enterprise integration
- Azure Blob Storage & Azure Blob SDK: Cloud object storage with WORM immutability and managed SDK interactions
- Azure Functions & ClamAV: Serverless execution environment for cost-effective, asynchronous virus scanning
- Azure Event Grid: Event routing backbone with Dead Letter Queue for reliable asynchronous messaging
- Azure Key Vault: Secure management of Customer-Managed Keys (CMK) for data encryption at rest

## Rationale
[This component architecture offloads heavy file uploads directly to cloud storage using short-lived SAS tokens, protecting backend resources while maintaining strict security controls. Asynchronous virus scanning via serverless Azure Functions ensures malicious files are quarantined without blocking claims processing workflows.]