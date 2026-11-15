## Overview
The Recommendation Service provides personalized book recommendations and promotional merchandising for the Online Bookstore. It processes high-throughput user interactions while meeting strict sub-2-second performance and GDPR/CCPA compliance requirements.

## Key Elements
- **Active Shopper & Marketing Manager**: Primary users and internal personas driving discovery and promotional rules.
- **API Controller**: FastAPI application managing inbound gRPC and REST requests with RBAC.
- **Recommendation Engine**: Python module performing collaborative filtering for "Customers also bought" features.
- **Merchandising & Rules Processor**: Component applying promotional weights for sponsored book placements.
- **Model Store Client**: Fetches pre-computed machine learning models from Amazon S3.
- **Feature Cache Client**: Retrieves real-time user clickstream data from Amazon ElastiCache (Redis).
- **Async Telemetry Publisher**: Background worker managing asynchronous metric collection.

## Relationships
- **Amazon API Gateway -> API Controller**: Routes incoming recommendation requests using mTLS and TLS 1.3.
- **Core E-Commerce API -> API Controller**: Requests personalized recommendations via gRPC.
- **API Controller -> Recommendation Engine & Merchandising Processor**: Coordinates business logic using synchronous in-process method calls.
- **Model Store Client -> Amazon S3**: Fetches models using encrypted AWS SDK calls over HTTPS.
- **Feature Cache Client -> Amazon ElastiCache (Redis)**: Queries session features via TCP.
- **Async Telemetry Publisher -> Amazon SQS**: Publishes pseudonymized metrics asynchronously via HTTPS.

## Technology Stack
- **Python with FastAPI**: Powers the core API Controller and asynchronous background workers for high performance.
- **Scikit-learn / LightFM**: Implements collaborative filtering algorithms within the Recommendation Engine.
- **Amazon S3**: Stores pre-computed models secured with AWS KMS encryption.
- **Amazon ElastiCache (Redis)**: Delivers low-latency access to real-time user session data.
- **Amazon SQS**: Decouples telemetry publishing to protect critical API latency SLAs.

## Rationale
This component architecture separates high-latency machine learning tasks and telemetry logging from synchronous request paths using asynchronous workers and caching. This design ensures the system scales to 1M MAU while maintaining sub-2-second response times and strict GDPR/CCPA privacy controls.