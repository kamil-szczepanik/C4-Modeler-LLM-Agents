## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud and provides case management tools for risk analysts.]
[It ensures PCI-DSS Level 1 compliance while maintaining a low-latency, resilient decision-making pipeline.]

## Key Elements
- Fraud Analysts & Risk Managers [person]
- Payment Gateway / Acquirer [externalSystem]
- AWS Application Load Balancer (ALB) [container]
- Scoring Engine [container]
- Case Management Service [container]
- Amazon DynamoDB [container]
- AWS S3 Object Lock [container]
- AWS Cognito [externalSystem]
- Amazon CloudFront & Amazon S3 [container]

## Relationships
- Payment Gateway / Acquirer -> AWS Application Load Balancer (ALB) [gRPC/HTTPS over mTLS]
- Fraud Analysts & Risk Managers -> Amazon CloudFront [HTTPS, TLS 1.3]
- Fraud Analysts & Risk Managers -> AWS Cognito [OAuth2/OIDC]
- Amazon CloudFront -> Amazon S3 [HTTPS, Origin Access Control]
- AWS Application Load Balancer (ALB) -> Scoring Engine [gRPC/HTTPS]
- AWS Application Load Balancer (ALB) -> Case Management Service [HTTPS]
- Case Management Service -> Scoring Engine [gRPC]
- Scoring Engine -> Amazon DynamoDB [TCP, AWS IAM]
- Case Management Service -> AWS S3 Object Lock [AWS API, HTTPS]

## Technology Stack
- Java (Spring Boot / gRPC) on AWS ECS on Fargate [Scoring Engine for sub-50ms P99 latency]
- Node.js & React on AWS ECS on Fargate and Amazon S3/CloudFront [Case Management UI and API]
- Amazon DynamoDB [Low-latency feature store]
- AWS S3 Object Lock [Tamper-evident 7-year audit storage]
- AWS Cognito [Identity and access management with OAuth2/OIDC]
- AWS CloudWatch & AWS X-Ray [Centralized logging and distributed tracing]

## Rationale
[The microservices architecture on AWS ECS Fargate and DynamoDB delivers the required sub-50ms P99 latency at 3,000 TPS within a fixed 25,000 EUR monthly budget.]
[Decoupling static UI assets to S3/CloudFront and leveraging managed AWS services minimizes operational overhead for a three-engineer team while satisfying PCI-DSS Level 1 security and auditability constraints.]