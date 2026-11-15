## Overview
The Case Management UI & Backend container supports fraud analysts, risk managers, and compliance officers in reviewing suspicious payment transactions. It enforces strict security controls and auditability while optimizing operational productivity within budget constraints.

## Key Elements
* Fraud Analysts, Risk Managers / Data Scientists, and Compliance & Audit Officers
* Amazon API Gateway and Application Load Balancer (ALB)
* Case Management UI & Backend (AWS ECS Fargate)
* Amazon S3 and Amazon QLDB for audit logs and compliance archives
* AWS Secrets Manager, IAM, AWS CloudWatch, and AWS X-Ray

## Relationships
* Users -> Case Management UI & Backend: Accesses interface via HTTPS (OIDC/MFA authenticated)
* Case Management UI & Backend -> Amazon QLDB: Streams immutable audit trails and analyst actions
* Case Management UI & Backend -> AWS Secrets Manager: Injects database secrets and OIDC keys at runtime

## Technology Stack
* AWS ECS Fargate: Provides a serverless container runtime aligned with the 3-person team capacity and €25k/month budget.
* TLS 1.3 and mTLS: Secures transit between the ALB, ECS tasks, and downstream datastores.
* Amazon QLDB: Stores cryptographically signed audit logs to satisfy the 7-year tamper-evident requirement.
* AWS Secrets Manager and IAM: Enforces least-privilege access and dynamic credential injection.

## Rationale
This architecture uses serverless containers and managed AWS services to minimize operational overhead for a three-person engineering team. It rigorously enforces PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while maintaining strict cost controls.