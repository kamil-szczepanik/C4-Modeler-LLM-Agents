## Overview
The Online Bookstore system is a scalable e-commerce platform designed for purchasing physical and electronic books with recommendations and reviews. It provides a secure, high-availability architecture utilizing AWS cloud services to support global users.

## Key Elements
* Single Page Application (SPA) (React, TypeScript, Amazon S3, Amazon CloudFront)
* API Gateway Container (AWS API Gateway)
* Rate Limiter Component (API Gateway throttling / Amazon Redis)
* Auth Integration Component (AWS Lambda Authorizer / JWT)
* Request Validator Component (JSON Schema validation)
* Route Dispatcher Component (AWS API Gateway routing)
* Response Transformer Component (Lambda edge transformation)
* Microservices: Catalog Service, Order & Checkout Service, Recommendation Service, Review & Notification Service
* External Systems: Auth0/AWS Cognito, Stripe/PayPal, FedEx/UPS, SendGrid/AWS SES, Avalara/TaxJar

## Relationships
* SPA -> Rate Limiter: Sends API requests [HTTPS / REST]
* Rate Limiter -> Auth Integration: Forwards requests for token validation [Internal Invocation]
* Auth Integration -> Auth0/AWS Cognito: Verifies tokens [OIDC / HTTPS]
* Auth Integration -> Request Validator: Forwards requests with context [In-memory]
* Request Validator -> Route Dispatcher: Forwards sanitized payloads [In-memory]
* Route Dispatcher -> Internal Microservices: Routes requests via internal Application Load Balancers [HTTPS / REST]
* Internal Microservices -> Response Transformer: Returns service responses [HTTPS / REST]
* Response Transformer -> SPA: Returns standardized responses [HTTPS]

## Technology Stack
* AWS API Gateway: Managed entry point ensuring 99.95% availability (R-07) and horizontal scalability (R-05).
* AWS Lambda / Lambda Authorizer: Executes edge validation, transformation, and stateless authentication.
* Amazon Redis: Supports rate limiting functionality and DDoS mitigation.
* JSON Schema: Enforces payload validation to satisfy OWASP Top-10 security requirements (R-08).

## Rationale
This architecture leverages managed AWS services to effortlessly scale to 1M MAU while maintaining strict security, performance, and compliance standards. Decoupling edge concerns like rate limiting, authentication, and validation ensures internal microservices remain protected and performant.