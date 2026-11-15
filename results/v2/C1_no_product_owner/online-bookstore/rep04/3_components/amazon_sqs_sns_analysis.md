## Overview
The Online Bookstore system is a scalable, multi-region e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. It uses an AWS-based asynchronous messaging architecture to ensure high availability, decoupling, and regulatory compliance.

## Key Elements
- **Order Events SNS Topic**: Amazon SNS fan-out broker utilizing HTTPS and IAM.
- **Checkout SQS Queue**: Amazon SQS Standard queue for buffering checkout orders.
- **Shipping SQS FIFO Queue**: Amazon SQS FIFO queue for strictly ordered third-party shipping payloads.
- **Processing DLQs**: Amazon SQS Dead Letter Queues capturing poisoned messages after max receives.
- **Event Publisher Component**: AWS SDK for JavaScript embedded in the Core E-Commerce Service.
- **Subscription Filter Component**: SNS Subscription Filters routing messages conditionally.

## Relationships
- **Core E-Commerce Service -> Order Events SNS Topic**: Publishes standardized JSON event payloads via AWS SDK (HTTPS/TLS 1.2+).
- **Order Events SNS Topic -> Checkout SQS Queue & Shipping SQS FIFO Queue**: Routes messages via HTTPS using SNS Subscription Filters.
- **Checkout SQS Queue & Shipping SQS FIFO Queue -> Background Worker Service**: Consumes asynchronous messages using Long Polling (TLS/IAM).
- **Queues/Topics -> AWS KMS**: Encrypts messages at rest using customer-managed keys with strict IAM policies.

## Technology Stack
- **Amazon SQS / SNS**: Core messaging backbone for high availability (99.95% SLA) and decoupled processing.
- **AWS KMS**: Customer-managed keys ensuring data-at-rest encryption and annual automated rotation.
- **AWS SDK for JavaScript**: Standardizes JSON event envelopes and injects X-Ray tracing headers.
- **Terraform / AWS CDK**: Infrastructure-as-Code for idempotent multi-region deployments.
- **Amazon CloudWatch**: Monitors queue depth and message age with automated alarms and anomaly detection.

## Rationale
This asynchronous architecture isolates core checkout and shipping workflows from flaky third-party APIs, protecting system scalability and meeting performance goals. Stricting payloads to resource IDs (`order_id`) without raw PII ensures GDPR/CCPA compliance across multi-region deployments.