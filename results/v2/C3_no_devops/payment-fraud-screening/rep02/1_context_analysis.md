## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud in under 50 milliseconds while providing a secure case management interface for analysts. It operates within a strict PCI-DSS Level 1 compliance framework while supporting high-throughput transactions on AWS.

## Key Elements
- Payment Gateway / Core Processing Platform (External System)
- Fraud Analysts & Risk Managers (Users)
- Card Networks & Issuers (External Systems)
- Regulators / Audit & Compliance System (External System)
- Real-Time Payment Fraud Screening System (Primary System Boundary)

## Relationships
- Payment Gateway sends authorization requests to Fraud Screening System via gRPC/REST over TLS 1.3 (R-01, R-04)
- Fraud Analysts access Case Management UI via HTTPS with OAuth2/OIDC IAM (R-02, R-03, R-05)
- Fraud Screening System routes decisions to Card Networks and Issuers via TLS
- Fraud Screening System streams immutable audit logs to S3 Object Lock using AWS KMS signatures (R-06)
- Fraud Screening System streams analytics asynchronously via AWS EventBridge/Kinesis

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring high availability within budget constraints
- gRPC / REST over TLS 1.3: Ensures low-latency, secure real-time communication for 3,000 TPS
- OAuth2 / OIDC IAM: Provides secure Role-Based Access Control and multi-factor authentication for analysts
- AWS S3 Object Lock & AWS KMS: Guarantees tamper-evident, 7-year immutable audit retention (R-06)
- AWS EventBridge / Kinesis: Decouples asynchronous telemetry and analytics from the critical scoring path

## Rationale
This architecture isolates synchronous fraud scoring from asynchronous logging and analytics to consistently achieve sub-50ms P99 latency. Furthermore, it strictly enforces PCI-DSS scope boundaries and automated compliance controls to operate successfully within a fixed budget and small engineering team.