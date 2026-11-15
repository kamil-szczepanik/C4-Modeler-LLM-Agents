## Overview
The Recommendation Engine Container delivers personalized, privacy-compliant book recommendations to enhance user engagement for the global online bookstore. It ensures high availability and low latency across multiple AWS regions while supporting GDPR and CCPA regulations.

## Key Elements
* Customer (Shopper): Primary user requesting book suggestions.
* Recommendation Engine Container: Core microservice deployed on Amazon EKS.
* Redis Sidecar: Caches pre-computed recommendations and user affinity profiles.
* Amazon S3: Stores model weights and pre-computed recommendation embeddings with KMS encryption.
* Amazon MSK (Kafka): Streams asynchronous real-time inventory updates.
* Istio Service Mesh: Manages mTLS, traffic routing, and circuit breaking.

## Relationships
* API Gateway -> Recommendation Engine Container: Routes internal inference requests [mTLS via Istio service mesh]
* Recommendation Engine Container <-> Amazon S3: Fetches model weights and embeddings [AWS IAM Roles for Service Accounts / TLS 1.3]
* Amazon MSK -> Redis Sidecar: Streams real-time inventory updates asynchronously [Kafka protocol]
* Recommendation Engine Container -> Redis Sidecar: Retrieves cached recommendations [TCP / AES-256]

## Technology Stack
* Amazon EKS: Container orchestration ensuring scalability via Horizontal Pod Autoscalers.
* Redis: Sidecar caching layer for sub-200ms response times.
* Amazon MSK (Kafka): Event bus for decoupled, real-time inventory synchronization.
* AWS IAM Roles for Service Accounts (IRSA): Least-privilege access control for AWS resources.
* AWS KMS & AES-256: Encryption at rest for cached data and model weights.

## Rationale
This architecture meets sub-200ms latency and high scalability requirements through decoupled asynchronous events and local caching. Security controls, S3 cross-region replication, and strict data anonymization guarantee multi-region resilience and GDPR/CCPA compliance.