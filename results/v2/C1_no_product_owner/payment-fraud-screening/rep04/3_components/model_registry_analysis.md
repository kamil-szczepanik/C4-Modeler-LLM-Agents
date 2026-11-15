## Overview
The Model Registry system securely manages, validates, and serves machine learning models for real-time payment fraud screening. It ensures zero-downtime model updates and 7-year tamper-evident auditability while operating within strict cloud cost constraints.

## Key Elements
* Model Storage Manager (Python, boto3, S3 Object Lock)
* Registry REST API (FastAPI, AWS ECS Fargate)
* MLflow Client Library (Python, serverless logging)
* Amazon S3 (KMS-encrypted model artifact repository)
* Scoring Engine (Consumer of model artifacts)

## Relationships
* Scoring Engine -> Registry REST API: Fetches active model metadata and pointers [gRPC over TLS 1.3]
* Registry REST API -> Amazon S3: Reads model artifacts and version pointers [boto3 / HTTPS]
* Model Storage Manager -> Amazon S3: Applies Object Lock Compliance Mode and versioning [boto3 / HTTPS]

## Technology Stack
* Python / FastAPI: Lightweight, high-performance framework for the REST API
* AWS ECS Fargate: Serverless container execution minimizing operational toil for a 3-engineer team
* Amazon S3 with Object Lock: Immutable storage satisfying the 7-year audit retention mandate
* AWS KMS: Customer Managed Keys for encrypting model artifacts and securing data at rest

## Rationale
This serverless, S3-centric architecture eliminates stateful infrastructure overhead, enabling a three-person team to maintain it within budget. S3 Object Lock and strict encryption natively satisfy PCI-DSS and 7-year audit requirements without compromising sub-millisecond model retrieval latencies.