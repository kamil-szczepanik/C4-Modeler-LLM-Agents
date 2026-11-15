## Overview
[An Amazon-style global online bookstore providing physical and electronic book sales with integrated recommendations and reviews.]

## Key Elements
*   **Users:** Book Shopper, Book Author/Publisher, Store Administrator.
*   **External Systems:** Stripe/PayPal, FedEx/UPS APIs, AWS SES, AWS Cognito/Auth0, AWS CloudFront/Route 53, AWS CloudWatch/Datadog.
*   **Client Containers:** Single Page Application (React/TypeScript).
*   **API Layer:** AWS API Gateway (REST/GraphQL).
*   **Backend Services:** Catalog & Search Service, Order & Checkout Service, Personalization Service, Customer Review Service, Notification Service.
*   **Data Stores:** Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Redis.

## Relationships
*   **SPA to API Gateway:** HTTPS / REST / GraphQL.
*   **API Gateway to Services:** Internal HTTPS / gRPC.
*   **Services to Data Stores:** JDBC / AWS SDK.
*   **Order Service to External:** HTTPS to Stripe/PayPal.
*   **Notification Service to External:** AWS SDK to AWS SES and FedEx/UPS APIs.
*   **Inter-Service Messaging:** Amazon EventBridge and Amazon SQS.

## Technology Stack
*   **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) utilizing Terraform/AWS CDK for Infrastructure as Code.
*   **Frontend Hosting:** AWS S3 delivered via AWS CloudFront CDN for global sub-2s performance.
*   **Compute:** AWS ECS/EKS with ArgoCD GitOps for zero-downtime blue/green deployments.
*   **Backend Services:** Spring Boot (Java), Node.js/Express, Python (FastAPI/Celery).
*   **Databases & Caching:** Amazon Aurora PostgreSQL (active-passive cross-region read-replicas), Amazon DynamoDB, Amazon OpenSearch, Redis (ElastiCache).

## Rationale
[AWS multi-region active-passive replication combined with asynchronous decoupling via SQS and EventBridge ensures 99.95% availability, strict PII isolation, and global scalability for 1M MAU. Dedicated microservices isolate high-load operations like reviews and recommendations from critical checkout paths to meet strict performance and compliance requirements.]