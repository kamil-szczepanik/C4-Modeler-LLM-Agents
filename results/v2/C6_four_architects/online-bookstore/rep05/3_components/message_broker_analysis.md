## Overview
The Online Bookstore is a globally distributed, Amazon-style e-commerce platform designed to provide resilient browsing, secure checkout, reviews, and personalized recommendations. It handles high-volume traffic across multiple AWS regions while maintaining strict compliance and high availability.

## Key Elements
- **Users**: Customer
- **External Systems**: Stripe/PayPal, FedEx/UPS, Auth0/AWS Cognito, SendGrid/AWS SES, Avalara/TaxJar
- **Containers**: Single Page Application (React, TypeScript), API Gateway (AWS API Gateway), Catalog Service (Node.js, Express), Order & Checkout Service (Spring Boot), Recommendation Service (Python, FastAPI), Review & Notification Service (Node.js), Message Broker (Amazon SNS, Amazon SQS), Aurora PostgreSQL Database, OpenSearch Service, Redis Cache
- **Message Broker Components**: Event Publisher (Amazon SNS), Event Queue Manager (Amazon SQS), Dead Letter Queue Manager (Amazon SQS DLQ), Event Payload Encryption Component (AWS KMS), Schema Validator (JSON Schema), Message Routing & Filtering Router (Amazon SNS Filter Policies)

## Relationships
- **Order & Checkout Service -> Event Publisher**: Publishes order lifecycle events via HTTPS (AWS SDK)
- **Event Publisher -> Message Routing & Filtering Router**: Evaluates filter attributes during message broadcast via Amazon SNS
- **Message Routing & Filtering Router -> Event Queue Manager**: Forwards matched events to targeted SQS queues
- **Event Queue Manager -> DLQ Manager**: Routes unprocessable messages after max retry attempts via AWS SQS redrive policy
- **Event Queue Manager -> Review & Notification Service / Recommendation Service / Catalog Service**: Delivers queued events via HTTP long-polling (AWS SDK)
- **Event Publisher / Event Queue Manager -> Event Payload Encryption Component**: Encrypts and decrypts sensitive message payloads via AWS KMS API

## Technology Stack
- **Compute & Orchestration**: AWS Lambda, Amazon S3, Amazon CloudFront for hosting and stateless routing
- **Messaging & Eventing**: Amazon SNS for pub/sub broadcasting, Amazon SQS for queuing and buffering, Amazon SNS Filter Policies for selective routing
- **Security & Compliance**: AWS KMS for message payload encryption at rest, JSON Schema for event validation
- **Databases & Caching**: Amazon Aurora PostgreSQL for relational data, Amazon OpenSearch Service for search, Amazon Redis for caching

## Rationale
This architecture leverages managed AWS services across multiple regions to easily scale past 1M MAU while guaranteeing 99.95% uptime. Asynchronous messaging via SNS and SQS combined with robust encryption and schema validation ensures strict GDPR/CCPA compliance and high-performance cross-service communication.