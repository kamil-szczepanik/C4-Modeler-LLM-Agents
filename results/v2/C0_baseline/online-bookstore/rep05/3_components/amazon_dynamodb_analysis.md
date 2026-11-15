## Overview
The Online Bookstore utilizes an AWS-hosted, multi-region NoSQL architecture designed to provide low-latency shopping cart interactions and real-time book recommendations for 1 million monthly active users. It meets strict retail scalability, performance, and regulatory compliance standards across the US, EU, and APAC regions.

## Key Elements
- **Amazon DynamoDB**: NoSQL database managing `ShoppingCarts` and `Recommendations` tables.
- **ShoppingCarts Table**: Stores user cart items with `CustomerID` partition key, `ItemID` sort key, and TTL.
- **Recommendations Table**: Stores book associations with `BookID` partition key and `RecommendedBookID` sort key.
- **Core Services & Recommendation Engine**: ECS Fargate containers using AWS SDK to query DynamoDB.
- **AWS Infrastructure**: Amazon EventBridge, AWS CloudWatch, AWS KMS, and VPC Endpoints.

## Relationships
- **Core Services** to **Amazon DynamoDB**: HTTPS/TCP over port 443 via AWS PrivateLink and IAM task roles using `BatchGetItem` and `Query` APIs.
- **Recommendation Engine** to **Amazon DynamoDB**: Asynchronous writes to the `Recommendations` table via HTTPS/TCP.
- **Amazon DynamoDB** to **Amazon EventBridge**: Change-data-capture streaming via DynamoDB Streams.
- **Amazon DynamoDB** to **AWS CloudWatch**: Operational metrics and Contributor Insights telemetry via native AWS integration.

## Technology Stack
- **Amazon DynamoDB Global Tables**: Chosen for multi-region replication, supporting global latency and GDPR/CCPA data residency.
- **Provisioned Capacity with Auto-Scaling**: Set to 70% target utilization to absorb traffic spikes cost-effectively while preventing throttling.
- **AWS KMS (Customer Managed Keys)**: Enforces encryption at rest across all deployment regions.
- **AWS IAM & VPC Endpoints**: Enforces least-privilege access, `dynamodb:LeadingKeys` fine-grained access control, and TLS 1.2+ transit security.

## Rationale
This architecture guarantees sub-2-second page loads and high availability (99.95% uptime) through native DynamoDB read-scaling without the operational complexity of caching layers. Furthermore, multi-region global tables, strict KMS encryption, and IAM segregation ensure full GDPR and CCPA compliance for 1M MAU.