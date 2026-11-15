## Overview
The Online Bookstore system is a scalable e-commerce platform for physical and electronic books, supporting global multi-currency transactions and real-time search. It provides secure browsing, checkout, recommendations, and reviews while maintaining high availability and GDPR/CCPA compliance.

## Key Elements
- Customers, Book Authors/Publishers, Store Administrators
- Amazon API Gateway, AWS App Mesh
- Single Page Application (React, TypeScript, Amazon CloudFront, Amazon S3)
- Catalogue & Search Service (Go, Amazon OpenSearch)
- Search API Controller, Indexing Worker, Query Normalizer & Spellcheck Component, Pricing & Currency Sync Handler
- Order & Checkout Service (Node.js/Java, Amazon Aurora PostgreSQL)
- Recommendation Service (Python FastAPI, Amazon DynamoDB)
- Review & Moderation Service (Node.js)
- Amazon SQS/SNS Messaging Bus with Dead-Letter Queues

## Relationships
- API Gateway -> Catalogue & Search Service: Routes search and browse requests [REST/GraphQL via mTLS]
- Search API Controller -> Amazon OpenSearch: Executes search queries [HTTPS]
- Indexing Worker -> Amazon OpenSearch: Updates document indices [HTTPS]
- Search API Controller -> Query Normalizer & Spellcheck Component: Parses raw terms [In-process Go call]
- Indexing Worker -> Pricing & Currency Sync Handler: Routes pricing events [In-process Go call]
- Catalogue & Search Service -> Amazon SQS/SNS: Publishes and consumes events [HTTPS]

## Technology Stack
- Go: Minimal memory footprint and high-throughput routing for search components
- Amazon OpenSearch: Inverted indices, faceted navigation, fuzzy matching, and multi-currency filtering
- Amazon SQS/SNS: Asynchronous event messaging with FIFO ordering and Dead-Letter Queues
- AWS KMS & Secrets Manager: Data encryption at rest and automated credential rotation

## Rationale
This architecture ensures sub-2-second search performance and multi-region resilience for 1M MAU through asynchronous event handling and decoupled Go microservices. OpenSearch and regional clustering deliver multi-currency compliance and high availability without sacrificing scalability.