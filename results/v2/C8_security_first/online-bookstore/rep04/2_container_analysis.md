## Overview
An Amazon-style online bookstore delivering physical and electronic books with recommendations, reviews, and secure global checkout. Built on AWS across multi-region infrastructure to support 1 million MAU with high availability.

## Key Elements
- Shopper and Administrator (Users)
- Frontend App (React SPA served via Amazon CloudFront/S3)
- Amazon API Gateway (Single entry point and rate limiter)
- Backend Microservices (Node.js Catalog Service, Java/Spring Boot Order & Checkout Service, Python/FastAPI Recommendation Service on AWS ECS Fargate)
- Data Persistence (Amazon Aurora PostgreSQL & Amazon OpenSearch)
- External Systems (Third-Party Payment Gateway, Shipping Provider, Currency Exchange Service, Recommendation Engine)

## Relationships
- Shopper to Frontend App: HTTPS/JSON via browser
- Frontend App to Amazon API Gateway: HTTPS/JSON with edge currency routing
- Amazon API Gateway to Backend Services: HTTPS with JWT validation via AWS App Mesh
- Internal Microservices to Microservices: gRPC over mTLS
- Backend Services to Data Persistence: TLS with IAM authentication
- Recommendation Service to Third-Party Recommendation Engine: HTTPS API calls with Envoy circuit breakers

## Technology Stack
- Cloud Provider: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region scale
- Compute: AWS ECS Fargate for elastic container management
- Database: Amazon Aurora PostgreSQL (multi-region) for transactional integrity and Amazon OpenSearch for keyword search
- Security: AWS Cognito for OAuth 2.0/JWTs, AWS App Mesh for mTLS, AWS Secrets Manager for secrets, AWS KMS for encryption at rest
- DevOps/Observability: ArgoCD for GitOps, AWS CodeDeploy for blue/green deployments, ADOT with Prometheus and Grafana for telemetry

## Rationale
Microservices on ECS Fargate combined with multi-region Aurora PostgreSQL ensure horizontal scalability for 1M MAU and 99.95% uptime. Strict subnet isolation and mTLS enforce GDPR/CCPA compliance and OWASP Top-10 mitigations while maintaining sub-2-second page loads globally.