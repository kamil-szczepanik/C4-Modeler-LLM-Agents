## Overview
## Overview
- Scaled-down Amazon-style e-commerce site for books featuring recommendations, reviews, and multi-currency support.
- Built to handle 1M MAU globally with strict GDPR/CCPA compliance and 99.95% uptime.

## Key Elements
- **Users**: Customer (Shopper), Store Administrator / Compliance Officer.
- **External Systems**: Notification System, Payment Gateway, Shipping Provider APIs, Identity Provider, Tax Calculation Service.
- **Containers**: Single Page Application (React/TypeScript, CloudFront, S3), API Gateway & Load Balancer (AWS API Gateway, ALB), Data Privacy Service (Amazon ECS on Fargate), Catalog & Search Service, Checkout & Order Service, Recommendation Service, Localization Service.
- **Data Privacy Components**: DSAR Orchestrator (Node.js/TypeScript), Consent Manager (Go), Data Anonymization Engine (Python/Pandas).
- **Data & Messaging**: Amazon Aurora (PostgreSQL) with Global Databases, Amazon DynamoDB, Amazon OpenSearch, Amazon SQS/SNS, S3 Staging Buckets.

## Relationships
- Single Page Application -> API Gateway & Load Balancer [HTTPS/REST]
- API Gateway -> Data Privacy Service (DSAR Orchestrator & Consent Manager) [REST/JSON, gRPC]
- DSAR Orchestrator -> Messaging Bus (Amazon SQS) [AMQP]
- DSAR Orchestrator -> Notification System (External) [Amazon SNS/HTTPS]
- Data Privacy Service -> Database Cluster (Amazon Aurora) [TCP/PostgreSQL driver]
- DSAR Orchestrator & Consent Manager -> S3 Temporary Staging Buckets [HTTPS]

## Technology Stack
- **Compute**: Amazon ECS on Fargate for containerized microservices isolation.
- **Languages**: Node.js/TypeScript (DSAR Orchestrator), Go (Consent Manager), Python (Anonymization Engine).
- **Database & Storage**: Amazon Aurora PostgreSQL with Global Databases for multi-region replication and GDPR/CCPA compliance; Amazon S3 for encrypted temporary DSAR export staging.
- **Messaging & Observability**: Amazon SQS/SNS for asynchronous workflows and AWS X-Ray for distributed tracing.

## Rationale
- Microservices on AWS Fargate combined with Amazon Aurora Global Databases ensure multi-region scalability for 1M MAU while meeting strict 99.95% uptime SLAs.
- Dedicated asynchronous components and encrypted S3 staging protect sensitive PII and guarantee automated GDPR/CCPA compliance.