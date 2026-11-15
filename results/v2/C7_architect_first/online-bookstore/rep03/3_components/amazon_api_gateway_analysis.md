## Overview
- Scalable e-commerce online bookstore serving 1 million Monthly Active Users globally across three AWS regions with 99.95% uptime.
- Provides secure catalog browsing, multi-currency purchasing, customer reviews, and personalized book recommendations.

## Key Elements
- **Client Tier**: Single Page Application (React) hosted on Amazon CloudFront and Amazon S3.
- **Edge Security & Routing Tier**: Amazon API Gateway with AWS WAF, featuring Request Validator, Router/Authorizer (JWT), Throttling/Rate Limiting, Transform & Edge Routing, and Edge Caching components.
- **Backend Compute Tier**: Core E-Commerce API and Recommendation & Review Service running on Amazon ECS (Fargate) via AWS App Mesh and ECS Service Connect.
- **Data & Integration Tier**: Amazon Aurora PostgreSQL Global Database, Amazon ElastiCache Redis, Identity Provider, Payment Gateway, Shipping Provider API, and Notification Service.

## Relationships
- Single Page Application -> Amazon API Gateway: Sends client requests [HTTPS/JSON] with TLS 1.3.
- Amazon API Gateway -> Identity Provider: Validates user tokens [OIDC/OAuth 2.0].
- Amazon API Gateway -> Core E-Commerce API: Routes validated, sanitized requests with currency context [HTTPS via AWS App Mesh/ECS Service Connect using mTLS or AWS IAM SigV4].
- Core E-Commerce API -> Amazon Aurora PostgreSQL Global Database: Reads and persists transactional data [PostgreSQL Wire Protocol over TLS].

## Technology Stack
- **Cloud Infrastructure**: AWS across regions `us-east-1`, `eu-west-1`, and `ap-southeast-1` managed via Terraform/AWS CDK for multi-region resilience.
- **API Management & Security**: Amazon API Gateway, AWS WAF, AWS IAM, and JSON Web Tokens (JWT) for secure, throttled edge routing.
- **Frontend**: React served via Amazon CloudFront and Amazon S3.
- **Backend Compute**: Node.js with Express and Python with FastAPI hosted on Amazon ECS (Fargate).
- **Data Stores**: Amazon Aurora PostgreSQL Global Database and Amazon ElastiCache Redis.

## Rationale
- Leverages globally distributed AWS services like Amazon CloudFront, API Gateway Edge Caching, and Aurora Global Databases to guarantee sub-2-second page loads on 3G and 99.95% availability for 1M MAU.
- Integrates AWS WAF, strict IAM/mTLS policies, and API Gateway input validation to meet stringent GDPR/CCPA privacy standards and OWASP Top-10 security requirements.