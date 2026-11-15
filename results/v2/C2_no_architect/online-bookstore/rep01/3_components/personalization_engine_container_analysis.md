## Overview
[The Personalization Engine Container delivers real-time "Customers also bought" recommendations to drive book sales while enforcing privacy compliance. It is deployed across AWS multi-region infrastructure to ensure high availability and low latency for global users.]

## Key Elements
*   **Personalization Engine Container:** Core recommendation service running on Amazon ECS/EKS.
*   **Data Pipeline:** Amazon SQS for asynchronous behavior event ingestion.
*   **Caching & Profiles:** Amazon ElastiCache for user affinity profiles and fallback bestsellers.
*   **Security & Encryption:** AWS KMS and S3 for cryptographic model verification and AES-256 encryption.
*   **Traffic Management:** AWS API Gateway with service-to-service mTLS and circuit breakers.

## Relationships
*   **API Gateway -> Personalization Engine Container:** Invokes recommendation endpoints via [mTLS inside AWS VPC].
*   **Personalization Engine Container -> Amazon ElastiCache:** Reads cached affinity profiles and fallback bestsellers [TCP].
*   **Personalization Engine Container -> Amazon SQS:** Insumes asynchronous user behavior telemetry [HTTPS/TLS 1.3].
*   **Personalization Engine Container -> AWS S3:** Loads cryptographically verified ML models [HTTPS/TLS 1.3 with AWS KMS].

## Technology Stack
*   **Amazon ECS/EKS:** Container orchestration across us-east-1, eu-west-1, and ap-southeast-1 for 1M MAU scalability and 99.95% uptime.
*   **Amazon ElastiCache:** In-memory caching for low-latency profile retrieval and deterministic fallback responses under 2s.
*   **Amazon SQS:** Asynchronous event broker to decouple behavior ingestion from real-time inference.
*   **AWS KMS & S3:** Cryptographic verification and storage for secure ML model integrity.
*   **AWS App Mesh / Istio:** Service mesh enforcing strict mTLS and circuit breaking.

## Rationale
[Pseudonymized data processing and consent flag filtering satisfy strict GDPR/CCPA constraints without sacrificing personalization quality. Caching, multi-region ECS/EKS scaling, and circuit breakers guarantee sub-2-second page loads and 99.95% availability under high-traffic conditions.]