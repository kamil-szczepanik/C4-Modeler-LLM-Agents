## Overview
The Event Broker provides real-time, fault-tolerant message streaming for the Real-Time Payment Fraud Screening system. It decouples high-throughput card-not-present payment authorizations while ensuring strict auditability and PCI-DSS Level 1 compliance.

## Key Elements
- **Topic Router & Partition Manager**: Manages topic creation, partition assignment, and high-throughput routing using hashed card ID keys.
- **Access Control & Auth Enforcer**: Validates mutual TLS (mTLS) certificates and enforces Kafka ACLs to isolate the `audit-log` topic.
- **Storage & Replication Engine**: Handles 3-AZ log replication and encrypted-at-rest persistence via AWS KMS CMKs.
- **Producers & Consumers**: Real-Time Scoring Engine, Audit Log Sitter, and Case Management API.
- **Infrastructure Services**: AWS Secrets Manager, S3 Object Lock, and AWS CloudWatch.

## Relationships
- Real-Time Scoring Engine -> Topic Router: Publishes authorization events and telemetry [TCP/TLS 1.3, Kafka Protocol]
- Topic Router -> Audit Log Sitter: Streams audit events via dedicated consumer group [TCP/TLS 1.3, Kafka Protocol]
- Topic Router -> Case Management API: Streams events for case creation [TCP/TLS 1.3, Kafka Protocol]
- Access Control & Auth Enforcer -> AWS Secrets Manager: Validates mTLS certificates and credentials [HTTPS/TLS 1.3]
- Storage Engine -> S3 Object Lock Bucket: Offloads tamper-evident audit streams asynchronously [AWS PrivateLink]

## Technology Stack
- **AWS MSK (Managed Kafka)**: Provisioned `kafka.m5.large` instances across 3 Availability Zones to guarantee high availability and stable cost control under 25,000 EUR/month.
- **TLS 1.3 & mTLS**: Secures all data-in-transit and authenticates internal services.
- **AWS KMS**: Provides customer-managed keys for encryption-at-rest.
- **Terraform / GitHub Actions**: Automates infrastructure provisioning and zero-downtime deployments.

## Rationale
Provisioned AWS MSK with 3-AZ deployment reliably sustains 3,000 TPS under the 50 ms latency threshold while maintaining a strict budget for a 3-engineer team. Strict topic isolation and S3 Object Lock meet 7-year tamper-evident auditability and PCI-DSS Level 1 compliance mandates.