## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site for purchasing physical and electronic books with recommendations and reviews. This architecture defines the internal components of the Recommendations Container to deliver high-performance, personalized suggestions.

## Key Elements
- Recommendation API Router (FastAPI / Python)
- Collaborative Filtering Engine (Python / NumPy & SciPy)
- Recommendation Service (Python)
- Cache & Persistence Access Layer (SQLAlchemy / Boto3)
- In-Memory Cache (Redis / Amazon ElastiCache)

## Relationships
- Recommendation API Router -> Recommendation Service: Direct function calls (In-memory) [gRPC over TLS]
- Recommendation Service -> Collaborative Filtering Engine: Invokes recommendation scoring algorithms [In-memory]
- Recommendation Service -> In-Memory Cache: Reads cached recommendation payloads [RESP over TCP / TLS]
- Recommendation Service -> Cache & Persistence Access Layer: Orchestrates data retrieval [In-memory]
- Cache & Persistence Access Layer -> Amazon Aurora PostgreSQL & Amazon DynamoDB: Reads and writes recommendation data [SQL / NoSQL over TLS]
- Cache & Persistence Access Layer -> In-Memory Cache: Fallback population on cache misses [RESP over TCP]

## Technology Stack
- FastAPI & Python: Provides high-performance asynchronous API endpoints for real-time recommendation delivery.
- NumPy & SciPy: Enables efficient computation of collaborative filtering and recommendation vectors.
- Redis / Amazon ElastiCache: Caches pre-computed vectors and lists to ensure low-latency responses under high concurrency.
- SQLAlchemy & Boto3: Manages persistence access to Amazon Aurora PostgreSQL and Amazon DynamoDB securely over TLS.

## Rationale
This component architecture separates heavy computational workloads from real-time API request handling to maintain sub-second page loads. Caching strategies and asynchronous processing ensure high availability and scalability to meet the 1M MAU requirement.