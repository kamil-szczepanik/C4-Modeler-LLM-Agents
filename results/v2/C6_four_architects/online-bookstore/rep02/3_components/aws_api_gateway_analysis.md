## Overview
The Online Bookstore system uses a scalable, cloud-native e-commerce architecture on AWS to provide book catalog browsing, secure checkout, reviews, and recommendations. It is designed to handle 1 million MAU globally while meeting strict security, performance, and compliance requirements.

## Key Elements
* **Users:** Customer, Admin/Content Manager
* **External Systems:** Payment Gateway, Third-Party Shipping API, Email/Notification Service, External Identity Provider, Tax Calculation Service
* **Containers:** AWS Route 53 & Amazon CloudFront, Frontend SPA (React, TypeScript), BFF Container (Next.js, Amazon ECS/Fargate), AWS API Gateway, Compliance/Audit Lambda, Core E-Commerce Service (Spring Boot), Recommendation Engine (FastAPI), Search & Discovery (Amazon OpenSearch), Notification Worker, Amazon Aurora Global Database, Amazon DynamoDB, Amazon ElastiCache, Amazon MSK, AWS Glue & Athena
* **API Gateway Components:** WAF & Security Shield, Route Validator & Authorizer, Rate Limiter, Transformation & Validation, Request Router, Monitoring & Logging

## Relationships
* **Frontend SPA -> BFF Container:** Proxies requests [HTTPS/REST]
* **BFF Container -> AWS API Gateway:** Proxies requests [HTTPS/REST (JSON over HTTP/2)]
* **AWS API Gateway -> Core E-Commerce Service:** Routes business requests [HTTPS over AWS VPC Links]
* **AWS API Gateway -> Recommendation Engine:** Routes recommendation requests [HTTPS over AWS VPC Links]
* **AWS API Gateway -> Search & Discovery:** Routes search queries [HTTPS over AWS VPC Links]
* **AWS API Gateway -> Identity Provider:** Authenticates users [Secure REST/HTTPS]

## Technology Stack
* **Cloud Infrastructure:** AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for multi-region high availability.
* **API Management:** AWS API Gateway with AWS WAF for edge routing, security, and OWASP Top-10 mitigation.
* **Compute:** Amazon ECS/Fargate and AWS Lambda for containerized microservices and serverless tasks.
* **Databases & Caching:** Amazon Aurora Global Database, Amazon DynamoDB, and Amazon ElastiCache (Redis) for low-latency data access.
* **Messaging & Search:** Amazon MSK (Apache Kafka) for event streaming and Amazon OpenSearch for catalog search.

## Rationale
This microservices-based, multi-region AWS architecture ensures 99.95% uptime and rapid page loads under 2 seconds. Using managed serverless and containerized services decouples components to effortlessly scale for 1 million MAU while enforcing strict security standards.