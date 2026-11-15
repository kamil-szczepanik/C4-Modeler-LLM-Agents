## Overview
Amazon DynamoDB serves as the low-latency distributed database container for the Online Bookstore's catalogue and shopping cart services. It is architected to support 1 million monthly active users globally while ensuring strict compliance with GDPR, CCPA, and OWASP security standards.

## Key Elements
- **Request Router:** DynamoDB Frontend Fleet handling request parsing, IAM SigV4 authorization, and partition key hashing.
- **Storage Engine Component:** Distributed B-tree/SSD storage partitions managed via AWS multi-AZ replication.
- **Stream Publisher Component:** DynamoDB Streams capturing item-level modifications for asynchronous change data capture.
- **Global Tables:** Multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Relationships
- **Catalogue & Shopping Cart Services -> Request Router:** Invoke CRUD operations using HTTPS / JSON over AWS PrivateLink VPC Endpoints.
- **Request Router -> Storage Engine:** Route partition-hashed requests via internal TCP/RPC over the AWS backbone.
- **DynamoDB Streams Component -> Recommendation Engine:** Push CDC change events securely using AWS Lambda and Amazon DynamoDB Streams.

## Technology Stack
- **Amazon DynamoDB:** Core NoSQL database chosen for predictable sub-10ms latency at scale.
- **AWS KMS (CMK):** Customer-managed encryption keys for at-rest encryption to satisfy GDPR/CCPA.
- **Terraform / AWS CDK:** Infrastructure as Code for defining tables, GSIs, and auto-scaling policies.
- **AWS CloudTrail & Contributor Insights:** Operational observability tools for hot partition detection and auditing.

## Rationale
This architecture uses DynamoDB Global Tables and On-Demand capacity to ensure sub-2-second page loads and 99.95% availability for a global user base. Rigorous IAM, TLS 1.3, and KMS encryption controls secure customer PII against OWASP threats without sacrificing performance.