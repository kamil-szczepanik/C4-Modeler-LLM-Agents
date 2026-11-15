## Overview
The Online Bookstore Session Cache Store is a multi-region NoSQL data layer designed to deliver high-performance cart and session management. It ensures sub-millisecond data access, seamless global scaling, and strict privacy compliance for millions of active users.

## Key Elements
- **ShoppingCartsTable**: Core Amazon DynamoDB table storing session and cart items.
- **UserIndex**: Global Secondary Index (GSI) on `UserID` for efficient user-specific data lookups.
- **SessionRepository**: Data access layer utilizing AWS SDK v3 for Node.js/Go.
- **Data Privacy Service**: External consumer handling GDPR/CCPA requests via `UserIndex`.
- **Checkout & Order Service**: Primary client writing and reading session states.

## Relationships
- Checkout & Order Service -> ShoppingCartsTable: Manages cart and session data [HTTPS, TLS 1.3, AWS PrivateLink]
- Data Privacy Service -> UserIndex: Queries and purges user session data for compliance [HTTPS, TLS 1.3, AWS PrivateLink]
- ShoppingCartsTable -> ShoppingCartsTable: Replicates global data across regions [AWS DynamoDB Global Tables Protocol]

## Technology Stack
- **Amazon DynamoDB**: Core NoSQL database chosen for native single-digit millisecond latency and high scalability.
- **DynamoDB Global Tables**: Enables multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global shoppers.
- **AWS PrivateLink & TLS 1.3**: Secures network traffic in-transit within isolated VPC boundaries.
- **DynamoDB TTL**: Automatically purges abandoned carts after 30 days to meet GDPR/CCPA data minimization mandates.

## Rationale
This architecture guarantees 99.95% uptime and rapid page loads under 2 seconds for 1 million MAU by utilizing distributed NoSQL storage with provisioned auto-scaling. Additionally, native global replication and built-in TTL policies satisfy strict multi-region performance and cross-border privacy regulations.