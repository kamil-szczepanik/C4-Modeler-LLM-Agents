## Overview
This architecture defines the Amazon DynamoDB component-level design for a global online bookstore serving 1M MAU. It ensures low-latency session management, secure cart storage, and multi-region replication.

## Key Elements
- **Cart Table Component**: Stores transient shopping cart items using partition key `userId` and sort key `cartId`.
- **Session Table Component**: Stores user session states with automatic TTL cleanup.
- **Global Tables Configuration**: Enables multi-active cross-region replication for the Session Table.
- **DynamoDB Encryption Component**: Enforces data encryption at rest using AWS KMS.
- **DynamoDB Streams Component**: Captures item modifications for real-time change data capture.
- **DynamoDB PITR**: Provides continuous backups for data durability.

## Relationships
- **Core E-Commerce Service** -> **Cart Table Component**: Reads and writes cart state via AWS SDK [HTTPS / TLS 1.3].
- **Core E-Commerce Service** -> **Session Table Component**: Validates and updates session state via AWS SDK [HTTPS / TLS 1.3].
- **Cart & Session Tables** -> **DynamoDB Encryption Component**: Encrypts stored PII data at rest [AWS KMS API / TLS 1.3].
- **Cart Table Component** -> **DynamoDB Streams Component**: Emits cart abandonment events [AWS Internal].
- **DynamoDB Streams Component** -> **Amazon EventBridge**: Forwards cart abandonment events [AWS SDK / TLS 1.3].

## Technology Stack
- **Amazon DynamoDB**: Chosen for single-digit millisecond latency to satisfy the <2s page load requirement.
- **DynamoDB Global Tables**: Selected for managed multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- **AWS KMS**: Utilized for customer-managed encryption keys to ensure GDPR and CCPA compliance.
- **DynamoDB Streams**: Deployed for event-driven processing without polling overhead.

## Rationale
This component architecture achieves 99.95% availability and global performance by leveraging fully managed AWS services with native multi-region replication. It strictly satisfies security mandates and data protection constraints without adding custom application overhead.