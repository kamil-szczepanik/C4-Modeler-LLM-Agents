## Overview
The Online Bookstore is a globally distributed e-commerce platform built on AWS to support physical and electronic book sales with high availability and low latency. It uses a cloud-native microservices architecture to handle high traffic volumes while ensuring strict compliance with regulatory standards.

## Key Elements
- **Users**: Customers (Shoppers), Store Staff & Administrators, Customer Support Representatives
- **External Systems**: Payment Gateway, Third-Party Shipping Provider, Tax & Currency Provider
- **Frontend Container**: React Single Page Application hosted on Amazon S3 and distributed via Amazon CloudFront
- **API Gateway Container**: Amazon API Gateway serving as the perimeter router and security enforcement point
- **Backend Containers**: Spring Boot and Python microservices including Catalog & Search, Order & Checkout, Recommendation, Localization & Tax, Content & Review (Node.js/DocumentDB), and Admin Back-Office

## Relationships
- Frontend Container -> API Gateway: Calls REST and GraphQL endpoints [HTTPS]
- API Gateway -> Catalog & Search: Routes internal traffic via VPC links [gRPC]
- API Gateway -> Order & Checkout: Routes internal traffic via VPC links [gRPC]
- API Gateway -> Recommendation: Routes internal traffic via VPC links [gRPC]
- API Gateway -> Localization & Tax: Routes internal traffic via VPC links [gRPC]
- API Gateway -> Content & Review: Routes internal traffic via VPC links [gRPC]
- API Gateway -> Admin Back-Office: Routes internal traffic via VPC links [gRPC]
- API Gateway -> Access Logging Emitter: Asynchronously streams telemetry [Async / CloudWatch Logs SDK]

## Technology Stack
- **Cloud Infrastructure**: AWS across regions `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global scalability and low latency
- **Global Traffic**: Amazon Route 53 with latency-based routing and health checks for regional failover
- **Edge Security**: Amazon API Gateway with built-in JWT authorizers and cached JWKS for low-latency perimeter validation
- **Internal Communication**: gRPC over VPC links for high-performance service-to-service data exchange
- **Observability**: AWS X-Ray for distributed tracing and Amazon CloudWatch for telemetry and asynchronous logging

## Rationale
This architecture meets the 99.95% availability target and 1M MAU scalability requirement through a multi-region deployment managed by Amazon Route 53. Utilizing Amazon API Gateway with cached JWKS and gRPC ensures sub-2-second page loads even on constrained networks while maintaining robust OWASP Top-10 security mitigations.