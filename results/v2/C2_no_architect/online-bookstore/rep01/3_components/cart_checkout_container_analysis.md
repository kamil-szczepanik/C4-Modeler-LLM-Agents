## Overview
The Cart & Checkout Container manages shopping cart sessions, secure payment processing, and order fulfillment for the Online Bookstore. It ensures friction-free conversion while adhering to strict regulatory compliance and high-availability standards.

## Key Elements
* Book Buyer (Primary User)
* Cart & Checkout Container (Amazon ECS/EKS)
* API Gateway (AWS API Gateway)
* AWS Aurora Database (Multi-Region)
* Amazon SQS (Dead-Letter Queues enabled)
* Third-Party Payment Gateway
* Third-Party Shipping APIs
* AWS Secrets Manager & AWS X-Ray

## Relationships
* Book Buyer -> API Gateway: Submits shopping and checkout requests [HTTPS / TLS 1.3]
* API Gateway -> Cart & Checkout Container: Routes validated checkout traffic [mTLS within AWS VPC]
* Cart & Checkout Container -> Third-Party Payment Gateway: Processes tokenized payments [HTTPS REST API]
* Cart & Checkout Container -> Third-Party Shipping APIs: Sends fulfillment data with circuit breaker fallbacks [HTTPS REST API]
* Cart & Checkout Container -> Amazon SQS: Publishes asynchronous order and abandoned cart events [AWS SDK with payload encryption]
* Cart & Checkout Container -> AWS Aurora Database: Persists transactional data and PII [Encrypted SQL / AES-256]

## Technology Stack
* Amazon ECS/EKS: Container orchestration ensuring auto-scaling for 1M MAU resilience.
* Transactional Outbox Pattern: Prevents dual-write failures between database and message queues.
* AWS Secrets Manager: Manages database credentials and API tokens with auto-rotation.
* AWS X-Ray: Provides distributed tracing with strict PII and token redaction.
* Resilience4j / AWS App Mesh: Implements circuit breaking for third-party shipping APIs.

## Rationale
This architecture uses cloud-native resilience and containerization to guarantee 99.95% uptime and sub-2-second performance. It strictly isolates payment scopes and enforces encryption to satisfy GDPR, CCPA, and PCI-DSS mandates without harming conversion rates.