## Overview
• The Audit & Event Tracking Container provides immutable logging and event processing for the Library Management System.
• It ensures regulatory compliance, data residency, and operational insights while maintaining high-performance ingestion.

## Key Elements
• Compliance Officers / Auditors: Primary users requiring tamper-evident logs for GDPR and EU data residency.
• Library Administrators: Users accessing usage insights for collection budgeting and staff allocation.
• Audit & Event Tracking Container: Microservice consuming Kafka events, managing backpressure, and generating compliance reports.
• Kafka/Redpanda Event Streaming Container: Source of system events via Kafka Protocol.
• Reporting/Analytics Container: Consumer of processed event data via Internal API and mTLS.
• WORM Object Storage: EU-region tiered storage for long-term historical logs.

## Relationships
• Kafka/Redpanda Event Streaming Container -> Audit & Event Tracking Container: Consumes events [Kafka Protocol]
• Audit & Event Tracking Container -> Reporting/Analytics Container: Populates analytics [Internal API with mTLS]
• Audit & Event Tracking Container -> WORM Object Storage: Archives compressed Parquet files [S3-compatible API with AES-256]

## Technology Stack
• Apache Kafka / Redpanda: Used for real-time event streaming with consumer lag monitoring via Prometheus.
• AES-256 with Customer-Managed Keys (CMK): Ensures encryption at rest within the EU region.
• WORM Object Storage: Guarantees tamper-resistance for long-term audit logs.
• Parquet Format: Optimized for serverless query engines during export operations.

## Rationale
• The architecture combines tiered storage and local write-ahead buffers to handle backpressure and scalability without dropping compliance events.
• Cryptographic chaining, data minimization, and strict access controls satisfy EU data residency and GDPR mandates.