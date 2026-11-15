## Overview
An AWS-based multi-region e-commerce platform for physical and electronic books, supporting 1 million monthly active users with sub-2-second page loads. The system provides secure catalogue browsing, shopping carts, checkout, reviews, and personalized recommendations.

## Key Elements
- Book Shopper [person]
- Reviewer [person]
- Store Administrator [person]
- Web Frontend [container, React SPA]
- Admin Portal [container, React SPA]
- Amazon API Gateway [container, Amazon API Gateway]
- Catalogue Service [container, Node.js / Express]
- Order and Checkout Service [container, Go]
- Review Service [container, Python / FastAPI]
- Admin Service [container, Node.js / Express]
- Recommendation Integration Service [container, Node.js]
- Amazon Aurora PostgreSQL [container, Amazon Aurora PostgreSQL]
- Amazon DynamoDB [container, Amazon DynamoDB]
- Amazon OpenSearch [container, Amazon OpenSearch]
- WAF & Threat Protection [component, AWS WAF]
- JWT Authorizer [component, AWS Lambda / Native IAM]
- Request Validator [component, API Gateway Request Validator]
- Throttling & Rate Limiter [component, API Gateway Usage Plans]
- Response Caching [component, API Gateway Cache]
- API Router [component, Amazon API Gateway Routes/Stages]
- Access Logging & Tracing [component, Amazon CloudWatch / AWS X-Ray]
- Payment Gateway [externalSystem]
- Third-Party Shipping APIs [externalSystem]
- Identity Provider [externalSystem, Auth0/Cognito]
- Email Service [externalSystem, Amazon SES]
- ML Recommendation Engine [externalSystem, Amazon Personalize]

## Relationships
- Web Frontend -> WAF & Threat Protection: Inspects incoming traffic [HTTPS/REST]
- WAF & Threat Protection -> JWT Authorizer: Forwards sanitized requests [Internal]
- JWT Authorizer -> Request Validator: Passes validated security context [Internal]
- Request Validator -> Throttling & Rate Limiter: Evaluates rate limits [Internal]
- Throttling & Rate Limiter -> API Router: Forwards approved requests [Internal]
- API Router -> Response Caching: Checks cache for read operations [Internal]
- API Router -> Catalogue Service: Routes catalogue requests [HTTPS/REST with mTLS]
- API Router -> Order and Checkout Service: Routes checkout requests [HTTPS/REST with mTLS]
- API Router -> Access Logging & Tracing: Emits metrics [Internal]
- Order and Checkout Service -> Payment Gateway: Processes transactions [HTTPS/REST]
- Order and Checkout Service -> Third-Party Shipping APIs: Manages fulfillment [HTTPS/REST and Webhooks]
- Catalogue Service -> Amazon Aurora PostgreSQL: Queries relational data [TCP]
- Catalogue Service -> Amazon OpenSearch: Executes keyword search [TCP]

## Technology Stack
- AWS (Cloud Provider in us-east-1, eu-west-1, ap-southeast-1): Multi-region scalability and 99.95% uptime.
- React SPA: Frontend user and admin interfaces.
- Node.js, Go, Python/FastAPI: Microservices backend stack tailored by domain needs.
- Amazon Aurora PostgreSQL & DynamoDB: Relational storage and low-latency session/cart state.
- Amazon OpenSearch: Sub-second keyword search.
- AWS WAF & API Gateway: Edge security, throttling, caching, and request validation.

## Rationale
This architecture uses serverless edge routing and managed microservices to handle 1M MAU securely while meeting stringent GDPR/CCPA and sub-2-second performance requirements. Multi-region AWS deployment ensures high availability and low latency across global markets.