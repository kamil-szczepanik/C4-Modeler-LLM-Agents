## Overview
• Cloud-native, Amazon-style online bookstore offering physical and electronic books, reviews, and recommendations.
• Designed to scale globally while ensuring high availability, strict security, and GDPR/CCPA compliance.

## Key Elements
• Customer (Shopper)
• Registered Reviewer / Community Member
• Store Administrator / Content Moderator
• Online Bookstore Software System
• Payment Gateway (Stripe/PayPal)
• Shipping Provider APIs (FedEx/UPS)
• Identity & Notification Service (AWS SES)

## Relationships
• Users -> Online Bookstore: HTTPS (TLS 1.3)
• Online Bookstore -> Payment Gateway: HTTPS/REST with mTLS
• Online Bookstore -> Shipping Provider APIs: HTTPS/REST via AWS SQS async queuing
• Online Bookstore -> Identity & Notification Service: HTTPS/SMTP
• Containers -> Containers: mTLS and SPIFFE/SPIRE via AWS App Mesh

## Technology Stack
• AWS Cloud (us-east-1, eu-west-1, ap-southeast-1): Multi-region deployment for global performance.
• Amazon Route 53: Latency-based routing for sub-2s page loads.
• AWS ECS/EKS: Independent container architecture for checkout, catalog, and reviews.
• AWS Secrets Manager & KMS: Secure credential injection and PII encryption at rest.
• AWS X-Ray & CloudWatch: Centralized observability, tracing, and autoscaling.

## Rationale
• Decoupled micro-containers and multi-region AWS routing ensure 99.95% uptime and scalability for 1M MAU.
• Strict adherence to TLS 1.3, mTLS, AWS KMS encryption, and audit logging guarantees GDPR/CCPA and OWASP compliance.