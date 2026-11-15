## Overview
The system screens card-not-present payment authorizations for fraud in real-time while providing a case management UI for analysts. It operates on AWS to deliver sub-50ms decisions and 7-year tamper-evident auditability.

## Key Elements
* **Payer (End Customer):** Initiates checkouts
* **Merchant:** Receives transaction approvals
* **Fraud Analyst:** Reviews suspicious cases via Case Management UI
* **Risk Operations Manager:** Oversees audit logs and compliance
* **Payment Gateway / Acquirer:** External system sending authorization payloads
* **Card Networks / Tokenization Service:** External system providing PAN tokenization
* **ML Model / Rule Provider:** External service supplying fraud models
* **Fraud Screening System (AWS `eu-west-1`):** Core cloud software system

## Relationships
* **Payment Gateway** -> **Fraud Screening System** [HTTPS/gRPC]: Sends real-time authorization payloads for synchronous scoring
* **Fraud Screening System** -> **ML Model / Rule Provider** [HTTPS/S3]: Fetches updated risk models asynchronously for zero-downtime updates

## Technology Stack
* **AWS (`eu-west-1`):** Cloud infrastructure provider selected to fit the 25,000 EUR monthly budget for a 3-engineer team
* **gRPC / REST:** Protocols ensuring low-latency communication for <50ms P99 decision requirements
* **mTLS:** Security protocol enforcing strict trust boundaries between external gateways and the screening system
* **WORM (Write Once, Read Many) Storage:** Storage technology ensuring 7-year tamper-evident auditability for compliance

## Rationale
This architecture uses cloud-managed infrastructure in AWS and asynchronous model updates to meet the strict sub-50ms latency and 25,000 EUR budget constraints. It maintains PCI-DSS Level 1 compliance through tokenized card data and immutable audit logs.