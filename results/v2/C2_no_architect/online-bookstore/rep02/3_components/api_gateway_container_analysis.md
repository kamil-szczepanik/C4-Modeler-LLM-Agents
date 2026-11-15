## Overview
The Online Bookstore system is a scalable e-commerce platform designed for selling physical and electronic books with recommendations and reviews. It provides a secure, high-performance shopping experience supporting 1 million monthly active users globally.

## Key Elements
* **Users:** Customers (Shoppers), Catalog Administrators, Registered Reviewers / Authors
* **External Systems:** Amazon CloudFront, Amazon Route 53, Third-Party Payment Gateway, Shipping Provider, Recommendation Engine, AWS CloudWatch / OpenTelemetry, AWS IAM Identity Center
* **Containers:** API Gateway Container, Browse & Search Container, Shopping Cart & Checkout Container, Reviews & Ratings Container, Recommendations Container

## Relationships
* Amazon CloudFront -> API Gateway Container: Forwards user traffic [HTTPS]
* API Gateway Container -> Browse & Search Container: Routes catalogue requests [mTLS via AWS App Mesh]
* API Gateway Container -> Shopping Cart & Checkout Container: Routes cart and checkout requests [mTLS via AWS App Mesh]
* API Gateway Container -> Reviews & Ratings Container: Routes review requests [mTLS via AWS App Mesh]
* API Gateway Container -> Recommendations Container: Routes recommendation requests [mTLS via AWS App Mesh]

## Technology Stack
* **Cloud Infrastructure:** AWS (us-east-1, eu-west-1, ap-southeast-1 regions) selected for global scalability and multi-region deployment.
* **Compute & Orchestration:** AWS ECS / EKS for containerized microservices deployment.
* **Traffic & Security:** AWS Application Load Balancer (ALB), AWS Global Accelerator, and AWS WAF for ingress routing, load balancing, and edge protection.
* **Service Mesh:** AWS App Mesh for internal service-to-service mTLS encryption and tracing.
* **Observability & Secrets:** AWS CloudWatch, OpenTelemetry, and AWS Secrets Manager for monitoring, distributed tracing, and secure runtime credential injection.

## Rationale
This architecture guarantees 99.95% uptime and sub-2-second page loads globally through multi-region AWS deployment, edge acceleration, and robust auto-scaling. Security and compliance requirements (GDPR/CCPA, OWASP Top-10) are met via AWS WAF, mTLS service mesh routing, automated PII log sanitization, and strict secrets management.