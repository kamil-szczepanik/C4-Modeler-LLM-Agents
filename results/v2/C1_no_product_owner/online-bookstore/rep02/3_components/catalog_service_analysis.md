## Overview
The Online Bookstore system is a multi-region e-commerce platform providing physical and electronic book purchasing, recommendations, and reviews. It utilizes a resilient, event-driven microservices architecture on AWS to ensure high scalability and compliance.

## Key Elements
* **Catalog API Controller (Node.js/Express):** Handles incoming gRPC requests, schema validation, and JWT-based role authorization.
* **Search & Browse Engine (Node.js & Amazon OpenSearch):** Manages complex keyword searching, filtering, and query sanitization.
* **Catalog Data Repository (Node.js ODM/Mongoose):** Manages book metadata CRUD operations against Amazon DocumentDB.
* **Catalog Sync Worker (Node.js background process):** Consumes asynchronous update events via Amazon SQS to synchronize search indices.

## Relationships
* **AWS API Gateway -> Catalog API Controller:** Routes catalog requests [gRPC over mTLS]
* **Catalog API Controller -> Catalog Data Repository:** Executes metadata operations [In-memory function calls]
* **Catalog Data Repository -> Amazon DocumentDB:** Persists catalog data [TCP/TLS]
* **Catalog Data Repository -> Amazon SQS:** Publishes `CatalogItemUpdated` domain events [HTTPS]
* **Catalog Sync Worker -> Amazon SQS:** Polls and consumes update messages [HTTPS]
* **Catalog Sync Worker -> Amazon OpenSearch Service:** Updates search indices [HTTPS with AWS SigV4]

## Technology Stack
* **Node.js/Express:** Core runtime for scalable, lightweight microservices and background workers.
* **Amazon OpenSearch Service:** Dedicated search engine to guarantee sub-2-second page load performance.
* **Amazon DocumentDB:** NoSQL document database for flexible storage of book metadata.
* **Amazon SQS & EventBridge:** Decouples write operations from search indexing via asynchronous messaging.
* **AWS KMS & TLS 1.3:** Ensures end-to-end data encryption in transit and at rest for GDPR/CCPA compliance.

## Rationale
This architecture uses event-driven CQRS patterns and specialized search datastores to decouple write operations from read-heavy catalog browsing. This design directly satisfies stringent availability, security, and performance constraints under high global traffic.