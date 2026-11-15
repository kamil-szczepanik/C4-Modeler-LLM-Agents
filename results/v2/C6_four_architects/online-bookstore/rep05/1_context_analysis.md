## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to provide browsing, searching, purchasing, reviews, and personalized recommendations for physical and electronic books. It targets a global audience across three AWS regions while ensuring GDPR and CCPA compliance, multi-currency support, and high availability.

## Key Elements
* **Customer**: End-user browsing, reviewing, and purchasing books via web or mobile.
* **CDN / DNS Provider**: AWS Route 53 and CloudFront serving global static assets.
* **Web Application (SPA)**: React single-page application hosted in Amazon S3.
* **API Gateway**: AWS API Gateway and ALB managing ingress, TLS termination, and rate limiting.
* **Core E-commerce API**: Go/Node.js service on Amazon ECS Fargate managing catalog, cart, and orders.
* **Recommendation & Review Service**: Python/FastAPI service on Amazon ECS Fargate handling 5-star ratings and recommendations.
* **Background Worker**: ECS Fargate container processing asynchronous domain events.
* **Databases & Caches**: Amazon Aurora PostgreSQL (Primary DB), ElastiCache (Redis), and Amazon OpenSearch.
* **Async Event Bus**: AWS EventBridge and SQS/SNS for decoupled event-driven workflows.
* **External Systems**: Stripe/PayPal (Payments), FedEx/UPS (Shipping), Auth0/AWS Cognito (Identity/OIDC), SendGrid/AWS SES (Notifications), Avalara/TaxJar (Tax calculation).

## Relationships
* **Customer** connects to **CDN / DNS Provider** via HTTPS.
* **CDN / DNS Provider** serves **Web Application (SPA)** via HTTPS.
* **Web Application** communicates with **API Gateway** via HTTPS/REST.
* **API Gateway** routes traffic to **Core E-commerce API** and **Recommendation & Review Service** via internal gRPC/REST over TLS.
* **Core E-commerce API** persists data to **Amazon Aurora PostgreSQL** via PostgreSQL wire protocol, caches state in **ElastiCache (Redis)**, and publishes events to **Async Event Bus** via HTTPS/AMQP.
* **Recommendation & Review Service** queries **Amazon OpenSearch** for keyword indexing and catalog searches.
* **Online Bookstore** integrates with **Identity Provider**, **Payment Gateway**, **Shipping Provider APIs**, **Tax Calculation Service**, and **Email/Notification Service** via outbound REST APIs over TLS 1.3.

## Technology Stack
* **Cloud Infrastructure**: AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global reach and 99.95% uptime.
* **Frontend**: React hosted on Amazon S3 with AWS CloudFront for sub-2-second page loads.
* **Compute**: Amazon ECS Fargate running Go, Python (FastAPI), and Node.js containers for scalable microservices.
* **Storage & Search**: Amazon Aurora PostgreSQL for ACID compliance, ElastiCache (Redis) for cart/session caching, and Amazon OpenSearch for fast search.
* **Messaging**: AWS EventBridge and SQS for asynchronous event-driven decoupling.
* **Security & Auth**: Auth0/AWS Cognito using OIDC/OAuth2 for GDPR/CCPA compliance.

## Rationale
This microservices-based architecture on AWS ECS Fargate scales independently to handle 1 million monthly active users without performance degradation. Asynchronous event decoupling and regional CDN caching ensure strict adherence to sub-2-second 3G page load limits and 99.95% availability targets.