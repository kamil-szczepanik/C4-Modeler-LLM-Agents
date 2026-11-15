## Overview
[The Online Bookstore system provides scalable e-commerce browsing, checkout, and recommendations.]
[The Shipping & Payment Integration Worker securely processes asynchronous orders via serverless infrastructure.]

## Key Elements
* SQS Event Consumer (AWS Lambda Handler, Python/Java)
* Idempotency Manager (Amazon DynamoDB Global Tables with 7-day TTL)
* Payment Processor Client (HTTP Client)
* Fulfillment Integrator (HTTP Client)
* DLQ Handler (Amazon SQS Dead-Letter Queue)
* Audit Event Emitter (Amazon EventBridge)
* Secrets & Currency Context Injector (AWS Lambda Powertools)

## Relationships
* Checkout & Order Container -> SQS Event Consumer [AWS SQS]
* Payment Processor Client -> Payment Gateway [HTTPS]
* Fulfillment Integrator -> Third-Party Shipping API [HTTPS]
* Audit Event Emitter -> Amazon EventBridge [AWS SDK]
* Secrets & Currency Context Injector -> AWS Secrets Manager [HTTPS/AWS SDK]

## Technology Stack
* AWS Lambda: Serverless compute for asynchronous background processing
* Amazon SQS: Message queue with DLQ for reliable decoupling and retry handling
* Amazon DynamoDB Global Tables: Distributed state store for multi-region idempotency enforcement
* AWS Secrets Manager: Dynamic credential management with automatic rotation
* Amazon EventBridge: Event bus for publishing sanitized audit logs

## Rationale
[Asynchronous serverless workers protect core checkout availability and prevent gateway timeouts under high traffic.]
[Tokenization, KMS encryption, and strict VPC egress controls ensure full GDPR, CCPA, and OWASP compliance.]