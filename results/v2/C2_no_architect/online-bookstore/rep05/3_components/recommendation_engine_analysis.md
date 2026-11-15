## Overview
The Recommendation Engine provides real-time personalized book recommendations for the Online Bookstore's 1M MAU. It balances high-performance delivery with strict GDPR/CCPA compliance and multi-region resilience.

## Key Elements
*   **Registered Shopper:** Primary user leveraging the discovery and recommendation features.
*   **Web Frontend:** SPA/SSR interface consuming recommendations via gRPC.
*   **Recommendation Engine Container:** Core service hosted on AWS ECS/EKS handling inference.
*   **Feature Store / Data Pipeline:** Asynchronous offline training via AWS SageMaker and Airflow on Spot instances.
*   **Caching & Resiliency Layer:** Edge CDN and in-memory Redis cluster for fallback payloads and circuit breaking.

## Relationships
*   **Web Frontend -> Recommendation Engine:** Fetches personalized recommendations using gRPC over mTLS with JWT user propagation.
*   **Recommendation Engine -> AWS S3:** Ingests cryptographically verified model weights (sigstore/Notation) across multi-region buckets (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
*   **Recommendation Engine -> Redis / Edge CDN:** Serves cached public trending fallback payloads to anonymous or unauthenticated users.

## Technology Stack
*   **Compute:** AWS ECS/EKS for containerized gRPC microservices and automated scaling.
*   **ML & Training:** AWS SageMaker and Apache Airflow on Spot instances for cost-optimized asynchronous model training.
*   **Security & Compliance:** mTLS, JWT scope validation, AWS X-Ray for distributed tracing, and automated TTL pipelines for GDPR/CCPA data purges.
*   **Caching:** Redis and Edge CDN for low-latency cold-start fallbacks and traffic shielding.

## Rationale
This architecture scales horizontally to handle 1M MAU across multiple global regions while maintaining 99.95% uptime and sub-2-second page loads. Decoupling asynchronous model training from real-time gRPC inference guarantees low-latency performance and strict regulatory compliance.