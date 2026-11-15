## Overview
[The Catalog & Search Container handles book discovery, faceted filtering, and search functionality for the Online Bookstore. It delivers sub-second response times and multi-currency support while ensuring scalability and GDPR/CCPA compliance.]

## Key Elements
* Search API Controller (Spring MVC)
* Catalog Query Service (Spring Data / Domain Logic)
* Product Detail Repository (Spring Data JPA)
* Cache Manager Component (Spring Data Redis)
* Recommendation Integration Client (Spring Cloud OpenFeign)
* Amazon Aurora PostgreSQL & Amazon ElastiCache (Redis)

## Relationships
* API Gateway -> Search API Controller: Routes search requests [REST over HTTPS, AWS SigV4]
* Catalog Query Service -> Cache Manager Component: Reads/writes query results [In-memory / Redis protocol over TLS]
* Product Detail Repository -> Amazon Aurora PostgreSQL: Queries canonical book metadata [JDBC over TLS 1.3]
* Recommendation Integration Client -> Recommendation Service Container: Fetches personalized recommendations [REST over HTTPS, OAuth2 / SigV4]

## Technology Stack
* Java / Spring Boot: Core runtime for the catalog container, providing dependency injection and robust enterprise features.
* Amazon Aurora PostgreSQL: Primary data store using native full-text search for catalog persistence.
* Amazon ElastiCache (Redis): Distributed caching layer using Global Datastores for low-latency multi-currency query results.
* Resilience4j: Provides circuit breaker fallback mechanisms for recommendation integration to protect availability.
* AWS ECS Fargate & X-Ray: Container orchestration and distributed tracing for scalability and observability.

## Rationale
[Decomposing the catalog container with Spring Boot, Aurora PostgreSQL, and ElastiCache satisfies sub-second performance and 1M MAU scalability targets without operational complexity. This streamlined stack maintains high availability and strict GDPR/CCPA security compliance across multi-region AWS deployments.]