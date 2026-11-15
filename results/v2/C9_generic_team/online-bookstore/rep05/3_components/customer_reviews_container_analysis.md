## Overview
The Customer & Reviews Container manages customer profiles, account settings, and book reviews within the Online Bookstore platform. It ensures high availability, strict security, and GDPR/CCPA compliance across global AWS regions.

## Key Elements
* **Customer Profile Domain**: Manages strict PII and account settings.
* **Reviews Domain**: Manages public book reviews and 5-star ratings.
* **Dedicated Data Store**: Amazon DynamoDB with global tables and regional PII partitioning.
* **Background Worker Container**: Executes data retention, anonymization, and Saga workflows.
* **API Gateway**: Enforces rate limiting, Content Security Policy (CSP), and request routing.

## Relationships
* **Web Application/API Gateway -> Customer & Reviews Container**: Manages customer profile and review interactions [gRPC/REST over TLS].
* **Customer & Reviews Container -> Amazon DynamoDB**: Persists profile and review data [AWS SDK over TLS].
* **Customer & Reviews Container -> Background Worker Container**: Publishes asynchronous events [AWS SQS/SNS].

## Technology Stack
* **AWS ECS/EKS**: Container orchestration for scalable service deployment.
* **Amazon DynamoDB**: NoSQL data store with global tables for low-latency review reads and regional residency for PII.
* **AWS X-Ray**: Distributed tracing for endpoint monitoring.
* **Pact**: Contract testing framework for interface validation.

## Rationale
CQRS and regional data partitioning satisfy global performance and GDPR requirements while protecting user privacy. Decoupled internal domains and managed AWS infrastructure ensure 99.95% uptime and seamless scaling.