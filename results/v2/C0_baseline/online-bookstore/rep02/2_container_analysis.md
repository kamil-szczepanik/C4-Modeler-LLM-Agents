## Overview
An Amazon-style e-commerce online bookstore for physical and electronic books designed for global scale and compliance. It delivers high-performance catalogue browsing, secure checkout, and targeted recommendations while maintaining strict regulatory standards.

## Key Elements
- **Users**: Customers, Book Authors/Publishers, Store Administrators
- **Client**: Single Page Application (React / TypeScript)
- **Routing & Security**: Amazon API Gateway
- **Services**: Catalogue & Search Service (Go), Order & Checkout Service (Node.js/Java), Recommendation Service (Python), Review & Moderation Service (Node.js)
- **Data Stores**: Amazon OpenSearch, Amazon Aurora (PostgreSQL), Amazon DynamoDB
- **Infrastructure & Messaging**: Amazon ECS/EKS, Amazon SQS/SNS, AWS App Mesh
- **External Systems**: Identity Provider, Payment Gateway, Shipping Provider, Recommendation Engine, Notification Service

## Relationships
- **SPA to API Gateway**: Routes all client traffic via HTTPS (TLS 1.3)
- **API Gateway to Microservices**: Routes requests via REST/GraphQL and enforces mTLS via AWS App Mesh
- **Microservices to Data Stores**: Reads/writes via dedicated database drivers (Aurora, DynamoDB, OpenSearch)
- **Services to Messaging**: Publishes and consumes asynchronous events via Amazon SQS/SNS
- **Checkout to External**: Integrates securely with external Payment and Shipping APIs

## Technology Stack
- **Frontend**: React / TypeScript hosted on Amazon CloudFront / S3 for fast client-side rendering
- **Backend Services**: Go, Python (FastAPI), Node.js / Java (Spring Boot) containerized on AWS ECS/EKS
- **Databases**: Amazon Aurora (PostgreSQL) for transactional data, Amazon DynamoDB for recommendations, Amazon OpenSearch for catalogue search
- **Messaging & Integration**: Amazon SQS/SNS for asynchronous event-driven decoupling
- **Security & Ops**: AWS Secrets Manager, AWS KMS, AWS App Mesh (mTLS), and AWS X-Ray / CloudWatch

## Rationale
This container architecture separates high-throughput discovery and checkout from compliance-heavy review workflows to satisfy the <2s page load and 1M MAU scalability goals. Utilizing managed AWS services and asynchronous messaging via SQS/SNS ensures 99.95% uptime while isolating PII to meet GDPR and CCPA requirements.