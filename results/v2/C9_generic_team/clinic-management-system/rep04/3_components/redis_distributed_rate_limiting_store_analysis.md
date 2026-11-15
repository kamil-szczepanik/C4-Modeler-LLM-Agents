## Overview
The Clinic Management System is a clinical IT solution designed to handle patient records, scheduling, billing, and admissions for medium-sized healthcare facilities. It utilizes a distributed Redis store to provide low-latency caching and rate-limiting while adhering to strict HIPAA and GDPR compliance standards.

## Key Elements
- Redis Distributed Rate Limiting Store
- API Gateway
- Core Domain Containers
- OpenTelemetry Observability Container
- Kubernetes Orchestration Platform

## Relationships
- API Gateway interacts with Redis Distributed Rate Limiting Store via Redis Protocol (RESP) over TLS for rate limiting.
- Consuming services connect to Redis via client-side connection pooling using TCP with TLS.
- OpenTelemetry scrapes telemetry and Redis metrics (`evicted_keys`, `used_memory_rss`) via HTTP/gRPC.

## Technology Stack
- Redis: Chosen for ephemeral caching and distributed rate limiting with low latency.
- Lua Scripts: Executed atomically within Redis for Token Bucket/Sliding Window algorithms.
- OpenTelemetry: Implemented for distributed tracing and Redis performance monitoring.
- Testcontainers: Utilized in CI/CD for integration testing against real Redis instances.

## Rationale
This architecture ensures 99.99% availability by offloading ephemeral state from transactional databases and implementing fail-open fallback mechanisms. Strict security baselines and hybrid cloud compatibility protect sensitive healthcare data without sacrificing performance.