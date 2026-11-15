## Overview
The Localization/Currency component provides multi-currency (USD, EUR, GBP) and localized content support for the global e-commerce platform. It ensures low-latency currency conversion, automated geo-detection, and secure user-explicit preference overrides.

## Key Elements
- **Book Buyer**: End-user interacting with the store and currency selectors.
- **AWS CloudFront & WAF**: Edge service handling Geo-IP resolution via viewer headers and routing.
- **AWS Lambda@Edge**: Edge compute for initial request localization and header processing.
- **Localization/Currency Container (Amazon ECS/EKS)**: Core backend component managing currency logic and overrides.
- **AWS ElastiCache (Redis)**: Distributed cache storing synced exchange rates globally via Global Datastores.
- **AWS EventBridge & Lambda**: Background worker pipeline for periodic exchange rate synchronization.
- **AWS Secrets Manager**: Secure storage for third-party exchange rate API keys.

## Relationships
- **AWS CloudFront & WAF -> Localization/Currency**: Routes requests via HTTPS / mTLS over AWS App Mesh.
- **AWS EventBridge & Lambda -> External Exchange Rate APIs**: Fetches market rates periodically via HTTPS.
- **Localization/Currency -> AWS ElastiCache**: Reads cached exchange rates via Redis protocol.
- **Localization/Currency -> AWS Secrets Manager**: Retrieves API credentials securely using AWS SDK.

## Technology Stack
- **Amazon ECS/EKS**: Container orchestration for scalable microservice deployment.
- **AWS ElastiCache Redis**: Distributed caching for low-latency exchange rate retrieval (<2s page load).
- **AWS App Mesh & mTLS**: Secures service-to-service communication within the mesh.
- **AWS Secrets Manager**: Isolates sensitive API credentials with automatic rotation.

## Rationale
Decoupling exchange rate fetching via asynchronous background sync and regional ElastiCache replication prevents single points of failure, protecting the 99.95% uptime SLA and <2s page load requirement. Offloading geo-detection to the edge combined with secure session-bound overrides ensures regulatory compliance (GDPR/CCPA) and an optimized global user experience.