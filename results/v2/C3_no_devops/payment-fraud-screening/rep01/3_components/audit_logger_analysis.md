## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions and provides case management for suspicious payments.]
[It ensures secure, auditable, and sub-50ms fraud decisions under strict PCI-DSS Level 1 compliance constraints.]

## Key Elements
* Personas: Fraud Analyst, Compliance Officer, External Regulators
* Containers: Audit Logger (AWS Lambda), Message Queue (Amazon SQS), Tamper-Evident Storage (Amazon S3)
* Audit Logger Components: Queue Consumer Component (Go), Canonical Formatter Component (Go), Storage Writer Component (Go)

## Relationships
* Queue Consumer -> Message Queue: Polls payloads [AWS SDK over HTTPS]
* Queue Consumer -> Canonical Formatter: Normalizes data [In-memory Go structs]
* Canonical Formatter -> Storage Writer: Passes formatted payload [In-memory function call]
* Storage Writer -> Tamper-Evident Storage: Writes audit logs with Object Lock [HTTPS / S3 API]
* Storage Writer -> AWS KMS: Signs payloads for cryptographic non-repudiation [AWS KMS API]

## Technology Stack
* AWS Lambda: Serverless execution for zero idle infrastructure cost within the 25k EUR budget
* Go: High-performance language for the AWS Lambda handler and internal components
* Amazon S3 Object Lock: Compliance Mode enforcement for tamper-evident 7-year audit retention
* AWS KMS: Cryptographic signing and encryption using customer-managed keys (CMK)
* Amazon SQS: Decoupled event ingestion secured via VPC Endpoint policies

## Rationale
[Serverless components minimize operational overhead for a 3-person engineering team while strictly adhering to the 25,000 EUR monthly budget.]
[Immutable storage and cryptographic signing satisfy PCI-DSS Level 1 mandates and 7-year auditability requirements.]