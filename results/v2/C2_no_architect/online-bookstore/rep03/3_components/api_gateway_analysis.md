## Overview
[The system is an online bookstore platform serving 1M MAU globally with catalog browsing, secure checkout, recommendations, and reviews. Its core purpose is to provide a reliable, multi-currency e-commerce experience complying with GDPR and CCPA.]

## Key Elements
- Shopper and Site Administrator (Users)
- AWS CloudFront (CDN & Edge Compute)
- AWS WAF (Web Application Firewall)
- API Gateway (Istio / AWS App Mesh Ingress)
- Catalog, Recommendation Engine, Checkout/Payment, Currency Localization, and Support Containers (Amazon EKS)
- Warehouse Partner, Third-Party Payment APIs, AWS KMS, AWS Secrets Manager, Amazon CloudWatch

## Relationships
- Shopper / Admin -> AWS CloudFront: Sends HTTPS requests [HTTPS]
- AWS CloudFront -> AWS WAF: Inspects and filters web traffic [HTTPS]
- AWS WAF -> API Gateway: Forwards sanitized requests [HTTPS]
- API Gateway -> Catalog, Recommendation, Checkout, Localization Containers: Routes internal requests [mTLS via Istio Service Mesh]
- API Gateway -> AWS KMS: Verifies and signs cryptographic JWS tokens [Internal AWS API]

## Technology Stack
- Istio / AWS App Mesh: Manages ingress routing, rate limiting, and strict mTLS for microservices.
- Amazon EKS: Hosts containerized microservices across multi-region clusters.
- AWS WAF & CloudFront: Provides DDoS mitigation, rate limiting, and edge geo-routing.
- OpenTelemetry & Amazon CloudWatch: Handles centralized distributed tracing and structured JSON logging with PII redaction.
- AWS Secrets Manager & KMS: Manages dynamic certificate rotation and cryptographic identity propagation.

## Rationale
[This architecture uses a secure API Gateway paired with a multi-region EKS and Istio service mesh to meet stringent 99.95% availability, scalability, and OWASP security requirements. Edge processing and strict mTLS ensure low-latency global performance while complying with regional data protection regulations.]