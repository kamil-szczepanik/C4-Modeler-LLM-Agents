## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor. It provides fraud scoring, case management, and zero-downtime model deployments.]

## Key Elements
* Data Scientists / Fraud Modelers (Users)
* Engineering Team (Users)
* GitHub (Secure Git Repository)
* AWS CodePipeline & AWS CodeBuild
* Amazon ECS Fargate
* Amazon CloudWatch
* Amazon S3 Audit & Feature Store

## Relationships
* Data Scientists -> GitHub (HTTPS): Commits fraud rules and models.
* GitHub -> AWS CodePipeline (Webhook / HTTPS): Triggers deployment pipeline.
* AWS CodePipeline -> AWS CodeBuild (API): Validates and compiles models into ONNX format.
* AWS CodeBuild -> Amazon S3 (AWS SDK): Stores signed model artifacts and audit metadata.
* AWS CodePipeline -> Amazon ECS Fargate (AWS ECS API / HTTPS): Orchestrates zero-downtime task updates.
* Amazon CloudWatch -> AWS CodePipeline (CloudWatch Alarms / EventBridge): Monitors P99 latency and error rates for automated canary rollbacks.

## Technology Stack
* AWS CodePipeline & CodeBuild: Serverless CI/CD to eliminate Kubernetes control plane overhead for a 3-engineer team.
* Python / FastAPI: Validation and compilation runtime.
* ONNX: Portable model format for consistent execution.
* Terraform / CDK: Infrastructure-as-code for declarative state management.
* Amazon CloudWatch: Real-time telemetry for automated rollbacks.

## Rationale
[This serverless, AWS-native pipeline architecture minimizes operational overhead for a three-engineer team while meeting the 25,000 EUR monthly budget constraint. It ensures zero-downtime deployments (R-03) and tamper-evident audit trails (R-06) via automated artifact storage and monitoring.]