## Overview
The Online Bookstore system is a scaled-down e-commerce platform providing catalog browsing, secure checkout, reviews, and recommendations for 1M MAU. The Browse & Search Container provides secure, multi-region catalog discovery with sub-2s performance on 3G networks.

## Key Elements
- **Users**: Customers (Shoppers), Catalog Administrators, Registered Reviewers / Authors
- **Containers**: API Gateway Container, Browse & Search Container, Shopping Cart & Checkout Container, Reviews & Ratings Container, Recommendations Container
- **External Systems**: Amazon CloudFront, Amazon Route 53, Third-Party Payment Gateway, Shipping Provider, Recommendation Engine, AWS CloudWatch / OpenTelemetry, AWS IAM Identity Center
- **Data & Caching**: Amazon ElastiCache (Redis) for search result caching, Database read-replicas for catalog storage

## Relationships
- Customers -> Amazon Route 53: Directs global traffic via latency-based routing [HTTPS]
- Amazon Route 53 -> Amazon CloudFront: Serves cached static catalog views and search facets [HTTPS]
- Amazon CloudFront -> API Gateway Container: Forwards dynamic search and browse requests [HTTPS]
- API Gateway Container -> Browse & Search Container: Routes browse and search requests via service mesh [mTLS (AWS App Mesh)]
- Browse & Search Container -> Amazon ElastiCache (Redis): Retrieves cached search queries and catalog metadata [TCP]

## Technology Stack
- **Compute**: AWS ECS / EKS with Horizontal Pod Autoscalers (HPA) for container orchestration
- **Cloud & Edge**: AWS (us-east-1, eu-west-1, ap-southeast-1), Amazon CloudFront (CDN), Amazon Route 53 (DNS routing)
- **Security & Observability**: AWS App Mesh (mTLS), AWS CloudWatch & OpenTelemetry (Distributed tracing), AES-256 (Encryption at rest), JWT (Cryptographically signed currency tokens)
- **Caching & Data**: Amazon ElastiCache (Redis) for query caching and database read-replicas

## Rationale
Multi-region deployment across AWS regions behind Route 53 guarantees 99.95% availability (R-07) and global performance. Aggressive edge caching via Amazon CloudFront and Redis ensures sub-2-second page loads on 3G (R-06) while supporting 1M MAU (R-05).