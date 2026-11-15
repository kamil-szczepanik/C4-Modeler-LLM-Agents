## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed for purchasing physical and electronic books with recommendations and reviews. It provides a highly available, secure, and scalable retail environment deployed across AWS.

## Key Elements
- **Customer & Store Administrator**: Primary users interacting with the platform.
- **Single Page Application (SPA)**: Built with React, TypeScript, Amazon S3, and Amazon CloudFront.
- **API Gateway**: Managed via Amazon API Gateway.
- **Backend Microservices**: Catalog Service (Go, Amazon Aurora, Amazon OpenSearch), Order & Checkout Service (Node.js, Amazon Aurora, Amazon ElastiCache), Recommendation Service (Python, FastAPI, Amazon DocumentDB), and Customer Review Service (Node.js, Amazon Aurora).
- **Message Broker Components**: Event Topic Router (Amazon SNS), Execution Queues (Amazon SQS), Dead Letter Queue Handler (Amazon SQS DLQ), Event Schema Validator (JSON Schema), and Message Retry & Backoff Controller (SQS Native Attributes).
- **External Systems**: Payment Gateway, Third-Party Shipping Provider API, Notification Service, Identity Provider / OAuth 2.0 Service, and Currency Exchange Rate Service.

## Relationships
- **Catalog Service / Order Service** -> **Event Schema Validator**: Validates published payloads [HTTPS / AWS SDK].
- **Event Topic Router** -> **Execution Queues**: Fan-out routing [AWS SNS to SQS subscription, HTTPS].
- **Execution Queues** -> **Recommendation Service / Notification Service**: Consumes asynchronous events [Polling, SQS SDK].
- **Execution Queues** -> **Message Retry & Backoff Controller**: Manages redrive policies [SQS Native Config].

## Technology Stack
- **Frontend**: React, TypeScript for responsive client-side rendering.
- **CDN & Storage**: Amazon CloudFront and Amazon S3 for low-latency static asset delivery.
- **API Management**: Amazon API Gateway for secure routing and throttling.
- **Databases**: Amazon Aurora (relational), Amazon OpenSearch (search), Amazon DocumentDB (NoSQL), and Amazon ElastiCache (caching).
- **Messaging**: Amazon SNS and Amazon SQS for asynchronous, decoupled event-driven communication.

## Rationale
This architecture utilizes serverless and managed AWS services to guarantee 99.95% uptime and seamless scaling for 1 million monthly active users. Decoupling services via Amazon SNS/SQS ensures high performance and resilience under load.