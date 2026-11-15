## Overview
- Scaled-down Amazon-style e-commerce online bookstore for buying physical and electronic books with recommendations and reviews.
- Handles 1 million monthly active users (MAU) with 99.95% uptime while ensuring GDPR and CCPA compliance.

## Key Elements
- Book Buyer, Site Administrator, Customer Support Representative
- Single Page Application (React, AWS S3, CloudFront)
- API Gateway (Node.js, AWS App Mesh, JWT)
- Catalog & Search Container (Spring Boot, Amazon OpenSearch, PostgreSQL)
- Order & Checkout Container (Node.js/Express, PostgreSQL)
- Recommendation Container (Python/FastAPI)
- Localization Container (Node.js/Express)
- Analytics & Event Ingestion Container (Go, AWS Kinesis Firehose, Amazon SQS/SNS, SQLite/WAL)
- External Systems: Payment Gateway, Third-Party Shipping API, Tax Calculation Service, Marketing/Email Service Provider

## Relationships
- Single Page Application -> API Gateway: Communicates via HTTPS / REST
- API Gateway -> Catalog & Search Container, Order & Checkout Container, Recommendation Container, Localization Container: Routes requests via gRPC over mTLS
- API Gateway -> Analytics & Event Ingestion Container: Forwards telemetry and events via gRPC over mTLS via AWS App Mesh
- Analytics & Event Ingestion Container -> Marketing/Email Service Provider: Triggers marketing emails and event notifications via Amazon SQS/SNS
- Analytics & Event Ingestion Container -> AWS Kinesis Firehose: Streams telemetry via HTTPS / AWS SDK

## Technology Stack
- React, AWS S3, CloudFront: Powers responsive frontend UI with global CDN caching for fast page loads under 2s on 3G
- Node.js, Express, Go: Delivers high-performance, asynchronous backend routing and event ingestion
- Spring Boot, Python/FastAPI: Supports robust business logic and ML-based recommendation models
- PostgreSQL, Amazon OpenSearch: Provides relational data storage and fast keyword search capabilities
- AWS Kinesis Firehose, Amazon SQS/SNS: Enables scalable real-time telemetry streaming and reliable asynchronous messaging
- AWS ECS Fargate, AWS App Mesh: Facilitates containerized multi-region deployment across us-east-1, eu-west-1, and ap-southeast-1 with mTLS service mesh security

## Rationale
- Microservices architecture combined with AWS ECS Fargate ensures elastic scalability to handle 1M MAU across three global regions with 99.95% availability.
- Strict PII scrubbing at the ingress boundary and encrypted local buffering guarantee GDPR and CCPA compliance while maintaining high-throughput event processing.