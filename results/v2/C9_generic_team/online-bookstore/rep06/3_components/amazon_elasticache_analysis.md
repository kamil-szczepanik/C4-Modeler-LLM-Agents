## Overview
[A scaled-down Amazon-style online bookstore offering physical and electronic books with recommendations, reviews, and multi-currency support.]

## Key Elements
* Customers
* AWS CloudFront & S3
* AWS API Gateway & BFF
* Amazon ECS/EKS Containers (Catalog, Checkout, Recommendations, Reviews, Compliance Workers)
* Amazon Aurora/RDS
* Amazon ElastiCache (Redis)
* AWS SQS, SNS, & DLQ
* External Systems (Payment Gateways, Shipping APIs, Forex API, Notification Service)

## Relationships
* Customers -> AWS CloudFront & S3: Browses static assets and UI [HTTPS]
* AWS CloudFront & S3 -> AWS API Gateway & BFF: Forwards dynamic requests [HTTPS]
* AWS API Gateway & BFF -> Amazon ECS/EKS Containers: Routes API calls [REST/gRPC]
* AWS API Gateway & BFF -> Amazon ElastiCache: Queries session state and catalog cache [Redis Protocol]
* Amazon ECS/EKS Containers -> Amazon Aurora/RDS: Reads and writes persistent relational data [SQL/TLS]
* Amazon ECS/EKS Containers -> External Systems: Integrates with payments, shipping, forex, and notifications [HTTPS/REST]

## Technology Stack
* AWS Cloud & Serverless Edge: AWS CloudFront and Amazon S3 for global content delivery and static hosting
* API Layer: AWS API Gateway for managed routing and backend-for-frontend architecture
* Compute: Docker containers hosted on Amazon ECS/EKS for scalable microservices
* Database: Amazon Aurora/RDS for reliable relational data storage
* Caching & Session Management: Amazon ElastiCache (Redis) utilizing Cache-Aside pattern, LRU eviction, and Lazy Freeing
* Message Queue & Integration: AWS SQS and SNS with Dead Letter Queues for asynchronous processing

## Rationale
* The multi-region AWS infrastructure with ElastiCache caching layers ensures sub-2-second page loads on 3G and maintains 99.95% availability for 1M MAU.
* Containerized microservices on Amazon ECS/EKS combined with Aurora/RDS and strict security controls satisfy compliance, scalability, and OWASP Top-10 requirements.