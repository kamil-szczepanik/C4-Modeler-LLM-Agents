## Overview
This system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by gradually migrating claim types to a hybrid cloud architecture. It ensures seamless parallel operations, strict transactional consistency, and rapid rollbacks without disrupting daily business.

## Key Elements
* Customers & Brokers (External Users)
* Claims Adjusters (Internal Users)
* COBOL/DB2 Mainframe (System of Record)
* Active Directory (IAM)
* API Gateway / Anti-Corruption Layer (ACL)
* Azure Service Bus (Event Broker)
* Azure Redis Cache (State Store)
* Azure Functions / WebJobs (Worker / Background Processing)
* Azure Blob Storage (Document Store)
* Azure App Configuration & Key Vault

## Relationships
* Customers & Brokers interact with BFF via HTTPS (TLS 1.3) for online claim submission.
* Claims Adjusters access the new web application via HTTPS (TLS 1.3) with Azure AD SSO.
* API Gateway / ACL communicates with the COBOL/DB2 Mainframe via secure internal protocols (MQ/JDBC).
* Background Workers process asynchronous tasks via Azure Service Bus queues using AMQP.
* Workers store large payloads and documents in Azure Blob Storage via HTTPS.

## Technology Stack
* Microsoft Azure (Cloud Provider, West Europe) for modern scalable compute and managed services.
* Azure Functions / Durable Functions / WebJobs for serverless background processing and state orchestration.
* Azure Service Bus for reliable asynchronous messaging with Dead-Letter Queues (DLQ).
* Azure Blob Storage for Claim Check payload offloading.
* Azure App Configuration and Key Vault for centralized zero-hardcoding secret and setting management.
* Azurite for local cloud development and emulator-based testing.

## Rationale
* The hybrid architecture isolates expensive mainframe changes while enabling gradual, low-risk claim type migrations.
* Cloud-native patterns (Idempotency, Claim Check, Circuit Breaker) and Azure Functions ensure strict consistency, performance, and maintainability despite the team's limited cloud experience.