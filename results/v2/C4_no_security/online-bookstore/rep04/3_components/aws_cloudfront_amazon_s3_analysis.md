## Overview
[An Amazon-style global online bookstore delivering physical and electronic books, reviews, and recommendations to 1M MAU. It features multi-currency support, robust security, and high availability across multiple AWS regions.]

## Key Elements
* Shopper
* Catalog Manager / Administrator
* AWS CloudFront & Amazon S3
* Single Page Application (React, TypeScript)
* AWS API Gateway
* Catalog Service, Order & Checkout Service, User & Compliance Service, Notification Service, Recommendation Worker (Spring Boot / Node.js on Amazon ECS/Fargate)
* Amazon RDS PostgreSQL & Amazon DynamoDB
* Amazon ElastiCache (Redis)
* AWS SQS/SNS with DLQs
* AWS WAF & AWS Shield Standard

## Relationships
* Shopper & Catalog Manager -> AWS CloudFront & Amazon S3: Accesses SPA via HTTPS [TLS 1.3]
* CloudFront Distribution -> Amazon S3 Bucket: Fetches static assets via HTTPS [IAM OAC]
* SPA -> AWS API Gateway: Makes dynamic API calls via HTTPS [REST/JSON]
* API Gateway -> ECS/Fargate Containers: Routes traffic via internal VPC network [HTTP/gRPC]

## Technology Stack
* AWS CloudFront & S3: Global content delivery and static web hosting for performance and scalability
* React & TypeScript: Modern, responsive single-page application client framework
* Spring Boot / Node.js on Amazon ECS/Fargate: Microservices backend container runtime
* Amazon RDS PostgreSQL & DynamoDB: Relational and NoSQL data persistence layers
* Amazon ElastiCache (Redis): In-memory caching for session and catalogue acceleration
* AWS WAF & Shield: Security, DDoS mitigation, and OWASP Top-10 protection

## Rationale
[This cloud-native AWS architecture leverages edge caching and containerized microservices to guarantee sub-2-second page loads, 99.95% uptime, and seamless global scaling. Strict adherence to security controls, encryption, and automated deployment pipelines ensures full regulatory compliance and operational resilience.]