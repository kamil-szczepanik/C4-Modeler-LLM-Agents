## Overview
This architecture defines the Search & Analytics Service for an online bookstore supporting keyword search and review indexing. It utilizes serverless compute and managed caching to deliver high performance and scalability.

## Key Elements
- **Query API Controller**: Node.js/TypeScript on AWS Lambda
- **Indexing Worker**: Python on AWS Lambda
- **Analytics Aggregator**: Python on AWS Lambda
- **Search Cache Layer**: Amazon ElastiCache for Redis
- **OpenSearch Index Cluster**: Amazon OpenSearch Service
- **AWS API Gateway**
- **Amazon SQS / Amazon EventBridge**

## Relationships
- **AWS API Gateway** -> **Query API Controller**: Routes search requests [HTTPS/REST]
- **Query API Controller** -> **Search Cache Layer**: Caches frequent query results [Redis protocol]
- **Query API Controller** -> **OpenSearch Index Cluster**: Executes full-text searches [HTTPS/REST]
- **Amazon SQS** -> **Indexing Worker**: Triggers index updates [JSON over SQS]
- **Indexing Worker** -> **OpenSearch Index Cluster**: Bulk updates and indexes data [HTTPS/REST]
- **Analytics Aggregator** -> **Amazon EventBridge**: Publishes clickstream metrics [JSON over EventBridge]

## Technology Stack
- **AWS Lambda**: Minimizes operational overhead for intermittent query translation and indexing workloads.
- **Amazon OpenSearch Service**: Provides distributed full-text search and analytical capabilities.
- **Amazon ElastiCache for Redis**: Delivers ultra-low latency caching to meet performance goals.
- **Amazon SQS & EventBridge**: Enables reliable asynchronous event-driven synchronization.

## Rationale
The serverless and cached architecture ensures sub-second response times under heavy concurrent load, meeting strict scalability and performance requirements. Decoupled asynchronous components maintain high availability and fault tolerance.