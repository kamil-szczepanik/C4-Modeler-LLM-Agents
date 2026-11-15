## Overview
[The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books, featuring recommendations and reviews. It utilizes a resilient, event-driven messaging architecture on AWS to ensure high availability and GDPR/CCPA compliance.]

## Key Elements
- [Event Publisher / SNS Topics (AWS SNS)]
- [Subscription Queues / SQS Buffers (AWS SQS)]
- [Payload Sanitizer Middleware (Claims-Check pattern)]
- [Schema Registry & Validation Middleware (AWS Glue Schema Registry)]
- [DLQ Routing & Lambda Redrive Component (AWS Lambda)]
- [Order & Checkout Service, Catalogue & Search Service, Review & Moderation Service, Notification Service]

## Relationships
- [Order & Checkout Service -> Event Publisher / SNS Topics: Publishes checkout domain events using JSON over HTTPS]
- [Catalogue & Search Service -> Event Publisher / SNS Topics: Publishes catalogue events using JSON over HTTPS]
- [Review & Moderation Service -> Event Publisher / SNS Topics: Publishes moderation events using JSON over HTTPS]
- [Subscription Queues / SQS Buffers -> Notification Service: Dispatches transactional alerts using REST/JSON over HTTPS]

## Technology Stack
- [AWS SNS & SQS: Provides asynchronous event-driven messaging and decoupling for high scalability]
- [AWS Lambda: Powers automated redrive and error handling for dead-letter queues]
- [AWS Glue Schema Registry: Enforces strict contract versioning using JSON Schema]
- [AWS KMS & TLS 1.3: Ensures data encryption in transit and server-side encryption at rest]
- [Terraform / AWS CDK: Automates infrastructure provisioning and drift detection]

## Rationale
[This event-driven architecture guarantees 99.95% uptime and high scalability for 1M MAU while securely decoupling core microservices. Additionally, the Claims-Check pattern and strict AWS IAM controls enforce GDPR and CCPA compliance without introducing performance bottlenecks.]