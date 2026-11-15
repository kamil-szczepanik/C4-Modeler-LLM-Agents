## Overview
An online bookstore system providing catalog browsing, secure checkout, 5-star reviews, and personalized "Customers also bought" recommendations for 1M MAU. It ensures global availability across three AWS regions while maintaining strict GDPR and CCPA compliance.

## Key Elements
- Shoppers (Customers) and Merchandisers (Store Staff)
- Amazon API Gateway (Entry point)
- Recommendation Container (Spring Boot / Python)
- Recommendation API Controller (Spring Boot)
- Algorithm Engine (Python / AWS ECS / SageMaker)
- Model Data Store (Amazon ElastiCache Redis)
- Telemetry Publisher Component (Spring Boot)
- External Systems: Payment Gateway, Shipping Provider, Tax/Currency Provider

## Relationships
- Amazon API Gateway -> Recommendation Container: Routes internal traffic via VPC links [gRPC]
- Recommendation API Controller -> Model Data Store: Fetches pre-computed recommendations [Redis Protocol]
- Recommendation API Controller -> Telemetry Publisher Component: Dispatches interaction events [In-process async]
- Telemetry Publisher Component -> Amazon Kinesis: Emits anonymous usage telemetry [HTTPS]
- Algorithm Engine -> Model Data Store: Writes pre-computed co-purchase matrices [Redis Protocol]
- Catalog & Search -> Recommendation Container: Syncs product metadata asynchronously [Amazon SQS]

## Technology Stack
- Spring Boot: Powers backend controllers and telemetry handling for robust enterprise integration.
- Python (Scikit-learn / LightFM): Executes offline collaborative filtering and co-purchase analysis.
- Amazon ElastiCache (Redis): Provides low-latency caching with Global Datastores for multi-region replication.
- Amazon Kinesis / EventBridge: Handles asynchronous, GDPR-compliant telemetry ingestion.
- AWS ECS / SageMaker: Runs scheduled batch machine learning jobs.

## Rationale
Decoupling offline batch machine learning from the real-time runtime path via Redis guarantees sub-2-second page loads and high availability. Asynchronous telemetry and multi-region replication satisfy stringent performance, scalability, and regulatory requirements.