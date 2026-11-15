## Overview
The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for global users. The architecture utilizes Amazon DynamoDB with Global Tables to ensure low-latency order processing and high availability.

## Key Elements
*   Order & Checkout Service (Node.js container)
*   Amazon DynamoDB (NoSQL database container)
*   Request Router / Request Coordinator (Component)
*   Storage Nodes / Partition Engine (Component)
*   Replication Manager / Global Tables Engine (Component)

## Relationships
*   Order & Checkout Service -> Request Router: Executes low-latency queries and atomic transactions via AWS SDK / HTTPS with SigV4 Auth
*   Request Router -> Storage Nodes: Routes operations using AWS internal protocols
*   Replication Manager -> Global Tables: Synchronizes cross-region data via AWS internal private backbone network

## Technology Stack
*   Amazon DynamoDB: Provides single-digit millisecond latency and global distribution for high scalability.
*   AWS KMS: Enforces encryption at rest, envelope encryption for PII, and annual key rotation for GDPR/CCPA compliance.
*   AWS IAM & VPC Endpoints: Secures service-to-database communication over isolated private networks.
*   Amazon CloudWatch: Monitors operational metrics, latency spikes, and throttling alerts.
*   Terraform / AWS CDK: Manages infrastructure-as-code deployments across multi-region environments.

## Rationale
This architecture uses DynamoDB Global Tables across target regions to ensure low-latency checkout and 99.95% uptime for global buyers. Robust encryption and IAM controls satisfy GDPR and CCPA compliance requirements without sacrificing performance.