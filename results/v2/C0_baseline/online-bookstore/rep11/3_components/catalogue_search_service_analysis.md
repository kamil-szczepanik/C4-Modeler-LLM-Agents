## Overview
[The Online Bookstore Catalogue & Search Service is a containerized microservice that handles high-performance product discovery, faceted filtering, and keyword search for 1M MAU. It ensures low-latency responses, regional availability, and robust fallback mechanisms across AWS cloud regions.]

## Key Elements
- [Search API Controller (Node.js / Express)]
- [Search Query Engine (Node.js)]
- [Database Fallback Handler (Node.js)]
- [Catalogue Sync Worker (Node.js)]
- [Amazon OpenSearch]
- [Amazon ElastiCache (Redis)]
- [Amazon RDS (PostgreSQL)]
- [Amazon API Gateway / Application Load Balancer]

## Relationships
- [API Gateway -> Search API Controller: Routes search queries via HTTPS / REST]
- [Search API Controller -> Search Query Engine: Delegates query processing via in-memory function call]
- [Search Query Engine -> Amazon OpenSearch: Executes search and aggregations via HTTP / REST with AWS SigV4]
- [Search Query Engine -> Database Fallback Handler: Triggers fallback on circuit breaker trip via internal function call]
- [Database Fallback Handler -> Amazon ElastiCache (Redis): Retrieves cached search payloads via Redis protocol]
- [Catalogue Sync Worker -> Amazon OpenSearch: Synchronizes catalogue index via asynchronous events]

## Technology Stack
- [AWS ECS / Fargate: Serverless container orchestration for scalability and auto-scaling]
- [Amazon OpenSearch: Primary search engine for fast keyword lookup and faceted aggregations]
- [Node.js / Express: Lightweight, high-performance runtime for API controllers and workers]
- [Amazon ElastiCache (Redis): Caching layer for fast fallback responses during outages]
- [AWS IAM & Secrets Manager: Credential-less task authentication and automated secret rotation]

## Rationale
[This architecture decouples search from the primary database using OpenSearch and Redis caching, guaranteeing sub-2-second page loads and high availability. It integrates robust security controls, strict input sanitization, and least-privilege networking to meet compliance, scalability, and uptime goals.]