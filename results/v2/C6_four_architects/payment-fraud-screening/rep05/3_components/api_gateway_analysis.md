## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and provides case management tools for fraud analysts. Its core purpose is to prevent fraudulent transactions while maintaining PCI-DSS Level 1 compliance and a P99 latency under 50 ms.]

## Key Elements
* Amazon API Gateway (Regional API endpoint)
* CloudFront / React SPA
* Case Management API (Amazon ECS Fargate)
* Identity Provider (IdP)
* AWS WAF
* AWS Lambda (Lambda Authorizer)
* Amazon CloudWatch
* AWS X-Ray

## Relationships
* CloudFront / React SPA -> Amazon API Gateway: Sends analyst review traffic [HTTPS/REST via TLS 1.2+]
* Amazon API Gateway -> Case Management API: Forwards validated requests [HTTPS/REST via HTTP/2]
* Amazon API Gateway -> Identity Provider (IdP): Validates JWT tokens via Lambda Authorizer [HTTPS]
* Amazon API Gateway -> Amazon CloudWatch: Streams structured JSON access logs [AWS API]

## Technology Stack
* Amazon API Gateway: Regional endpoint configuration to optimize latency within eu-west-1 and reduce multi-region costs.
* AWS WAF: Perimeter defense and abuse protection for PCI-DSS compliance.
* AWS Lambda: Local JWT validation and caching to offload authentication overhead from the backend.
* OpenAPI 3.0 via AWS CDK: Enforces strict API contracts and prevents schema drift.
* AWS X-Ray: End-to-end distributed tracing across analyst review workflows.

## Rationale
[The architecture utilizes managed AWS services like API Gateway, Fargate, and WAF to satisfy strict PCI-DSS Level 1 compliance and auditability requirements while minimizing operational overhead for a 3-engineer team. Regional deployment in eu-west-1 and native edge validations ensure P99 latency remains under 50 ms within budget limits.]