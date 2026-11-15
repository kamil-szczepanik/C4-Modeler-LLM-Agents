## Overview
The Real-Time Payment Fraud Screening Platform screens card-not-present payment authorizations for fraud at 3,000 TPS while enabling analysts to review suspicious transactions. It ensures sub-50ms latency, PCI-DSS compliance, and a 7-year tamper-evident audit trail within a €25k monthly AWS budget.

## Key Elements
*   **Payment Gateway / Acquirer**: Upstream actor submitting authorization requests.
*   **Fraud Analyst & Risk Manager**: Internal users reviewing cases and monitoring fraud metrics.
*   **Corporate Identity Provider (IdP)**: Authenticates analysts via OIDC/SAML.
*   **Card Tokenization Provider**: External vault for PCI-DSS scope reduction.
*   **Notification Gateway**: External SMS/Email service (Amazon SES/Twilio) for alerts.
*   **Real-Time Payment Fraud Screening Platform**: Core AWS-hosted system containerized on ECS Fargate.

## Relationships
*   **Payment Gateway** -> *Sends Authorization Requests (gRPC/HTTPS via AWS PrivateLink and NLB)* -> **Fraud Screening Platform**
*   **Fraud Analyst** -> *Reviews cases and tunes rules (HTTPS via ALB)* -> **Fraud Screening Platform**
*   **Fraud Screening Platform** -> *Authenticates users (OIDC/SAML)* -> **Corporate IdP**
*   **Fraud Screening Platform** -> *Sends operational alerts (HTTPS)* -> **Notification Gateway**

## Technology Stack
*   **Compute**: Amazon ECS with AWS Fargate to eliminate node management toil for a 3-person team.
*   **Networking**: AWS Network Load Balancer (NLB) with AWS PrivateLink for sub-50ms P99 latency.
*   **Audit & Storage**: AWS QLDB or S3 Object Lock for tamper-evident 7-year audit logs.
*   **Deployment**: GitOps (ArgoCD) for zero-downtime model and rule updates.

## Rationale
This architecture uses serverless containers and private networking to meet strict performance and PCI-DSS requirements without excessive operational overhead. The lean AWS stack stays comfortably within the €25k monthly budget while supporting a 3-person engineering team.