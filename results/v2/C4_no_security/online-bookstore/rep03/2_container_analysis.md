## Overview
The Online Bookstore system is a globally distributed, high-availability e-commerce platform designed to support 1 million monthly active users with multi-currency checkout, rapid catalog browsing, and personalized recommendations. It ensures strict data residency compliance (GDPR/CCPA) and 99.95% uptime across three AWS regions.

## Key Elements
* **Users & Roles**: Casual Shoppers, Buyers, and Contributors/Reviewers.
* **Client Frontend**: Single Page Application (React) hosted on AWS CloudFront/S3.
* **Edge & Ingress**: Amazon Route 53 (latency-based DNS) and Amazon API Gateway (rate-limiting, JWT validation).
* **Core Microservices (Containers)**: Catalog & Search Container (Spring Boot/Go), Order & Checkout Container (Node.js/Java), and Review & Rating Container (Python/Django).
* **Data Stores**: Amazon Aurora PostgreSQL (Global Database) and Amazon DynamoDB (Global Tables).
* **External Systems**: Stripe/PayPal, FedEx/UPS, Avalara/TaxJar, AWS SES/SendGrid.

## Relationships
* **SPA to API Gateway**: HTTPS over TLS for all client requests routed via AWS Route 53 and CloudFront.
* **API Gateway to Containers**: Regional API Gateways forward requests to isolated backend containers within each VPC.
* **Inter-Service Communication**: gRPC over TLS for internal service-to-service calls.
* **Order & Checkout to External APIs**: Synchronous HTTPS calls with Envoy/AWS App Mesh circuit breakers to Stripe, PayPal, and Avalara.

## Technology Stack
* **Cloud Infrastructure**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`), AWS ECS/EKS with Karpenter, and AWS App Mesh / Envoy.
* **Frontend**: React, AWS CloudFront, Amazon S3.
* **Backend**: Node.js, Spring Boot, Go, Python/Django for isolated container services.
* **Databases & Search**: Amazon Aurora PostgreSQL Global Database for transactional persistence; Amazon DynamoDB Global Tables for cart sessions; Amazon OpenSearch for catalog search and recommendations.
* **Operations & Delivery**: ArgoCD with AWS CodePipeline, AWS Secrets Manager, OpenTelemetry, Prometheus, and Grafana.

## Rationale
This multi-region, containerized architecture leverages AWS global services (Aurora Global Databases, DynamoDB Global Tables, and Route 53) to guarantee low latency, strict GDPR/CCPA data residency compliance, and 99.95% availability. Isolating critical domains like checkout and implementing strict circuit breakers ensures revenue protection and resilience against upstream API failures.