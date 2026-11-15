## Overview
An Amazon-style e-commerce online bookstore platform designed to handle global book browsing, recommendations, and secure checkout. The system delivers high scalability, multi-currency support, and strict compliance across multiple AWS regions.

## Key Elements
- Shopper (Customer)
- Catalog Manager (Site Admin)
- Recommendation Engine Container
- Currency Localization Container
- API Gateway (Istio / AWS App Mesh)
- Catalog Container (Amazon EKS / Microservices)
- AWS OpenSearch / Elasticsearch
- AWS KMS

## Relationships
- Shopper -> API Gateway: Browses catalogue & searches via HTTPS (mTLS)
- API Gateway -> Catalog Container: Routes internal requests via mTLS (Istio/App Mesh)
- Catalog Container -> AWS OpenSearch: Queries product metadata and pre-calculated regional pricing
- Recommendation Engine Container -> Catalog Container: Consumes catalog data for recommendations via mTLS

## Technology Stack
- Amazon EKS: Container orchestration for microservices ensuring scalability and 99.95% uptime
- AWS OpenSearch / Elasticsearch: Search backend populated via asynchronous CDC for high-performance <2s search
- AWS KMS: Customer-managed keys (CMKs) for encryption at rest ensuring GDPR/CCPA compliance
- OAuth2/OIDC: JWT validation for securing Catalog Manager write operations
- Istio / AWS App Mesh: Service mesh handling mTLS and API rate limiting

## Rationale
Decoupled read/write paths via OpenSearch and pre-calculated regional pricing ensure low-latency searches globally across three AWS regions. Robust security controls and EKS containerization satisfy OWASP compliance, multi-region scalability, and high availability requirements.