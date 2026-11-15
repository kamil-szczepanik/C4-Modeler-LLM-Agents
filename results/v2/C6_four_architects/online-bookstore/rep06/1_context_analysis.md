## Overview
A scaled-down Amazon-style e-commerce site for physical and electronic books with recommendations and reviews. Hosted on AWS across multi-regions to serve 1M MAU with 99.95% uptime.

## Key Elements
* **Actors:** Customer, Store Administrator
* **External Systems:** Payment Gateway (Stripe/PayPal), Third-Party Shipping API (FedEx/UPS), Notification Service (AWS SES), Currency Exchange Rate API
* **Containers:** React SPA (CloudFront/S3), AWS API Gateway, ECS Fargate Microservices, Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon OpenSearch, Amazon SQS/SNS

## Relationships
* Customer -> React SPA [HTTPS]
* React SPA -> AWS API Gateway [HTTPS/JSON]
* AWS API Gateway -> ECS Fargate Microservices [HTTP/2 / gRPC]
* ECS Microservices -> Amazon Aurora PostgreSQL [TCP/SQL]
* ECS Microservices -> Amazon ElastiCache [RESP]
* ECS Microservices -> Payment Gateway & Shipping API [HTTPS/REST]
* ECS Microservices -> Amazon SQS/SNS [TLS/HTTPS]

## Technology Stack
* **Frontend:** React SPA hosted on AWS S3 with CloudFront CDN for global sub-2s page loads.
* **API Layer:** AWS API Gateway for TLS termination, rate limiting, and JWT validation.
* **Backend:** Go/Node.js microservices on Amazon ECS (Fargate) using gRPC for internal inter-service communication.
* **Data & Search:** Amazon Aurora PostgreSQL (Multi-Region) for transactions, Amazon ElastiCache (Redis) for sessions/caching, and Amazon OpenSearch for fast catalogue search.
* **Integration:** Amazon SQS/SNS for asynchronous event-driven workflows.

## Rationale
AWS multi-region deployment across us-east-1, eu-west-1, and ap-southeast-1 guarantees 99.95% uptime and scalability for 1M MAU. Managed services like ECS, Aurora, and CloudFront ensure low latency (<2s on 3G) and robust security.