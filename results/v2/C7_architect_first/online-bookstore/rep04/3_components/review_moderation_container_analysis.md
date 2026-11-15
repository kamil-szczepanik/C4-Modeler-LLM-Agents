## Overview
The Review Moderation Container is a microservice within the Online Bookstore architecture responsible for automated and human-in-the-loop review moderation. It ensures catalog trust and GDPR/CCPA compliance by processing, filtering, and auditing user-submitted reviews.

## Key Elements
- Moderation API Controller (Node.js/Express, Amazon ECS on AWS Fargate)
- Moderation Queue Consumer (Node.js/Express, Amazon ECS on AWS Fargate)
- Auto-Moderator Engine (Node.js/Express, Amazon ECS on AWS Fargate)
- Moderator Dashboard Service (Node.js/Express, Amazon ECS on AWS Fargate)
- Moderation Data Access Layer (Node.js/Express, Amazon ECS on AWS Fargate)
- Amazon SQS (AWS Ingestion Queue)
- Amazon Aurora PostgreSQL (AWS Multi-Region Database)
- Amazon SNS (AWS Notification Service)

## Relationships
- Amazon API Gateway -> Moderation API Controller [gRPC over HTTP/2 via mTLS]
- Moderation API Controller -> Amazon SQS [HTTPS/AWS SDK]
- Moderation Queue Consumer -> Auto-Moderator Engine [In-process]
- Moderator Dashboard Service -> Amazon Aurora PostgreSQL [TCP/PostgreSQL wire protocol via TLS 1.3]
- Review Moderation Container -> Amazon SNS [Amazon SNS/SQS]

## Technology Stack
- Amazon ECS on AWS Fargate: Serverless container orchestration for elastic scalability without infrastructure management.
- Node.js/Express: Lightweight runtime for fast asynchronous API routing and queue consumption.
- Amazon SQS: Message queue for asynchronous decoupling and protection against NLP processing traffic spikes.
- Amazon Aurora PostgreSQL: Relational database with AWS KMS encryption for secure review state and audit log persistence.
- AWS Secrets Manager & IAM: Secure credential storage and least-privilege task role access control.

## Rationale
This event-driven, containerized architecture scales elastically to handle 1M MAU while maintaining high availability (99.95% uptime). Asynchronous ingestion via SQS safeguards backend NLP processing against resource-exhaustion attacks, ensuring resilient and secure moderation workflows.