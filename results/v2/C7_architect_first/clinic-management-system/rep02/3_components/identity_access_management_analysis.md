## Overview
The Identity & Access Management container provides secure authentication, multi-factor authentication, fine-grained access control, and identity federation for the Clinic Management System. It ensures strict HIPAA and GDPR compliance while maintaining high availability (99.99%) and low-latency clinical access.

## Key Elements
* Authentication Engine (Keycloak Core)
* Token Service
* Policy Decision Point (PDP)
* Audit Logger
* Caching & Redis Cluster
* User & Role Sync Service
* Identity Federation Adapter

## Relationships
* API Gateway -> Token Service: Validates incoming JWTs [gRPC / Internal REST]
* Policy Decision Point -> Caching & Redis Cluster: Evaluates access rules [Redis Protocol]
* Audit Logger -> Message Broker (Kafka): Publishes security events [Kafka Protocol]
* Authentication Engine -> Identity Federation Adapter: Delegates external patient logins [OIDC / SAML]
* User & Role Sync Service -> Caching & Redis Cluster: Syncs user roles asynchronously [Redis Protocol]

## Technology Stack
* Keycloak Core: Manages credentials, federation, and MFA to ensure robust IAM.
* JSON Web Tokens (JWT): Uses asymmetric keys (RS256/ES256) for stateless, secure session handling.
* Redis Cluster: Provides in-memory caching for sub-millisecond RBAC evaluations.
* Apache Kafka: Handles asynchronous audit logging to meet 10-year retention rules.
* OpenTelemetry: Enables distributed tracing to prevent latency spikes.

## Rationale
This architecture decouples authorization from database calls using Redis caching and asynchronous sync workers, safeguarding the 99.99% uptime target. It balances rigorous HIPAA/GDPR security controls (like NIST 800-63 IAL2 and JIT Break-Glass) with frictionless clinical workflows.