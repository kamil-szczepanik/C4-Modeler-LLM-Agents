## Overview
The Online Bookstore Edge & Ingress system manages global incoming client traffic, enforcing security, rate-limiting, and request routing. It ensures high performance, multi-currency support, and GDPR compliance across three global AWS regions.

## Key Elements
* DNS Router (Amazon Route 53)
* API Gateway Service (Amazon API Gateway)
* Auth & Token Verifier Component
* Request Router & Transformer Component
* Client Frontend (React, AWS CloudFront, Amazon S3)
* Downstream Containers (Catalog, Order, Review)

## Relationships
* Client Frontend -> API Gateway Service [HTTPS over TLS]
* API Gateway Service -> Auth & Token Verifier [In-memory validation]
* Auth & Token Verifier -> Request Router & Transformer [Internal routing]
* Request Router & Transformer -> Catalog, Order, and Review Containers [gRPC over TLS with AWS X-Ray Trace Context and localization headers]
* Amazon Route 53 -> Regional API Gateways [Latency-based DNS routing with health-check failover]

## Technology Stack
* Amazon Route 53: Provides latency-based global DNS routing and automatic multi-region failover.
* Amazon API Gateway: Handles rate-limiting, OWASP Top-10 mitigations, TLS termination, and response caching for anonymous catalog searches.
* AWS X-Ray: Enables distributed tracing across global regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
* gRPC over TLS: Secures low-latency internal communication between edge components and microservices.
* AWS CodePipeline: Orchestrates zero-downtime blue/green deployments for API routes.

## Rationale
This architecture utilizes managed AWS edge services to handle 1M MAU while maintaining sub-2-second page loads globally. Edge-based security, caching, and currency fallback logic protect backend microservices from traffic spikes while ensuring high availability.