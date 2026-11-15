## Overview
The system screens card-not-present payment authorizations for fraud in real time and enables analysts to review suspicious transactions. It provides low-latency fraud decisions while maintaining strict compliance, auditability, and a fixed infrastructure budget.

## Key Elements
- **Shard Routing & Ingestion Service**: AWS-managed ingress handling partition key hashing.
- **Partition Log & Storage Engine**: AWS-managed immutable, append-only log storage.
- **Enhanced Fan-Out Consumer Endpoints**: Dedicated HTTP/2 throughput channels via KCL.
- **Data Retention & Replay Controller**: AWS-managed component enforcing log retention.
- **Real-Time Scoring Engine**: Publishes events via HTTPS (AWS SDK).
- **Audit Worker**: Consumes event streams via HTTP/2 (KCL).

## Relationships
- **Real-Time Scoring Engine** -> **Shard Routing & Ingestion Service**: Publishes payment events [HTTPS (AWS SDK)]
- **Partition Log & Storage Engine** -> **Data Retention & Replay Controller**: Manages time-based log rotation [AWS Internal API]
- **Partition Log & Storage Engine** -> **Enhanced Fan-Out Consumer Endpoints**: Feeds real-time event streams [AWS Internal Protocol]
- **Enhanced Fan-Out Consumer Endpoints** -> **Audit Worker**: Delivers push-based event streams [HTTP/2 (KCL)]

## Technology Stack
- **Amazon Kinesis Data Streams**: Fully managed streaming service chosen to handle 3,000 TPS with zero infrastructure overhead.
- **AWS Kinesis Client Library (KCL)**: Consumes event streams reliably via HTTP/2 for downstream auditing.
- **AWS Internal Protocols**: Utilized for secure, low-latency cross-component communication within the AWS cloud.

## Rationale
The managed streaming architecture meets high-throughput and low-latency performance targets without exceeding the 3-engineer operational capacity. It satisfies PCI-DSS Level 1 compliance and 7-year tamper-evident auditability constraints through serverless AWS primitives.