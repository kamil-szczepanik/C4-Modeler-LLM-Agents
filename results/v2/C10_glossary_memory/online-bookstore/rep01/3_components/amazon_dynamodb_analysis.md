## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. It utilizes AWS infrastructure across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to deliver scalable, low-latency, and compliant retail operations.

## Key Elements
- **Book Shopper**: End-user browsing the catalogue, purchasing books, and leaving reviews.
- **Reviewer**: User reading and submitting book reviews.
- **Store Administrator**: Administrator managing system configurations and catalogue items.
- **Web Frontend & Admin Portal**: React SPAs served via AWS CloudFront.
- **Amazon API Gateway**: Entry point routing traffic and validating JWT tokens.
- **Backend Services**: Catalogue Service (Node.js/Express), Order and Checkout Service (Go), Review Service (Python/FastAPI), Admin Service (Node.js/Express), and Recommendation Integration Service (Node.js).
- **Data & Storage**: Amazon Aurora PostgreSQL, Amazon DynamoDB (Cart Table and Session Table), and Amazon OpenSearch.
- **External Systems**: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Amazon SES, and Amazon Personalize (ML Recommendation Engine).

## Relationships
- **Shoppers/Admins -> Web Frontend/Admin Portal**: HTTPS via AWS CloudFront
- **Frontends -> Amazon API Gateway**: HTTPS/REST with JWT validation
- **API Gateway -> Microservices**: HTTPS/REST with JWT validation
- **Order and Checkout Service -> Cart Table & Session Table**: HTTPS/DynamoDB API over TLS 1.3 with VPC Endpoints
- **Catalogue/Order/Review/Admin Services -> Amazon Aurora PostgreSQL**: TCP
- **Catalogue Service -> Amazon OpenSearch**: TCP
- **Order and Checkout Service -> Payment Gateway & Shipping APIs**: HTTPS/REST and Webhooks
- **Recommendation Integration Service -> ML Recommendation Engine**: HTTPS/REST and SQS/SNS

## Technology Stack
- **Compute & Cloud**: AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region availability.
- **Frontend**: React SPA deployed via AWS CloudFront.
- **API Routing**: Amazon API Gateway for traffic management and JWT validation.
- **Backend Languages**: Node.js/Express, Go (Order and Checkout), Python/FastAPI (Reviews).
- **Databases**: Amazon Aurora PostgreSQL (relational data), Amazon DynamoDB Global Tables (carts and sessions with TTL and KMS encryption), and Amazon OpenSearch (keyword search).
- **Integrations**: Amazon SES (email), Amazon Personalize (recommendations), Auth0/AWS Cognito (OAuth2/OIDC).

## Rationale
This architecture ensures 99.95% uptime and high scalability for 1M MAU through multi-region AWS deployments and DynamoDB Global Tables. Security and compliance (GDPR/CCPA, OWASP Top-10) are enforced via TLS 1.3, AWS KMS encryption, IAM Least Privilege (`dynamodb:LeadingKeys`), and VPC Endpoints.