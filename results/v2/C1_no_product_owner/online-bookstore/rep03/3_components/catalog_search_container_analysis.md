## Overview
The Online Bookstore system is a scalable e-commerce platform built to handle high-volume book browsing, searching, and purchasing globally. It features a microservices architecture optimized for sub-second responses, multi-region deployment, and strict compliance.

## Key Elements
- **Users**: Customer, Admin / Support Staff
- **External Systems**: Payment Gateway, Shipping Provider APIs, Tax & Compliance Service, Identity & Access Management, Notification Service
- **Containers**: SPA (React, TypeScript), API Gateway (Amazon API Gateway), Catalog & Search Container, Order & Checkout Container, Recommendations Container, Notification Service Container
- **Catalog & Search Components**: Search Controller, Search Service, Product Query Service, Search Index Client, Catalog Synchronization Worker
- **Data Stores**: Amazon OpenSearch Service, Amazon Aurora PostgreSQL, AWS MSK / Amazon EventBridge, AWS Secrets Manager

## Relationships
- **API Gateway -> Catalog & Search Container**: Routes catalog and search requests [gRPC/REST over VPC internal load balancers with mTLS]
- **Search Controller -> Search Service & Product Query Service**: In-memory [Java Method Calls]
- **Search Service -> Amazon OpenSearch Service**: Keyword and faceted searches [HTTPS]
- **Product Query Service -> Amazon Aurora PostgreSQL**: Retrieves product metadata from read replicas [JDBC/TLS]
- **Catalog Synchronization Worker -> Amazon Aurora PostgreSQL & Amazon OpenSearch Service**: Keeps search indexes eventually consistent [JDBC / HTTPS]

## Technology Stack
- **Backend Framework**: Spring Boot and Spring MVC/Batch for robust enterprise catalog operations.
- **Search Engine**: Amazon OpenSearch Service for high-performance, full-text keyword and faceted search.
- **Database & Messaging**: Amazon Aurora PostgreSQL for reliable relational storage, and AWS MSK / Amazon EventBridge for asynchronous eventing.
- **Cloud Infrastructure**: AWS ECS (Fargate) for container orchestration across us-east-1, eu-west-1, and ap-southeast-1.
- **Resiliency & Security**: Resilience4j for circuit breakers, AWS KMS for encryption-at-keys, and AWS Secrets Manager for secret rotation.

## Rationale
This architecture uses Amazon OpenSearch coupled with Aurora PostgreSQL read-replicas to deliver sub-2s performance under heavy load. Multi-region AWS deployment with strict VPC isolation guarantees 99.95% availability, OWASP mitigations, and GDPR/CCPA compliance.