## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books, featuring personalized recommendations and reviews. The Auth Service container manages user authentication, session security, and compliance workflows.

## Key Elements
- **Authentication Controller**: Fastify-based controller handling inbound HTTP/2 requests.
- **Token Manager**: Manages JWTs and opaque sessions.
- **Identity Provider Integration Adapter**: Federates logins via OAuth2/OIDC.
- **User Credential Repository**: Handles Argon2 password hashing and user profiles.
- **GDPR Consent Manager**: Manages data access and deletion requests.
- **Security Audit Logger**: Captures authentication failures and security events.
- **Rate Limiting & Brute-Force Guard**: Mitigates credential stuffing via sliding-window tracking.

## Relationships
- API Gateway -> Authentication Controller: Routes authentication requests [gRPC / HTTP/2]
- Token Manager -> Redis (ElastiCache): Caches sessions and revocation lists [Redis Protocol]
- User Credential Repository -> Amazon Aurora PostgreSQL: Reads/writes credentials [TLS / JDBC]
- Privacy Service -> GDPR Consent Manager: Requests user data export/deletion [gRPC]
- Security Audit Logger -> Amazon SNS/SQS: Publishes audit events [AWS SDK / HTTPS]

## Technology Stack
- **Node.js with TypeScript and Fastify**: Chosen for high-throughput I/O performance.
- **Redis (ElastiCache)**: Used for sub-millisecond session lookups and rate limiting.
- **Amazon Aurora PostgreSQL**: Secures user profiles with Argon2 hashing and TLS 1.3.
- **Amazon SNS/SQS**: Enables asynchronous security event publishing.

## Rationale
This architecture ensures GDPR/CCPA compliance through dedicated consent management and credential isolation. It meets 99.95% availability and 1M MAU scalability targets via Redis-backed session caching and rate limiting.