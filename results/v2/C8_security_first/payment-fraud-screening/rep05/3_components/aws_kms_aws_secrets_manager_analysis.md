## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages case reviews for suspicious transactions. It ensures PCI-DSS Level 1 compliance and 7-year auditability under a strict 25,000 EUR monthly budget operated by three engineers.

## Key Elements
* AWS KMS & AWS Secrets Manager (Security Container)
* Key Management Service (KMS) Component
* Secrets Manager Component
* Scoring Engine Container with Envelope Encryption Cache
* Case Management API Container with Secrets In-Memory Cache
* AWS Lambda (Secret Rotation)

## Relationships
* Scoring Engine Container -> KMS Component: Requests Data Keys via local in-memory cache [AWS IAM, AWS PrivateLink, TLS 1.3]
* Case Management API Container -> Secrets Manager Component: Fetches and temporarily caches database credentials [AWS IAM, AWS PrivateLink, TLS 1.3]
* Secrets Manager -> AWS Lambda: Triggers automated credential rotation [AWS Internal]

## Technology Stack
* AWS KMS: Manages customer-managed CMKs with annual rotation for envelope encryption
* AWS Secrets Manager: Manages encrypted database credentials with 30-day automated rotation
* AWS PrivateLink (VPC Endpoints): Secures internal traffic without public internet exposure
* AWS Lambda: Executes automated secret rotation via native built-in templates
* Terraform: Implements Infrastructure-as-Code to prevent manual console drift

## Rationale
This architecture uses AWS-managed encryption and secret rotation to satisfy PCI-DSS Level 1 compliance and 7-year auditability with minimal operational overhead for a three-engineer team. Client-side caching and VPC endpoints ensure sub-50ms latency at 3,000 TPS while maintaining strict budget and availability constraints.