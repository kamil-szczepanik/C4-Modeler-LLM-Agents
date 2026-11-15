## Overview
The AWS App Mesh & Security component secures internal microservice communication and manages sensitive data for the Online Bookstore. It enforces strict zero-trust boundaries, encryption at-rest and in-transit, and compliance with GDPR/CCPA standards.

## Key Elements
* **Envoy Proxy Sidecar**: Envoy/AWS App Mesh injected into every microservice pod
* **Secrets Controller**: AWS Secrets Manager and External Secrets Operator
* **Key Management Daemon**: AWS KMS for envelope encryption
* **Mesh Control Plane**: AWS App Mesh Controller and AWS IAM
* **Telemetry & Audit Router**: AWS CloudWatch and AWS X-Ray
* **Certificate Authority**: AWS Certificate Manager (ACM) Private CA

## Relationships
* *Catalog, Checkout, & other Containers* -> *Envoy Proxy Sidecar*: Localhost loopback [gRPC/HTTP]
* *Envoy Proxy Sidecar* <-> *Envoy Proxy Sidecar*: Cross-service communication [Mutual TLS over TCP/Port 443]
* *Services* -> *Secrets Controller*: Fetch runtime secrets [HTTPS/AWS SDK]
* *Envoy Proxy Sidecar* -> *Mesh Control Plane*: Fetch dynamic routing and certificate updates [gRPC with local caching fallback]
* *Envoy Proxy Sidecar* -> *Telemetry & Audit Router*: Export metrics and access logs [OTLP/HTTPS]

## Technology Stack
* **AWS App Mesh & Envoy**: Handles traffic routing, service discovery, and mTLS encryption with low latency.
* **AWS Secrets Manager & KMS**: Secures runtime credentials and manages data at rest with strict IAM scoping.
* **AWS Certificate Manager (ACM)**: Automates 24-hour certificate rotation with local Envoy caching for high availability.
* **AWS CloudWatch & X-Ray**: Captures access logs, mTLS handshake metrics, and distributed traces for compliance audits.

## Rationale
This architecture ensures robust zero-trust security and GDPR/CCPA compliance without violating performance or availability SLAs. Local certificate caching and rolling updates prevent cascading infrastructure failures, protecting the 99.95% uptime requirement.