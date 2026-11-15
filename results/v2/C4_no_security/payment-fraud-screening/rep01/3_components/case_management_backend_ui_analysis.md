## Overview
The Case Management system provides an interactive React UI and Python backend enabling fraud analysts to review suspicious payment cases and manage workflows. It ensures compliance-driven auditability while maintaining real-time queue synchronization.

## Key Elements
* **React Analyst Web App**: Single-page application hosted on Amazon S3 and distributed via Amazon CloudFront.
* **FastAPI Case Management Backend**: Unified container handling API routing, RBAC, data masking, and orchestration on AWS ECS Fargate.
* **Audit Event Emitter**: Internal module using AWS SDK (boto3) to stream immutable logs.
* **Audit Log Storage**: Amazon S3 featuring Object Lock for tamper-evident retention.

## Relationships
* **Fraud Analyst -> React Analyst Web App**: Reviews flagged transactions and manages queues via HTTPS and WebSockets.
* **React Analyst Web App -> FastAPI Case Management Backend**: Communicates request data and queue updates via REST/HTTPS and WebSockets.
* **FastAPI Case Management Backend -> Amazon S3**: Streams append-only audit events via AWS SDK over HTTPS.

## Technology Stack
* **Python (FastAPI)**: Consolidated backend runtime reducing maintenance overhead for a 3-person team.
* **React**: Frontend framework delivering sub-minute case reviews.
* **AWS ECS Fargate**: Serverless container orchestration fitting the 25k EUR monthly budget.
* **Amazon S3 with Object Lock**: Cost-effective, immutable storage satisfying the 7-year audit mandate.

## Rationale
This architecture minimizes operational complexity for a three-engineer team by consolidating runtime stacks. It meets strict PCI-DSS and 7-year audit requirements within budget through native AWS services.