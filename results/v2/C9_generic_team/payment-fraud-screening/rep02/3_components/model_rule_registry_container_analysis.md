## Overview
[The system is a Real-Time Payment Fraud Screening platform that screens card-not-present payment authorizations for fraud and manages analyst review cases.]

## Key Elements
* Model & Rule Registry Container
* High-Performance Scoring Engine
* AWS S3
* AWS Parameter Store
* AWS ECS on Fargate
* Amazon CloudWatch

## Relationships
* High-Performance Scoring Engine polls AWS Parameter Store and AWS S3 for rule artifacts.
* Model & Rule Registry Container publishes versioned artifacts to AWS S3.
* Model & Rule Registry Container updates configuration pointers in AWS Parameter Store.

## Technology Stack
* AWS S3 for storing immutable versioned model and rule artifacts with lifecycle policies.
* AWS Parameter Store for managing configuration pointers and canary rollout metadata.
* OpenAPI/Swagger for defining the Model & Rule Registry Container API contract.
* Amazon CloudWatch for centralized structured logging and metric emission.

## Rationale
[The architecture uses immutable artifacts and local caching to guarantee sub-50ms scoring latency while maintaining 7-year auditability. It leverages serverless AWS primitives to stay within the 25,000 EUR monthly budget and minimize operational overhead for a three-engineer team.]