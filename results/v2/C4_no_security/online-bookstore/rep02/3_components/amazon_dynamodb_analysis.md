## Overview
The Amazon DynamoDB container provides low-latency NoSQL storage for the Online Bookstore's personalization and review services. It supports high-scale e-commerce operations across multiple global regions.

## Key Elements
* Request Router / API Frontend
* Storage Nodes (Partition Engine)
* Replication Engine
* TTL Background Evaluator
* Streams Processor

## Relationships
* Personalization Service -> Request Router: Reads/writes user preference and recommendation data via AWS SDK over TLS
* Customer Review Service -> Request Router: Reads/writes review data via AWS SDK over TLS
* Streams Processor -> Amazon EventBridge: Publishes item-level modification events using native AWS service-to-service integration over TLS

## Technology Stack
* Amazon DynamoDB Global Tables: Multi-region active-active replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for low international latency.
* DynamoDB On-Demand Capacity: Handles unpredictable 1M MAU traffic spikes and flash sales without manual tuning.
* DynamoDB Streams: Captures real-time item modifications for asynchronous event-driven architecture integration.
* DynamoDB Time-to-Live (TTL): Automatically expires temporary data to support GDPR and CCPA compliance.
* AWS KMS: Customer-managed keys with automatic rotation for encryption at rest.

## Rationale
This architecture ensures single-digit millisecond latency to meet strict <2s page load requirements while automatically scaling for 1M MAU. Global deployment and automated compliance features satisfy multi-region and regulatory constraints.