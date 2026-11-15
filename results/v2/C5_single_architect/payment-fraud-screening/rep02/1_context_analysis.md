## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor and provides case management for fraud analysts. It operates on AWS to deliver low-latency fraud decisions while maintaining strict compliance, auditability, and budgetary constraints.

## Key Elements
* Payment Gateway / Core Processing Platform
* Fraud Analyst
* Identity Provider (IdP)
* Real-Time Payment Fraud Screening System
* AWS Key Management Service (KMS) / HSM

## Relationships
* Payment Gateway sends authorization requests to Real-Time Payment Fraud Screening System via REST/gRPC over HTTPS with mTLS.
* Fraud Analyst interacts with Real-Time Payment Fraud Screening System via Web UI over HTTPS.
* Fraud Analyst authenticates against Identity Provider via OIDC/SAML.
* Real-Time Payment Fraud Screening System connects to AWS KMS via AWS PrivateLink and HTTPS for cryptographic signing and envelope encryption.

## Technology Stack
* AWS Cloud Platform (eu-west-1 region): Selected to host the system within a managed environment matching the 25,000 EUR monthly budget and 3-person team limit.
* AWS KMS: Utilized for cryptographic signing to ensure tamper-evident audit logs and meet R-06 without operational overhead.
* REST / gRPC over HTTPS with mTLS: Chosen for secure, high-performance communication with the Payment Gateway.
* OIDC/SAML: Implemented via Identity Provider for secure, multi-factor analyst authentication.

## Rationale
This architecture isolates the PCI-DSS boundary and leverages fully-managed AWS services to meet strict sub-50ms latency (P99) and 3,000 TPS performance goals. By avoiding self-managed infrastructure, the three-person engineering team can reliably operate the system within the 25,000 EUR budget while enforcing 7-year tamper-evident auditability.