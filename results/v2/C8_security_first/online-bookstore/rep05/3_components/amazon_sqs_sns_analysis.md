## Overview
[An Amazon-style online bookstore system providing catalog browsing, secure checkout, 5-star reviews, and personalized recommendations for physical and electronic books.]

## Key Elements
- Customers & Store Administrators (People)
- Single Page Application (React / TypeScript, Amazon S3 + CloudFront CDN)
- API Gateway & Load Balancer (AWS API Gateway, ALB, Route 53)
- Microservices: Catalog & Search Service, Checkout & Payment Service, Recommendation Service (Go, Node.js, Python / FastAPI, AWS ECS Fargate)
- Databases & Caching: Amazon Aurora PostgreSQL, Redis
- Messaging: Amazon SNS, Amazon SQS FIFO, Dead-Letter FIFO Queue
- External Systems: Stripe / PayPal, FedEx / UPS, AWS Cognito / Auth0, AWS SES / SendGrid

## Relationships
- Customers -> Single Page Application [HTTPS]
- Single Page Application -> API Gateway & Load Balancer [HTTPS / REST / GraphQL]
- API Gateway -> Catalog & Search Service, Checkout & Payment Service, Recommendation Service [gRPC / REST]
- Checkout & Payment Service -> Order SNS Topic [AWS SDK / HTTPS / SigV4]
- Order SNS Topic -> Shipping FIFO Queue [AWS SNS-SQS Pub/Sub]
- Shipping FIFO Queue -> Dead-Letter FIFO Queue [AWS SQS Redrive Policy]
- Checkout & Payment Service -> Stripe / PayPal [HTTPS / REST]
- Shipping Workers -> FedEx / UPS [HTTPS / REST]

## Technology Stack
- Cloud Provider: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global availability
- Compute: AWS ECS Fargate for scalable containerized microservices execution
- Messaging: Amazon SNS and Amazon SQS FIFO for decoupled asynchronous event processing
- Database: Amazon Aurora PostgreSQL Global Database for relational data and multi-region replication
- Security & Transport: AWS PrivateLink (VPC Endpoints), AWS KMS (Customer-Managed Keys), TLS 1.2+, AWS IAM least privilege

## Rationale
[This architecture decouples core checkout from third-party shipping APIs using SQS FIFO queues to guarantee 99.95% uptime and prevent race conditions during high-volume traffic. AWS PrivateLink and KMS encryption ensure strict GDPR/CCPA compliance and OWASP-grade transport security.]