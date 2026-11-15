## Overview
The Online Bookstore system is a scalable e-commerce platform built to handle physical and electronic book sales, customer reviews, and personalized recommendations. It provides a highly available, secure, and performant shopping experience across multiple global regions.

## Key Elements
- Customers (Users)
- AWS CloudFront & S3 (Static Content Delivery)
- AWS API Gateway & BFF (Routing & Request Aggregation)
- Catalog Container (Amazon ECS/EKS)
- Checkout Container (Amazon ECS/EKS)
- Recommendations Container (Amazon ECS/EKS)
- Reviews Container (Amazon ECS/EKS)
- Compliance Workers (Amazon ECS/EKS)
- Amazon Aurora / RDS (Primary Database)
- Amazon ElastiCache (Redis Caching & Session State)
- AWS SQS, SNS, & DLQ (Asynchronous Messaging)
- External Systems (Payment Gateways, Shipping APIs, Forex API, Notification Service)

## Relationships
- Customers -> AWS CloudFront & S3: Fetches static assets [HTTPS]
- Customers -> AWS API Gateway & BFF: Interacts with storefront services [HTTPS/REST]
- AWS API Gateway & BFF -> Amazon ElastiCache: Queries session state and caches [Redis Protocol]
- AWS API Gateway & BFF -> Catalog/Checkout/Recommendations/Reviews Containers: Routes backend requests [HTTPS/REST]
- Backend Containers -> Amazon Aurora / RDS: Reads and writes persistent data [SQL/TLS]
- Backend Containers -> AWS SQS/SNS: Publishes and consumes asynchronous events [AMQP/HTTPS]

## Technology Stack
- **Cloud Provider:** AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability.
- **Compute:** Docker containers hosted on Amazon ECS/EKS for microservices isolation and scalability.
- **API Management:** AWS API Gateway & BFF for routing, rate limiting, and request aggregation.
- **Security & Edge:** AWS WAF and TLS Termination at the edge for OWASP Top-10 mitigation and encryption.
- **Database:** Amazon Aurora / RDS for relational data storage and multi-currency support.
- **Caching:** Amazon ElastiCache (Redis) for low-latency session management and response caching.
- **Messaging:** AWS SQS, SNS, and DLQ for asynchronous event-driven communication.

## Rationale
This architecture uses cloud-native AWS services and a containerized microservices pattern to guarantee 99.95% availability, support 1 million MAU, and maintain sub-2-second page loads on 3G. Edge caching, strict security controls, and multi-region deployment satisfy strict performance, scalability, and GDPR/CCPA compliance constraints.