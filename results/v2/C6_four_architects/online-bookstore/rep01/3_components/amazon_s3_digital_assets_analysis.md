## Overview
The Online Bookstore system is a scalable e-commerce platform for physical and electronic books with recommendations and reviews. The architecture secures digital e-book assets using AWS-native components to ensure compliance and performance.

## Key Elements
- Customer SPA (React, Amazon S3, CloudFront)
- Order & Checkout Service (Node.js)
- Asset Management Controller (Go / AWS Lambda)
- CloudFront Signer Component (Go SDK)
- S3 Private Storage Bucket (Amazon S3, AES-256)
- Access Audit Monitor (Amazon CloudFront Standard Logs / CloudWatch)
- Bucket Policy Enforcer (AWS IAM / S3 Bucket Policy)

## Relationships
- Customer SPA -> Asset Management Controller: Requests download token via [HTTPS / REST]
- Asset Management Controller -> CloudFront Signer Component: Requests signed URL generation via [In-process Go function]
- CloudFront Signer Component -> Order & Checkout Service: Validates purchase entitlement via [gRPC / HTTPS]
- CloudFront Edge -> S3 Private Storage Bucket: Retrieves objects via [HTTPS / AWS IAM Origin Access Control (OAC)]

## Technology Stack
- Go: Used for high-performance asset management and signing logic
- Amazon S3: Encrypted private object storage (AES-256) for binary e-book assets
- Amazon CloudFront: CDN utilizing Signed URLs and Origin Access Control (OAC) for secure delivery
- AWS IAM: Enforces strict bucket policies preventing public access

## Rationale
This architecture ensures secure, zero-exposure e-book delivery while meeting GDPR and CCPA compliance constraints. It leverages AWS-native security controls to satisfy strict non-functional security requirements (R-08) without impacting global scalability.