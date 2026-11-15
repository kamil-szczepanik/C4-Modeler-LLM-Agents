## Overview
[A secure, low-latency data storage layer built on AWS Aurora PostgreSQL and Amazon ElastiCache Serverless Redis powers real-time payment fraud screening and case management.]

## Key Elements
* Feature Store: Amazon ElastiCache Serverless Redis cluster for high-velocity transaction features.
* Operational & Audit Database: AWS Aurora PostgreSQL Multi-AZ for case management and transaction history.
* Audit Archive Exporter: AWS Lambda function with Amazon EventBridge scheduling.
* Security Controls: AWS KMS Customer-Managed Keys (CMKs) and AWS Security Groups.
* External Storage: Amazon S3 Glacier Vault with Object Lock.

## Relationships
* Fraud Scoring Engine -> Feature Store: Fetches real-time transaction features via RESP / TLS 1.3.
* Case Management Service -> Operational & Audit Database: Persists analyst reviews via PostgreSQL Wire Protocol / TLS 1.3.
* Audit Archive Exporter -> Secure Audit Archive: Transfers immutable audit logs via HTTPS / TLS 1.3.

## Technology Stack
* Amazon ElastiCache Serverless Redis: Provides sub-millisecond feature reads to meet P99 latency targets.
* AWS Aurora PostgreSQL Multi-AZ: Ensures reliable relational storage for compliance and case management.
* AWS Lambda & Amazon EventBridge: Automates serverless log archiving with minimal operational overhead.
* Amazon S3 Glacier Vault: Implements tamper-evident, cost-effective 7-year audit retention.
* AWS KMS: Enforces column-level encryption and AES-256 data protection.

## Rationale
[This dual-engine storage architecture balances sub-50ms performance requirements with strict PCI-DSS compliance and a 7-year audit mandate. Furthermore, serverless components minimize operational toil for a three-engineer team while respecting the 25,000 EUR monthly budget.]