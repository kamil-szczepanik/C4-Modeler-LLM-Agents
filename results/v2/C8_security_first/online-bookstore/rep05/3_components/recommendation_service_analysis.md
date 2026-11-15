## Overview
The Online Bookstore system is a scalable e-commerce platform providing catalog browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users globally. It delivers a fast, resilient shopping experience across multiple currencies while maintaining strict GDPR and CCPA compliance.

## Key Elements
- Customers and Store Administrators (Users)
- Single Page Application (React / TypeScript on Amazon S3 + CloudFront)
- Amazon CloudFront / API Gateway / ALB (Edge & Routing Layer)
- Recommendation Service Container (AWS ECS Fargate)
- API Handler Component (Python / FastAPI)
- Recommendation Engine Component (Python / FastAPI)
- Cache & Ingestion Worker Component (Go)
- Amazon ElastiCache (Redis)
- Amazon Aurora PostgreSQL Global Database
- Amazon SQS / SNS

## Relationships
- Amazon CloudFront / API Gateway / ALB -> Recommendation Service: Routes incoming user recommendation requests [HTTPS, gRPC with mTLS]
- API Handler -> Recommendation Engine: Forwards validated recommendation requests [gRPC]
- Recommendation Engine -> Amazon ElastiCache (Redis): Reads pre-computed recommendation vectors [RESP over TLS, <10ms]
- Amazon SQS -> Cache & Ingestion Worker: Delivers asynchronous clickstream and order events [HTTPS/SQS SDK]
- Cache & Ingestion Worker -> Amazon ElastiCache (Redis): Updates cached recommendation data [RESP over TLS]
- Recommendation Service -> Amazon Aurora PostgreSQL Global Database: Reads necessary transactional metadata [SQL over TLS]

## Technology Stack
- **Compute:** AWS ECS Fargate for serverless container orchestration
- **Languages/Frameworks:** Python with FastAPI for API and recommendation logic; Go for high-throughput ingestion workers
- **Caching/Storage:** Amazon ElastiCache (Redis) for low-latency vector caching; Amazon Aurora PostgreSQL for relational data
- **Messaging:** Amazon SQS for asynchronous event-driven ingestion
- **Security/Networking:** mTLS via AWS Service Connect, AWS IAM, and TLS for data in transit and at rest

## Rationale
The microservices-based container architecture deployed across AWS regions ensures 99.95% uptime and handles 1M MAU scaling requirements. Decoupling real-time reads via ElastiCache Redis and asynchronous SQS ingestion guarantees sub-200ms recommendation latency, protecting the overall page load SLA.