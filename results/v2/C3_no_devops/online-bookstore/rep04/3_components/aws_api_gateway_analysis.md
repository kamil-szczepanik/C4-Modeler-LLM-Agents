## Overview
The AWS API Gateway component serves as the secure entry point and traffic router for the Online Bookstore's microservices architecture. It enforces global security, rate limiting, and protocol translation for all client and third-party interactions.

## Key Elements
- **WAF & Security Filter**: AWS WAF integrated with API Gateway for OWASP Top-10 mitigations.
- **Authorizer Component**: AWS Lambda Authorizer for JWT validation and scope extraction.
- **Throttling & Usage Plan Engine**: Native API Gateway Usage Plans and API Keys for rate limiting.
- **Request Router**: AWS API Gateway REST/HTTP APIs using proxy integration.
- **Transform & Response Mapper**: Velocity Template Language (VTL) engine for payload formatting and PII masking.
- **Observability Publisher**: Amazon CloudWatch and AWS X-Ray for telemetry.

## Relationships
- React SPA -> WAF & Security Filter: Inspects incoming requests [HTTPS/JSON, TLS 1.3]
- WAF & Security Filter -> Authorizer Component: Validates security tokens [Internal]
- Authorizer Component -> Throttling & Usage Plan Engine: Checks API quotas [Internal]
- Throttling & Usage Plan Engine -> Request Router: Forwards authorized traffic [Internal]
- Request Router -> Transform & Response Mapper: Formats error and success payloads [JSON]
- Request Router -> Observability Publisher: Emits metrics, logs, and traces [CloudWatch/X-Ray]
- Request Router -> Backend Microservices (Catalog, Checkout): Forwards signed requests via AWS App Mesh [gRPC/HTTP with SigV4/mTLS]

## Technology Stack
- **AWS API Gateway**: Core managed service for API routing, rate limiting, and protocol handling due to high scalability.
- **AWS WAF**: Web Application Firewall for security filtering and OWASP protection.
- **AWS Lambda**: Executes custom authorizer logic for flexible identity validation.
- **AWS App Mesh & SigV4**: Secures service-to-service communication within the VPC.
- **Amazon CloudWatch & AWS X-Ray**: Provides distributed tracing and observability.

## Rationale
This architecture ensures 99.95% uptime and high scalability (1M MAU) by offloading cross-cutting concerns like throttling, security, and telemetry to managed AWS services. It satisfies GDPR/CCPA and OWASP requirements via strict edge validation, PII masking, and encrypted zero-trust internal routing.