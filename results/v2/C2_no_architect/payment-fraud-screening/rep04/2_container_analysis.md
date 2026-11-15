## Overview
The system provides real-time card-not-present payment fraud screening and case management for a mid-size payment processor in AWS (eu-west-1). It screens 3,000 authorizations per second, routes suspicious payments to analysts, and enforces strict PCI-DSS compliance and 7-year tamper-evident auditability.

## Key Elements
*   **Users:** Fraud Analysts, Risk Managers, Compliance Officers, Shoppers/End-Consumers
*   **External Systems:** Payment Gateway / Shoppers
*   **Containers:** Real-Time Scoring Engine, Case Management Service, Tokenization Proxy, Audit & Cryptographic Signer Sidecar, Model Management Service
*   **Data Stores & Infrastructure:** Amazon ECS with Fargate, Amazon ECR, Amazon S3 (WORM with Glacier), AWS KMS, AWS Secrets Manager, AWS CloudHSM

## Relationships
*   Payment Gateway to Real-Time Scoring Engine via HTTPS/TLS 1.3
*   Real-Time Scoring Engine to Tokenization Proxy via gRPC
*   Scoring Engine to Audit Sidecar via IPC / Local gRPC
*   Fraud Analysts to Case Management Service via HTTPS (OIDC/OAuth2 via AWS Cognito)
*   Audit Sidecar to S3 WORM Bucket via AWS SDK (HTTPS)

## Technology Stack
*   **Compute:** AWS ECS with Fargate and Fargate Spot, using ECS Service Connect for mTLS to minimize operational overhead for a 3-person team.
*   **Security & Encryption:** AWS KMS (Customer-Managed Keys) and AWS CloudHSM for tamper-evident cryptographic signing and data-at-rest encryption.
*   **Secret & Token Management:** AWS Secrets Manager for secret zero and dedicated tokenization proxies for PCI-DSS scope reduction.
*   **Storage:** Amazon S3 with Object Lock (WORM) and Glacier Lifecycle Policies for 7-year immutable audit retention.

## Rationale
AWS ECS Fargate and managed services eliminate infrastructure management overhead, allowing a 3-person team to operate within a 25,000 EUR monthly budget. Memory-cached models and localized tokenization guarantee P99 latencies below 50 ms while satisfying strict PCI-DSS Level 1 and tamper-evident audit requirements.