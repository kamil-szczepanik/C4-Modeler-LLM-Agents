## Overview
The Audit Query API is a Go-based microservice that provides secure, high-performance access to 7-year immutable audit logs for compliance officers and auditors. It isolates analytical queries from real-time fraud scoring while maintaining strict PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
- **Query Router / Controller**: Go-based entry point handling HTTPS/REST requests, OIDC/JWT authentication, RBAC, input validation, and rate-limiting.
- **Audit Query Service**: Go-based business logic layer executing search, filtering, pagination, data masking, and export orchestration.
- **Export Formatter**: Go-based streaming component transforming audit records into CSV or JSON formats.
- **Ledger Repository**: Go and AWS SDK data access layer connecting exclusively to an Amazon Aurora read replica.
- **Amazon Aurora Read Replica**: Dedicated PostgreSQL-compatible database layer storing encrypted, tamper-evident audit ledgers.

## Relationships
- **Compliance Portal -> Query Router**: HTTPS with OIDC/JWT authentication [TLS 1.3]
- **Query Router -> Audit Query Service**: In-process function calls with RBAC and rate-limiting
- **Audit Query Service -> Export Formatter**: Streams raw records for serialization [In-process function calls]
- **Audit Query Service -> Ledger Repository**: Queries historical audit data [mTLS / PostgreSQL Wire Protocol]
- **Ledger Repository -> Amazon Aurora Read Replica**: Executes parameterized SQL read queries [TCP / KMS encrypted]

## Technology Stack
- **Go**: Chosen for lightweight concurrency, low memory footprint, and alignment with the 3-engineer team capacity.
- **AWS ECS (Fargate)**: Serverless container execution minimizing operational overhead within the 25,000 EUR monthly budget.
- **Amazon Aurora**: Immutable ledger database providing tamper-evident storage for 7-year audit retention (NFR R-06).
- **AWS KMS**: Customer-managed keys enforcing encryption-at-rest for historical compliance data.
- **AWS X-Ray & CloudWatch**: Distributed tracing and monitoring for performance SLAs and resource utilization alerts.

## Rationale
This architecture securely separates resource-heavy audit queries from real-time payment screening using a dedicated read replica and strict rate-limiting. It fulfills strict PCI-DSS and 7-year audit mandates while remaining maintainable by a 3-engineer team within a fixed budget.