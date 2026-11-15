## Overview
- An Amazon OpenSearch component provides scalable keyword search, fuzzy matching, and search analytics for the Online Bookstore.
- It delivers high-performance product discovery to support 1 million monthly active users while ensuring GDPR and CCPA compliance.

## Key Elements
- **REST API Handler Component**: Receives secure HTTPS requests via SigV4.
- **Search Engine Component**: Apache Lucene Core executing inverted-index searches and multi-language tokenization.
- **Index Management Component**: Manages shard allocation, replica sync, and snapshots.
- **Data Storage Component**: EBS gp3 block storage with AWS KMS encryption.
- **Async Event Emitter Component**: Offloads search telemetry.

## Relationships
- Catalog Service -> REST API Handler: Queries catalogue items [HTTPS/JSON, TLS 1.3, SigV4]
- Search Engine -> Data Storage: Reads and writes data [POSIX block I/O]
- Search Engine -> Async Event Emitter: Offloads metrics [In-memory queue]
- Async Event Emitter -> Amazon Kinesis Data Streams: Exports search telemetry [HTTPS/JSON]

## Technology Stack
- **Amazon OpenSearch Service**: Managed search engine ensuring 99.95% availability.
- **AWS KMS**: Customer-managed keys for Encryption-at-Rest.
- **Amazon S3**: Automated snapshot storage and retention.
- **Amazon Kinesis Data Streams**: Streaming telemetry export for merchandising analytics.

## Rationale
- Multi-AZ deployment and dedicated master nodes guarantee 99.95% uptime and split-brain prevention.
- Strict IAM least-privilege scoping and private VPC isolation satisfy OWASP Top-10 and GDPR/CCPA compliance requirements.