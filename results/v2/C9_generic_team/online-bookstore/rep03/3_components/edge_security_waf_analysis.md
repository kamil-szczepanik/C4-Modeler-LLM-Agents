## Overview
The Online Bookstore is a scaled-down e-commerce platform providing book sales, recommendations, and reviews for 1 million monthly active users globally. The architecture prioritizes high availability, sub-2-second page loads, and strict compliance with GDPR, CCPA, and OWASP Top-10 security standards.

## Key Elements
- Storefront Frontend (SPA) (AWS S3, Amazon CloudFront)
- Edge Security & WAF (AWS WAF)
- API Gateway / BFF (AWS API Gateway)
- Core Domain Services (AWS ECS / EKS, gRPC, REST)
- Caching Layer (Amazon ElastiCache (Redis))
- Asynchronous Message Broker (AWS SQS/SNS with Dead Letter Queue)
- Persistence Layer (Amazon RDS, Amazon OpenSearch)
- Observability & Monitoring (Amazon CloudWatch, AWS X-Ray, SIEM)

## Relationships
- Storefront Frontend (SPA) -> Edge Security & WAF: Protects frontend requests [AWS WAF]
- Edge Security & WAF -> API Gateway / BFF: Forwards validated traffic [HTTPS]
- API Gateway / BFF -> Core Domain Services: Routes microservice requests [gRPC, REST]
- Core Domain Services -> Persistence Layer: Reads and writes data [TCP]
- Core Domain Services -> Caching Layer: Retrieves cached data and sessions [Redis Protocol]

## Technology Stack
- Cloud Infrastructure: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global distribution.
- Edge & Security: AWS WAF with AWS Managed Rules for OWASP Top 10 to mitigate attacks at the edge.
- Infrastructure as Code (IaC): AWS CDK or Terraform for modular, version-controlled resource management and drift detection.
- Monitoring & Telemetry: Amazon CloudWatch and AWS X-Ray for metrics, automated alarms on block rates, and log streaming.

## Rationale
The architecture uses a globally distributed AWS infrastructure with edge security to ensure 99.95% uptime and sub-2-second response times under high concurrency. Modular IaC and automated testing pipelines maintain strict regulatory compliance while securing checkout and search workflows against malicious traffic.