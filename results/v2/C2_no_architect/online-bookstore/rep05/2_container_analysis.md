## Overview
An Amazon-style online bookstore providing catalogue browsing, secure checkout, reviews, and recommendations across three global AWS regions. Built to scale for 1M MAU while ensuring strict multi-region compliance, security, and high availability.

## Key Elements
* Users: Casual Browsers, Intentional Buyers, Authors/Publishers, Store Administrators.
* External Systems: Payment Gateway, Third-Party Shipping Provider APIs.
* Core Containers: Web Frontend SPA/SSR, Catalogue Service, Secure Checkout & Payment Service, Recommendation Engine, Admin & Reporting Service.
* Infrastructure & Security: AWS WAF, Application Load Balancers, AWS App Mesh / Istio, AWS KMS, AWS Secrets Manager.

## Relationships
* Users to Frontend: HTTPS (TLS 1.3), OAuth2/OIDC, JWT via Route 53 and ALBs.
* Frontend to Containers: REST and gRPC over mTLS via AWS App Mesh.
* Checkout Service to Payment Gateway: HTTPS / TLS 1.3 API integration.
* Backend to Shipping APIs: HTTPS REST API integrations.
* Cross-Region Replication: AWS region-isolated backups and encrypted database sync across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Technology Stack
* Cloud & Compute: AWS ECS/EKS for multi-region container orchestration in `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
* Networking & Routing: AWS Route 53 with latency-based routing and automated DNS failover for 99.95% uptime.
* Security & Compliance: AWS WAF (OWASP Top-10), AWS KMS (data at rest encryption for GDPR/CCPA), AWS Secrets Manager, Trivy/AWS Inspector (supply chain).
* Observability & Mesh: AWS X-Ray, CloudWatch, OpenSearch, Prometheus, Grafana, AWS App Mesh / Istio (mTLS).

## Rationale
The containerized microservices architecture with strict bulkhead isolation prevents non-critical background jobs like recommendations and reporting from impacting core catalogue browsing and checkout. Multi-region AWS deployment with automated failover and zero-trust service mesh guarantees high availability, regional data compliance, and strict performance SLAs.