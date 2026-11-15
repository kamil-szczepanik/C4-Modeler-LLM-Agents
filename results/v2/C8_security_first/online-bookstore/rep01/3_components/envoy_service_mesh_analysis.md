## Overview
An enterprise-grade Online Bookstore built on AWS serving 1M MAU across three global regions. It delivers scalable e-commerce capabilities including catalog browsing, secure checkout, and personalized recommendations.

## Key Elements
* **Users:** Customer, Book Author / Publisher, Customer Support Agent, Shipping Partner, Site Administrator / Content Manager
* **Frontend:** Single-Page Application (React hosted on Amazon S3 and Amazon CloudFront)
* **Ingress & Mesh:** AWS API Gateway, Envoy Service Mesh (Envoy, SPIFFE/SPIRE)
* **Microservices:** Catalog Service, Order & Checkout Service, Recommendation Service, Customer Service, Admin & Support Service (all built on Node.js/Java/Python/Go, deployed on AWS ECS on Fargate)
* **Data & Messaging:** Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon S3, Amazon EventBridge, Amazon SQS
* **External Systems:** Payment Gateway, Shipping Provider APIs, Notification Service, Currency Exchange API

## Relationships
* **Single-Page Application -> AWS API Gateway:** Routes frontend client requests over HTTPS
* **AWS API Gateway -> Envoy Service Mesh:** Forwards edge-authenticated ingress traffic via gRPC over mTLS
* **Envoy Service Mesh -> ECS Microservices:** Routes internal inter-service traffic via gRPC over mTLS with enforced RBAC and `ext_authz` (OPA)
* **Microservices -> Amazon Aurora PostgreSQL / Amazon ElastiCache:** Persists transactional and cached data secured via AWS KMS
* **Microservices -> Amazon EventBridge / Amazon SQS:** Publishes and consumes asynchronous domain events secured via AWS KMS

## Technology Stack
* **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global availability
* **Compute & Containers:** AWS ECS on Fargate for serverless container orchestration without infrastructure overhead
* **Service Mesh & Security:** Envoy and SPIFFE/SPIRE for automated mTLS workload identity, strict fail-closed policies, and W3C trace propagation
* **Database & Caching:** Amazon Aurora PostgreSQL for relational persistence with AWS KMS encryption, and Amazon ElastiCache (Redis) for low-latency caching
* **Asynchronous Messaging:** Amazon EventBridge and Amazon SQS for decoupled event-driven communication

## Rationale
This architecture uses AWS ECS Fargate and Envoy Service Mesh to effortlessly scale and handle 1M MAU while guaranteeing 99.95% uptime and sub-2-second page loads. Automated mTLS via SPIFFE/SPIRE and strict data encryption satisfy global GDPR and CCPA compliance mandates.