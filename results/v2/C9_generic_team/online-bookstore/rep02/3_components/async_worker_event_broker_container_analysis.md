## Overview
The Online Bookstore is a scaled-down e-commerce platform built on AWS to support global book sales, reviews, and recommendations. It leverages a resilient event-driven architecture to ensure high availability, scalability, and seamless integration with external partners.

## Key Elements
- Customers
- API Gateway Container
- Frontend Container
- Core Domain Containers
- Integration / Anti-Corruption Layer (ACL) Container
- Async Worker / Event Broker Container
- Caching/Session Container (Redis)
- Background Job Scheduler Container
- AWS MSK / Amazon EventBridge, AWS Glue Schema Registry, Amazon S3
- Third-Party Shipping and Payment Services

## Relationships
- Customers -> API Gateway Container: HTTPS / REST / gRPC
- API Gateway Container -> Core Domain Containers: REST / gRPC
- Core Domain Containers -> Async Worker / Event Broker Container: Publish/Subscribe messaging using CloudEvents and W3C Trace Context headers
- Async Worker / Event Broker Container -> Amazon S3: Out-of-band large payload storage via S3 URIs
- Async Worker / Event Broker Container -> Third-Party Shipping Services: HTTPS with circuit breakers and token-bucket rate limiting

## Technology Stack
- AWS MSK / Amazon EventBridge: Managed event streaming for high availability across multi-region deployments
- CloudEvents & AWS Glue Schema Registry: Standardized event messaging with strict backward-compatibility rules
- Redis: Caching, session management, and idempotency key storage with defined TTLs
- Amazon S3: Out-of-band storage for large event payloads
- W3C Trace Context: Distributed tracing headers for end-to-end request observability

## Rationale
This architecture utilizes managed AWS services and decoupled asynchronous processing via CloudEvents to meet the 99.95% uptime requirement and scale effortlessly to 1M MAU. Built-in patterns like circuit breakers, DLQs, and idempotency guarantees protect fragile third-party integrations and ensure robust data consistency across regions.