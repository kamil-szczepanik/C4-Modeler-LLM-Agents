## Overview
Amazon ECR provides a secure, private container registry to store, version, and scan immutable runtime images for the Fraud Screening Engine and FastAPI Backend. It ensures PCI-DSS compliance and reliable zero-downtime deployments while staying within the 25,000 EUR monthly budget.

## Key Elements
- **Registry Repository Store**: AWS ECR repository storing Docker image layers encrypted with AES-256 via AWS KMS customer-managed keys.
- **Vulnerability Scanning Engine**: Amazon Inspector integration scanning images upon push to enforce security gates.
- **Lifecycle & Immutability Manager**: Enforces image immutability tags and retention policies to prune old artifacts.

## Relationships
- **CI/CD Pipeline** pushes built images to **Registry Repository Store** via HTTPS (TLS 1.3) using IAM role-based authentication.
- **Amazon ECS on EC2** pulls runtime images from **Registry Repository Store** via AWS VPC Endpoints (PrivateLink) using HTTPS (TLS 1.3).

## Technology Stack
- **Amazon ECR**: Container image registry chosen for managed scalability and zero-infrastructure overhead.
- **AWS KMS**: Customer-managed keys for encryption at rest to satisfy strict auditability requirements.
- **Amazon Inspector**: Automated vulnerability scanning to meet PCI-DSS compliance gates.
- **AWS CloudTrail**: Data event logging for all repository actions to meet 7-year audit requirements.

## Rationale
This architecture uses fully managed AWS services to minimize operational burden for a three-engineer team. Strict immutability, vulnerability gating, and least-privilege IAM controls ensure PCI-DSS Level 1 compliance and sub-50ms performance without exceeding the infrastructure budget.