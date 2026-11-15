## Overview
[Amazon ElastiCache (Redis) serves as an in-memory data store for session management, fast catalog caching, shopping cart persistence, and distributed locking. It ensures high performance and scalability to meet retail platform requirements.]

## Key Elements
* In-Memory Data Store Engine (Redis OSS / Valkey)
* Replication Manager
* Cluster Node Manager
* Session Store Data Structure (Hash maps: `user:session:<id>`)
* Cart & Distributed Lock Store Data Structure (Strings/Keys: `cart:<id>`, `lock:item:<id>`)

## Relationships
* Node.js BFF -> Amazon ElastiCache (Redis): Reads and writes session data and cache via RESP v3 over TLS 1.3 [TLS-encrypted connection / Port 6379]
* Checkout Service -> Amazon ElastiCache (Redis): Manages distributed locking and shopping cart persistence via RESP v3 over TLS 1.3 [TCP / Port 6379]

## Technology Stack
* AWS ElastiCache (Redis): Provides managed in-memory caching with multi-AZ replication for high availability.
* Redis OSS / Valkey: Executes high-throughput key-value operations and data structures.
* AWS KMS: Secures data at rest using Customer Managed Keys for GDPR/CCPA compliance.
* AWS Secrets Manager: Rotates and supplies Redis AUTH credentials securely.

## Rationale
[Multi-AZ replication with automatic failover guarantees the 99.95% uptime requirement without sacrificing fast response times. Private subnet isolation and encryption in-transit (TLS 1.3) and at-rest satisfy strict security and data protection mandates.]