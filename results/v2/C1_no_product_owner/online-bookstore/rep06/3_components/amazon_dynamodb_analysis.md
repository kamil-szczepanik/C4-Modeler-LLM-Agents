## Overview
- Internal C4 component architecture for the Amazon DynamoDB container within an AWS-hosted online bookstore.
- Provides scalable, low-latency cart and session persistence with multi-region replication and GDPR/CCPA compliance.

## Key Elements
- Request Router & Coordinator (AWS Distributed Request Router)
- Storage Node Engine (B-tree / LSM-tree on AWS Nitro)
- Replication & Consensus Manager (AWS Multi-AZ Paxos Consensus)
- DynamoDB Streams Processor (DynamoDB Streams API)
- AWS PrivateLink (VPC Endpoints)
- AWS KMS (Customer Managed Keys)

## Relationships
- Order & Checkout -> Request Router & Coordinator: Executes low-latency cart operations via AWS SDK [HTTPS / TLS]
- Order & Checkout -> Request Router & Coordinator: Connects via VPC Endpoints [AWS PrivateLink]
- Request Router & Coordinator -> DynamoDB Streams Processor: Triggers change events [Internal AWS IPC / TCP]
- DynamoDB Streams Processor -> Message Bus: Publishes CDC events [HTTPS / AWS SDK]

## Technology Stack
- Amazon DynamoDB Global Tables: Active-active multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for 99.95% availability.
- AWS KMS (CMK): Encryption at rest and across global table replicas for GDPR/CCPA compliance.
- DynamoDB Streams: Asynchronous change data capture for cart abandonments and analytics.
- AWS PrivateLink: Zero-trust network isolation preventing public internet exposure.

## Rationale
- Distributed consensus and auto-scaling deliver high availability and sub-second performance for 1M MAU.
- Strict IAM policies, VPC endpoints, and KMS encryption satisfy rigorous security and data privacy mandates.