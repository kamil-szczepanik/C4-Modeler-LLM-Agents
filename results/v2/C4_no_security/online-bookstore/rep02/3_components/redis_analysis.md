## Overview
[The Online Bookstore system provides a scalable, Amazon-style e-commerce platform for purchasing physical and electronic books, offering catalog search, secure checkout, reviews, and personalized recommendations.]

## Key Elements
* Redis (AWS ElastiCache): In-memory data store and caching layer
* Catalog Cache Component (Redis Strings/Hashes)
* Session & Cart Store Component (Redis Hashes/Sets)
* Rate Limiter Component (Redis Atomic Counters)
* Real-Time Recommendation Cache Component (Redis Sorted Sets/Hashes)
* Catalog & Search Service, Order & Checkout Service, Personalization Service, API Gateway

## Relationships
* Catalog & Search Service -> Catalog Cache Component: Caches catalog data [Redis Protocol / TCP]
* Order & Checkout Service -> Session & Cart Store Component: Read/Write active carts [Redis Protocol / TCP, port 6379]
* API Gateway -> Rate Limiter Component: Check and increment request counters [Redis Protocol / TCP, port 6379]
* Personalization Service -> Real-Time Recommendation Cache Component: Read trending pairs [Redis Protocol / TCP, port 6379]

## Technology Stack
* AWS ElastiCache for Redis: Provides managed in-memory storage with Cluster Mode for scalability
* Lettuce / Redis-py: Client libraries utilizing connection pooling over TLS-encrypted TCP
* Amazon CloudWatch: Monitors cache performance metrics (`DBCPUUtilization`, `EngineMemoryUsed`)
* Amazon S3: Stores daily RDB snapshots for persistence backup

## Rationale
[This Redis-centered architecture ensures sub-2-second page loads and 99.95% uptime for 1M MAU. Multi-AZ deployment and hybrid persistence guarantee reliable shopping cart sessions and secure checkout operations.]