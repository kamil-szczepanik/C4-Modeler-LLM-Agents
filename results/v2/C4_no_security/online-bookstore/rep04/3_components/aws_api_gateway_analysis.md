## Overview
An AWS-hosted online bookstore delivering a secure, multi-currency e-commerce platform with catalog browsing, recommendations, and compliance. It is engineered to support 1 million MAU with high availability.

## Key Elements
- Shopper & Customer Support Agent (Users)
- AWS Route 53 (DNS & Latency-Based Routing)
- AWS CloudFront & Amazon S3 (CDN & Static Content)
- Single Page Application (React, TypeScript)
- AWS API Gateway (Amazon API Gateway v2/HTTP API with Authorizer, Throttling, and Routing components)
- Catalog, Order & Checkout, User & Compliance, Notification Services, & Recommendation Worker (Spring Boot/Node.js on Amazon ECS/Fargate)
- Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis, AWS SQS/SNS

## Relationships
- Single Page Application -> AWS API Gateway: Communicates via HTTPS REST/JSON and gRPC-Web over HTTP/2
- AWS API Gateway -> Backend ECS/Fargate Services: Routes via AWS VPC Link using gRPC over TLS
- AWS Route 53 -> AWS CloudFront: Resolves global client traffic across regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`)

## Technology Stack
- Amazon API Gateway: Edge routing, rate-limiting, and OAuth2/JWT token validation
- Amazon ECS/Fargate: Container orchestration for backend microservices
- gRPC over TLS / HTTP/2: Low-latency internal service communication via AWS VPC Link
- Terraform / AWS CDK: Infrastructure as Code for multi-region deployments
- Amazon CloudWatch & AWS X-Ray: Distributed tracing and 429/5xx metric alerting

## Rationale
This architecture uses serverless edge routing and containerized microservices to guarantee 99.95% uptime and sub-2-second page loads under peak loads. Multi-region AWS deployment ensures strict GDPR and CCPA compliance for international shoppers.