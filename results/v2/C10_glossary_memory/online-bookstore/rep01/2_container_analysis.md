## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. It scales across AWS regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`) while ensuring high availability and strict GDPR/CCPA compliance.

## Key Elements
- Book Shopper, Reviewer, Store Administrator (Personas)
- Web Frontend & Admin Portal (React SPAs)
- Amazon API Gateway
- Core Containers: Catalogue Service (Node.js/Express), Order & Checkout Service (Go), Review Service (Python/FastAPI), Admin Service (Node.js/Express), Recommendation Integration Service (Node.js)
- Data Stores: Amazon Aurora PostgreSQL, Amazon DynamoDB
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Amazon SES, ML Recommendation Engine

## Relationships
- Shoppers/Admins -> Online Bookstore: HTTPS via AWS CloudFront
- API Gateway -> Core Containers: HTTPS/REST with JWT validation
- Online Bookstore -> Payment Gateway: HTTPS/REST
- Online Bookstore -> Third-Party Shipping APIs: HTTPS/REST and Webhooks
- Online Bookstore -> Identity Provider: OAuth2/OIDC
- Online Bookstore -> Email Service: Amazon SES
- Online Bookstore -> ML Recommendation Engine: HTTPS/REST and Amazon SQS/SNS

## Technology Stack
- Hosting & Orchestration: AWS ECS (Fargate) managed via Terraform and ArgoCD for reproducible zero-downtime deployments
- Compute & Frameworks: React, Node.js/Express, Go (for transactional checkout safety), Python/FastAPI
- Data & Search: Amazon Aurora PostgreSQL (multi-region relational data), Amazon DynamoDB (low-latency carts), Amazon OpenSearch (sub-second keyword search)
- Messaging & Integration: Amazon EventBridge, Amazon SQS/SNS for decoupled event-driven communication
- Security & Observability: AWS IAM, AWS Secrets Manager, AWS KMS, AWS App Mesh (mTLS), Amazon CloudWatch, AWS X-Ray, Prometheus/Grafana

## Rationale
Isolating critical boundaries like the Go-based Order & Checkout Service and OpenSearch-backed Catalogue Service guarantees 99.95% availability and sub-second performance under peak 1M MAU traffic. Multi-region ECS Fargate deployment combined with DynamoDB global tables and strict AWS security controls ensures robust scalability, disaster recovery, and compliance.