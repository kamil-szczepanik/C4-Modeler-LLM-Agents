## Overview
The Online Bookstore is a scaled-down e-commerce platform providing scalable book catalog browsing, secure checkout, reviews, and personalized recommendations. The Recommendation Microservice specifically delivers real-time, personalized "Customers also bought" suggestions to drive user conversion and average order value.

## Key Elements
- Shoppers & Vendors (Users)
- API Gateway & WAF (AWS API Gateway, AWS ALB, AWS WAF)
- Recommendation Microservice (AWS ECS Fargate, Amazon ElastiCache Redis)
- Recommendation API Controller (Go)
- Experiment Router (Go)
- Scoring Engine (Python, NumPy)
- Cache & Fallback Manager (Go, go-redis)
- Cold-Start Handler (Go)
- Analytics Publisher (Go, AWS Kinesis Producer)

## Relationships
- API Gateway & WAF -> Recommendation Microservice: Requests personalized recommendations [gRPC, HTTPS, mTLS, TLS 1.3]
- Recommendation API Controller -> Experiment Router: Evaluates variant context [In-memory Go function call]
- Experiment Router -> Scoring Engine: Invokes selected model variant [gRPC over IPC]
- Scoring Engine & API Controller -> Amazon ElastiCache (Redis): Fetches and updates user state [TCP, Redis AUTH, TLS]
- Analytics Publisher -> AWS Kinesis: Emits click-through and conversion metrics [AWS SDK, HTTPS]

## Technology Stack
- AWS ECS Fargate: Container orchestration for isolated microservices and sidecar separation of I/O and CPU-bound workloads.
- Go: Powers the API Controller, Experiment Router, Cache Manager, and Analytics Publisher for high-throughput, low-latency I/O.
- Python & NumPy: Powers the Scoring Engine for efficient numerical processing of collaborative filtering algorithms.
- Amazon ElastiCache (Redis): In-memory data store with Multi-AZ, automatic failover, and KMS encryption for fast user-state caching.
- AWS Kinesis: Stream ingestion for asynchronous recommendation telemetry and analytics.

## Rationale
This architecture uses sidecar container segregation on ECS Fargate to decouple lightweight Go I/O components from CPU-bound Python scoring models, ensuring sub-2-second latency. Multi-AZ Redis caching, circuit breakers, and automated fallback logic guarantee 99.95% availability under high concurrent load.