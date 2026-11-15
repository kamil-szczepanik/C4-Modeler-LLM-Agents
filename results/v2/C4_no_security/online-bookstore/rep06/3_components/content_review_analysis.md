## Overview
[The Online Bookstore Content & Review component manages customer ratings and reviews to drive user trust and engagement. It processes high-throughput read operations while supporting automated moderation and compliance requirements.]

## Key Elements
* Customers (Shoppers)
* Store Staff & Administrators
* Content & Review Container (Node.js, Express.js)
* Amazon API Gateway
* Amazon DocumentDB
* Amazon ElastiCache (Redis)
* Amazon SQS (with Dead Letter Queue)
* AWS Comprehend
* Admin Back-Office

## Relationships
* API Gateway -> Content & Review Container: Routes internal traffic via VPC links [gRPC]
* Content & Review Container -> Amazon ElastiCache (Redis): Reads cached reviews and metadata [Redis Protocol]
* Content & Review Container -> Amazon DocumentDB: Persists and retrieves reviews [MongoDB wire protocol via TLS]
* Content & Review Container -> Amazon SQS: Publishes review payloads for async moderation [AWS SDK / HTTPS]
* Moderation Service -> AWS Comprehend: Analyzes text toxicity and sentiment [AWS SDK / HTTPS]

## Technology Stack
* Node.js & Express.js: Runtime and web framework for low-latency REST APIs
* Amazon DocumentDB: JSON-native document database for flexible review schemas and horizontal scalability
* Amazon ElastiCache (Redis): Caching layer for sub-millisecond review reads and cache stampede protection
* Amazon SQS & DLQ: Asynchronous queue for decoupling moderation workflows and ensuring reliability
* AWS Comprehend: Managed ML service for automated sentiment and toxicity analysis

## Rationale
[This architecture utilizes an asynchronous caching and queuing pattern to maintain sub-millisecond read latencies, ensuring page load times remain under 2 seconds. Decoupling the moderation pipeline via Amazon SQS preserves system availability and fault tolerance for 1M MAU.]