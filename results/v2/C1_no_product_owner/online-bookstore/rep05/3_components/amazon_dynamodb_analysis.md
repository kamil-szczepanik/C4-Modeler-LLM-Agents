## Overview
[Component architecture of Amazon DynamoDB within the Online Bookstore, providing high-throughput, low-latency catalog storage across multiple global regions. It supports secure, scalable e-commerce operations for 1M MAU while meeting strict GDPR, CCPA, and availability requirements.]

## Key Elements
- Request Router / API Frontend
- Storage Node Engine (Partition Storage)
- Request Router / Transaction Coordinator
- Replication Manager (Paxos Group Manager)
- Catalog Service (ECS Fargate client)

## Relationships
- Catalog Service -> Request Router / API Frontend: Queries and mutates item attributes [HTTPS/TLS, IAM SigV4]
- Request Router / API Frontend -> Storage Node Engine (Partition Storage): Routes data read/write operations [Internal RPC]
- Storage Node Engine (Partition Storage) -> Replication Manager: Synchronizes partition state across replicas [Multi-Paxos]

## Technology Stack
- Amazon DynamoDB Global Tables: Multi-region active-active replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for 99.95% availability.
- Distributed B-Tree Storage Engine: SSD-backed storage utilizing Paxos replication for low-latency key-value access.
- AWS KMS Customer Managed Keys (CMKs): Encryption at rest with automated annual rotation.
- IAM SigV4 with Condition Keys: Secure authentication and least-privilege attribute-level authorization.
- AWS CloudTrail & CloudWatch: Audit logging, contributor insights, and auto-scaling target tracking policies.

## Rationale
[This internal component structure guarantees sub-2-second page loads and high availability under peak loads through automatic capacity scaling and distributed consensus. Rigorous encryption, access controls, and multi-region replication satisfy stringent security, compliance, and global performance requirements.]