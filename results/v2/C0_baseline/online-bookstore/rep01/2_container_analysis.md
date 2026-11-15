## Overview
[A scaled-down Amazon-style e-commerce site for physical and electronic books, providing catalog browsing, secure checkout, reviews, and personalized recommendations.]

## Key Elements
*   **Users & Actors:** Book Buyer, Site Administrator, Customer Support Representative, Content Provider/Publisher
*   **External Systems:** Payment Gateway, Third-Party Shipping API, Tax Calculation Service, Marketing/Email Service Provider, Recommendation Engine/ML Service
*   **Containers:** Single Page Application (SPA), API Gateway, Catalog & Search Container, Order & Checkout Container, Recommendation Container, Localization Container, Analytics & Event Ingestion Container
*   **Infrastructure & Data:** Amazon S3, CloudFront, AWS ECS/EKS, PostgreSQL, Amazon OpenSearch, Amazon SQS/SNS, AWS Kinesis Firehose, AWS Route 53

## Relationships
*   **Book Buyer to SPA:** HTTPS via AWS CloudFront and Route 53 latency-based routing
*   **SPA to API Gateway:** HTTPS with JWT validation and rate-limiting
*   **API Gateway to Containers:** gRPC over mTLS via AWS App Mesh within private VPC subnets
*   **Order & Checkout Container to Payment Gateway:** HTTPS with strict in-memory ephemeral cardholder data processing
*   **Analytics Container to Kinesis Firehose:** High-throughput asynchronous telemetry streaming with PII scrubbing

## Technology Stack
*   **Frontend:** React hosted on AWS S3 + CloudFront for performance (page load < 2s on 3G)
*   **API & Core Backend:** Node.js/Express (Order/Checkout and Localization), Spring Boot (Catalog/Search), Python/FastAPI (Recommendation), Go (Analytics)
*   **Database & Search:** PostgreSQL with multi-region replication, Amazon OpenSearch for keyword search
*   **Messaging & Streaming:** Amazon SQS/SNS for events, AWS Kinesis Firehose for analytics ingestion
*   **Security & Operations:** AWS ECS/EKS, AWS Secrets Manager, AWS IAM, AWS KMS CMKs for regional data residency, AWS App Mesh for mTLS

## Rationale
[This multi-region, containerized architecture isolates the PCI-DSS compliant checkout domain while decoupling high-throughput analytics to ensure 99.95% uptime and scalability for 1M MAU. Leveraging edge delivery and regional AWS infrastructure guarantees sub-2-second page loads and strict GDPR/CCPA data residency compliance.]