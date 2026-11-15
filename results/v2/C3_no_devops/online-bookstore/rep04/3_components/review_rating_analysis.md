## Overview
The Review & Rating component is a microservice within the Online Bookstore that manages customer reviews, 5-star ratings, and helpfulness voting. It enables verified buyers to submit feedback while providing administrators with moderation tools to ensure content quality and brand safety.

## Key Elements
- **Review Controller (FastAPI Router):** Exposes RESTful endpoints and validates JWTs for user and admin contexts.
- **Review Service:** Encapsulates core business logic, including aggregate rating calculations.
- **Moderation Service:** Handles administrative flagging, filtering, and deletion of abusive content.
- **Helpfulness Service:** Manages idempotent user votes and tallies helpfulness scores.
- **Review Repository:** Interacts with persistence layer.
- **Amazon DynamoDB:** Stores review records and aggregated ratings using single-table design with a Global Secondary Index (GSI) on `BookID` and `HelpfulnessScore`.
- **Checkout & Order Container:** External microservice providing verified-purchase validation.
- **AWS API Gateway:** Enforces rate limiting on review and voting endpoints.

## Relationships
- **AWS API Gateway -> Review Controller:** Routes REST/gRPC requests with JWT [HTTPS, TLS 1.3]
- **Review Service -> Checkout & Order Container:** Verifies customer purchases [REST/gRPC over mTLS via AWS App Mesh]
- **Review Service -> Amazon DynamoDB:** Persists and queries review data [AWS SDK, HTTPS]
- **Helpfulness Service -> Amazon DynamoDB:** Executes atomic conditional writes for votes [AWS SDK, HTTPS]

## Technology Stack
- **Python / FastAPI:** High-performance async framework for building APIs with automatic Pydantic input validation.
- **Amazon DynamoDB:** NoSQL database using single-table design for low-latency pagination and sorting.
- **AWS App Mesh:** Secures internal microservice communication using mutual TLS (mTLS).
- **AWS KMS:** Encrypts review data at rest using AES-256.

## Rationale
This architecture uses FastAPI and DynamoDB single-table design to achieve sub-second query latencies, easily supporting the 1M MAU scalability requirement. Security and data integrity controls, such as Pydantic sanitization, JWT RBAC, and conditional writes, prevent review fraud and maintain GDPR/CCPA compliance.