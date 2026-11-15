## Overview
The Shopping Cart Container manages user shopping cart items, state persistence, and guest-to-authenticated cart merging for the Online Bookstore. It ensures secure, low-latency cart operations while complying with GDPR and CCPA regulations.

## Key Elements
* **Book Buyer:** End-user interacting with the shopping cart via the frontend UI.
* **Shopping Cart Container:** Amazon ECS on AWS Fargate service handling cart business logic and state.
* **Amazon ElastiCache (Redis):** In-memory data store with multi-AZ replication, persistence (AOF/RDB), and AWS KMS encryption-at-rest.
* **Amazon Cognito:** OIDC/OAuth 2.0 identity provider issuing JWTs for user authentication.
* **Amazon SQS/SNS:** Event broker publishing encrypted asynchronous cart and abandonment events.

## Relationships
* **Application Load Balancer (ALB) -> Shopping Cart Container:** Routes validated ingress requests [gRPC over TLS with mTLS via AWS App Mesh].
* **Shopping Cart Container <-> Amazon ElastiCache (Redis):** Persists and merges cart state using atomic Redis Lua scripts [In-transit TLS].
* **Shopping Cart Container -> Amazon SQS/SNS with DLQs:** Publishes pseudonymized cart abandonment and update events [Encrypted AWS KMS channels].

## Technology Stack
* **AWS Fargate (Amazon ECS):** Serverless container runtime providing scalable compute for microservices.
* **Amazon ElastiCache (Redis):** High-performance state management for low-latency (<200ms) cart updates.
* **Amazon Cognito & JWT:** Stateless authentication enforcing strict session validation and authorization.
* **AWS KMS & Secrets Manager:** Cryptographic protection ensuring GDPR/CCPA data privacy compliance.

## Rationale
This architecture guarantees zero data loss and sub-200ms latency via Redis persistence and co-located AWS infrastructure. It securely meets scalability and compliance mandates through container isolation, atomic session merging, and automated data lifecycle policies.