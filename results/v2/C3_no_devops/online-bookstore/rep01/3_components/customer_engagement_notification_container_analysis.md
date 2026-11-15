## Overview
The Customer Engagement & Notification Container is a Node.js-based microservice responsible for processing asynchronous events to dispatch transactional and promotional messages. It ensures GDPR and CCPA compliance while delivering multi-channel notifications for the Online Bookstore.

## Key Elements
- Event Consumer Component (Node.js, AWS SDK)
- Notification Dispatcher Component (Node.js)
- Template Engine Component (Handlebars, MJML)
- Consent & Preference Manager Component (Node.js, DynamoDB Client)
- Third-Party Provider Adapter Component (Axios, HTTPS)
- Audit Logger Component (Node.js)
- Amazon SQS / SNS
- Amazon DynamoDB
- AWS Secrets Manager
- External Email/Notification Service (SES, Twilio)

## Relationships
- AWS SQS/SNS -> Event Consumer: Triggers asynchronous notification workflows [AWS SQS/SNS, TLS]
- Event Consumer -> Consent & Preference Manager: Validates user preferences [In-process / Async]
- Consent & Preference Manager -> Amazon DynamoDB: Reads/writes user consent profiles [AWS SDK, TLS 1.3]
- Notification Dispatcher -> Template Engine: Renders message content [In-process]
- Notification Dispatcher -> Third-Party Provider Adapter: Dispatches payload [In-process]
- Third-Party Provider Adapter -> Email/Notification Service: Sends final message [HTTPS, TLS 1.3]
- Third-Party Provider Adapter -> Audit Logger: Emits dispatch results [In-process / Async]
- Audit Logger -> Amazon DynamoDB: Persists audit logs [AWS SDK, TLS 1.3]
- Third-Party Provider Adapter -> AWS Secrets Manager: Retrieves API keys [AWS SDK, TLS 1.3]

## Technology Stack
- Node.js & TypeScript: Provides high-throughput, asynchronous worker execution
- Handlebars & MJML: Renders responsive, secure HTML/text multi-channel templates
- Amazon DynamoDB: Stores encrypted user consent profiles and non-PII audit logs
- AWS Secrets Manager: Secures third-party API keys at runtime
- Axios: Handles resilient outbound communication with exponential backoff retries

## Rationale
This architecture uses an event-driven worker model to decouple notification dispatching from core checkout workflows, ensuring high scalability under peak load. Integrated security controls, strict egress filtering, and a dedicated consent manager guarantee GDPR and CCPA compliance without impacting transaction performance.