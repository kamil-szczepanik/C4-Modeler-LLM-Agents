## Overview
The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations. Its purpose is to deliver a scalable, highly available e-commerce platform supporting multi-currency transactions and global users.

## Key Elements
- Recommendation Store Table (DynamoDB): Partition Key `CustomerID`, Sort Key `ProductID`.
- Customer Session State Table (DynamoDB): TTL-enabled cart persistence.
- Customer Reviews & Ratings Table (DynamoDB): Partition Key `ProductID`, Sort Key `ReviewID`.
- Idempotency & Lock Table (DynamoDB): Partition Key `OperationID`.
- AWS VPC Endpoints: Gateway and Interface endpoints.

## Relationships
- Recommendation Service -> Recommendation Store Table: Reads recommendation data via Native Database Protocol over VPC.
- Order & Checkout Service -> Customer Session State Table: Persists active shopping carts via Native AWS SDK over VPC, HTTPS/TLS.
- Catalog & Search Service -> Customer Reviews & Ratings Table: Fetches product reviews and ratings via Native AWS SDK over VPC, HTTPS/TLS.
- Order & Checkout Service -> Idempotency & Lock Table: Verifies transaction states via Native AWS SDK over VPC, HTTPS/TLS.
- Microservices -> AWS VPC Endpoints: Routes database traffic internally via HTTPS/TLS 1.3.

## Technology Stack
- Amazon DynamoDB: Provides single-digit millisecond latency for high-velocity reads and writes.
- AWS VPC Endpoints: Secures internal traffic without public internet exposure.
- AWS IAM: Enforces strict access control policies on database components.

## Rationale
This architecture leverages DynamoDB's scalable NoSQL design to handle high-throughput workloads like shopping carts, reviews, and recommendations with predictable sub-2-second performance. Utilizing private VPC endpoints and conditional writes guarantees compliance with stringent security and consistency requirements.