## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform providing catalog browsing, secure checkout, reviews, and personalized recommendations. The system ensures global compliance (GDPR/CCPA), multi-currency support, and high availability (99.95% uptime) across three AWS regions.

## Key Elements
- **Users**: Customer, Book Author/Publisher, Store Administrator
- **External Systems**: Payment Gateway, Shipping Provider APIs, Identity Provider, Notification System, Tax Calculation Service
- **Containers**: Single Page Application (React, TS, S3, CloudFront), API Gateway & Load Balancer (AWS API Gateway, ALB), Catalog & Search Service (Node.js, ECS Fargate), Checkout & Order Service (Go/Java, ECS Fargate), Recommendation Service (Python, FastAPI, ECS Fargate), Data Privacy Service, Localization Service
- **Recommendation Components**: Recommendation API Router, A/B Experimentation Evaluator, Algorithm Engine (NumPy/PyTorch), Circuit Breaker, Fallback Manager, Clickstream Publisher, Data Access Client
- **Data & Messaging**: Amazon Aurora (PostgreSQL), Amazon DynamoDB, Amazon OpenSearch, Amazon SQS/SNS, Amazon S3

## Relationships
- **SPA -> API Gateway & Load Balancer**: HTTPS REST/GraphQL traffic
- **API Gateway -> Recommendation Service**: gRPC / REST recommendation requests
- **Recommendation Service -> Amazon Aurora (PostgreSQL)**: Fetches user history and metadata via SQL/ORM
- **Recommendation Service -> Amazon DynamoDB**: Reads cached vectors and session data
- **Recommendation Service -> Amazon SQS/SNS**: Asynchronously publishes telemetry and clickstream events

## Technology Stack
- **Compute & Orchestration**: AWS ECS on Fargate in `us-east-1`, `eu-west-1`, and `ap-southeast-1` for scalable, multi-region container execution.
- **Backend Languages & Frameworks**: Python with FastAPI for high-performance ML inference routing.
- **ML & Data Processing**: NumPy, Scikit-learn, and PyTorch for collaborative filtering and recommendation generation.
- **Storage & Caching**: Amazon Aurora (PostgreSQL) for relational data, Amazon DynamoDB for session cache, and Amazon S3 for model artifacts.
- **Messaging & Observability**: Amazon SQS/SNS for asynchronous event publishing; AWS CloudWatch and Prometheus/OpenTelemetry for custom metrics and auto-scaling.

## Rationale
This architecture uses Python/FastAPI inside Amazon ECS on Fargate to deliver low-latency machine learning recommendations that meet the <2s page load requirement. Circuit breakers, fallback managers, and S3-cached model artifacts ensure system resilience, graceful degradation, and compliance with high availability SLAs.