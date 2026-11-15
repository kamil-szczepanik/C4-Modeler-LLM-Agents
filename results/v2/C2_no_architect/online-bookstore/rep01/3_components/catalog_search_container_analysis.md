## Overview
The Catalog & Search Container manages book inventory, real-time availability, and high-performance keyword search with facets. It powers fast product discovery while supporting multi-currency pricing and secure, decoupled telemetry for personalization.

## Key Elements
- **API Gateway**: Entry point for public traffic with AWS WAF rate-limiting.
- **Catalog & Search Container**: Core microservice deployed on Amazon ECS/EKS.
- **AWS Aurora Global Database**: Multi-region persistent storage for catalog data.
- **Amazon ElastiCache**: Write-through caching layer for real-time stock and catalog data.
- **Amazon SQS**: Asynchronous event queue for telemetry and personalization signals.
- **AWS Route 53**: Latency-based global traffic routing across regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`).

## Relationships
- **API Gateway -> Catalog & Search Container**: Routes search, browse, and facet requests via mTLS inside AWS VPC.
- **Catalog & Search Container -> AWS Aurora Global Database**: Queries and updates catalog records using encrypted SQL (AES-256).
- **Catalog & Search Container -> Amazon ElastiCache**: Retrieves cached catalog data and manages real-time availability via Redis Pub/Sub.
- **Catalog & Search Container -> Amazon SQS**: Publishes sanitized, anonymized search telemetry asynchronously for personalization.

## Technology Stack
- **Amazon ECS/EKS**: Orchestrates containerized microservices for scalability and high availability (R-05, R-07).
- **AWS Aurora Global Database**: Ensures sub-second read replication globally for low-latency browsing (R-06).
- **Amazon ElastiCache**: Provides write-through caching to handle traffic peaks and real-time stock badging.
- **AWS WAF**: Protects search endpoints against scraping, DoS, and complex injection attacks (R-08).
- **IAM Roles for Tasks (IRSA)**: Secures database and cache access without hardcoded credentials.

## Rationale
This architecture uses multi-region active-active deployment and aggressive write-through caching to guarantee sub-2-second page loads and 99.95% uptime globally. Strict input sanitization, WAF rate-limiting, and PII minimization ensure full OWASP compliance and GDPR/CCPA alignment.