## Overview
[Real-Time Payment Fraud Screening system processes card-not-present payment authorizations for a mid-size payment processor to evaluate fraud risk and manage reviews.]
[Screens authorizations in real-time, manages analyst cases, and ensures compliance with PCI-DSS Level 1 and 7-year auditability.]

## Key Elements
[Manual Analyst, Merchant Risk Manager, Compliance / Auditor Officer]
[Payment Gateway / Acquirer Systems, Third-Party Fraud Intelligence Feeds, Case Management SaaS]
[Identity Provider (AWS Cognito / Okta), Decision Audit Store (AWS S3 Object Lock & AWS KMS)]
[API Gateway & Routing Layer (AWS API Gateway / ALB)]
[Real-Time Scoring Engine (AWS ECS Fargate, Go/Java, ONNX Runtime)]
[Analyst & Rules Portal (AWS Amplify / S3 + CloudFront)]
[Case Management Backend (ECS Fargate)]
[Audit & Event Stream (Amazon SQS / EventBridge + Kinesis Data Firehose)]

## Relationships
[Payment Gateway to API Gateway & Routing Layer via HTTPS/JSON]
[API Gateway to Real-Time Scoring Engine via mTLS / HTTPS]
[Analyst & Rules Portal to Case Management Backend via REST/GraphQL]
[Scoring Engine and Case Management to Audit & Event Stream via Amazon SQS / EventBridge]
[Audit & Event Stream to Decision Audit Store (Amazon S3 Object Lock) via Kinesis Data Firehose]
[Scoring Engine to Third-Party Fraud Intelligence Feeds via AWS PrivateLink]

## Technology Stack
[AWS ECS Fargate for container orchestration to minimize operational overhead for a 3-person engineering team]
[Go or Java with ONNX Runtime for the Real-Time Scoring Engine to meet the P99 <50ms latency SLA at 3,000 TPS]
[Amazon S3 Object Lock (Compliance Mode) with AWS KMS for tamper-evident 7-year audit logging]
[Amazon SQS / EventBridge and Kinesis Data Firehose for serverless, low-maintenance event streaming]
[AWS Secrets Manager for dynamic secret injection and automatic rotation]
[AWS Amplify / S3 + CloudFront for the Analyst & Rules Portal SPA]

## Rationale
[This serverless-first AWS architecture meets the strict 25,000 EUR monthly budget and PCI-DSS Level 1 compliance while operating with only three engineers.]
[Decoupled, containerized microservices and immutable S3 rule bundles guarantee sub-50ms P99 latency and zero-downtime rule updates with robust fail-open safeguards.]