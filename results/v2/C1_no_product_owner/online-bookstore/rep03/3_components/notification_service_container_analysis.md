## Overview
[The Notification Service Container is a Go-based microservice responsible for consuming asynchronous events and reliably dispatching multi-channel notifications (Email, SMS, Push) to customers. It operates within the Online Bookstore platform to support order receipts, shipping updates, and marketing communications.]

## Key Elements
- Event Consumer Component (Go, AWS SDK for Go)
- Notification Dispatcher Component (Go)
- Template Engine Component (Go, `text/template`)
- Third-Party Provider Adapter Component (Go, HTTP Client)
- DLQ Handler Component (Go)
- Secrets Manager Client Component (Go, AWS SDK for Go)
- Amazon SQS & Amazon EventBridge
- SendGrid & Twilio APIs
- Amazon ECS on AWS Fargate

## Relationships
- Event Consumer -> Notification Dispatcher: Forwards raw event payloads [In-memory function call]
- Event Consumer -> DLQ Handler: Forwards poison-pill messages [In-memory function call]
- Notification Dispatcher -> Template Engine: Requests rendered content [In-memory function call]
- Notification Dispatcher -> Third-Party Provider Adapter: Dispatches final messages [REST over HTTPS]
- Third-Party Provider Adapter -> Secrets Manager Client: Retrieves API credentials [In-memory cache lookup]
- Third-Party Provider Adapter -> SendGrid/Twilio APIs: Sends notifications [REST over HTTPS with mTLS]

## Technology Stack
- Go: Chosen for high concurrency, fast startup times, and low memory footprint.
- Amazon ECS on AWS Fargate: Provides serverless container orchestration across multi-regions.
- Amazon SQS & Amazon EventBridge: Ensures decoupled, reliable event-driven messaging with dead-letter queue support.
- AWS Secrets Manager: Securely manages and rotates third-party API keys.
- OpenTelemetry & AWS CloudWatch: Enables structured JSON logging and distributed tracing.

## Rationale
[This architecture ensures high availability (99.95%) and horizontal scalability to handle 1M MAU via event-driven messaging and ECS Fargate auto-scaling. It embeds robust security controls—including PII masking, least-privilege IAM, and TLS encryption—to meet GDPR, CCPA, and OWASP compliance requirements.]