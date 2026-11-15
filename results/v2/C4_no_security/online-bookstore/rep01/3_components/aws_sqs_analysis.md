## Overview
[An Amazon-style global online bookstore providing multi-currency browsing, secure checkout, and real-time recommendations for 1M MAU.]
[AWS SQS powers high-throughput asynchronous messaging and strictly ordered payment workflows across three global regions with zero data loss.]

## Key Elements
- Checkout & Order Container
- Catalog & Search Container
- Recommendation Container
- Amazon SQS Standard Queues
- Amazon SQS FIFO Queues
- Amazon SQS Dead-Letter Queues (DLQs)
- Notification & Logging Container
- Customer Support Agents & Store Administrators

## Relationships
- Checkout & Order -> SQS FIFO Queue: Sends transaction events via AWS SDK v2 (HTTPS) using message group IDs
- Catalog & Search / Recommendation -> SQS Standard Queues: Publishes event notifications via AWS SDK v2 (HTTPS)
- AWS SQS DLQ -> Notification / Logging Container: Triggers processing via long-polling (HTTPS) for failed payloads

## Technology Stack
- Amazon SQS Standard & FIFO: Chosen for high-throughput asynchronous communication and strictly ordered checkout operations
- AWS SDK v2: Utilized for secure, reliable container-to-queue communication over HTTPS
- AWS KMS: Implemented for server-side encryption to meet GDPR and CCPA compliance
- Terraform / AWS CDK: Used for infrastructure-as-code provisioning and multi-region deployment

## Rationale
[This messaging architecture decouples core transactional services to guarantee 99.95% uptime and prevent inventory race conditions during flash sales.]
[Strict FIFO queues, DLQs, and visibility timeouts ensure exact-once processing and zero lost orders under heavy peak loads.]