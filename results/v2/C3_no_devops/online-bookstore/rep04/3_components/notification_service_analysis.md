## Overview
The Notification Service is a microservice container within the Online Bookstore platform responsible for delivering secure, GDPR-compliant transactional and marketing communications to customers globally. It processes asynchronous event queues to send localized emails and SMS while providing audit visibility for administrators.

## Key Elements
- **Registered Customer**: End-user receiving localized transactional alerts and preference-managed marketing communications via email and SMS.
- **Store Administrator**: System user accessing delivery success rates, bounce logs, and troubleshooting metrics.
- **Event Consumer Component**: Node.js/Express service using AWS SDK to poll AWS SQS queues and verify HMAC message signatures.
- **Template Renderer Component**: Node.js/Express service using Handlebars/MJML and AWS Secrets Manager for localized, multi-currency message generation.
- **Preference Validation Middleware**: Node.js/Express security middleware evaluating GDPR/CCPA marketing opt-outs and consent flags.
- **Dispatch Engine Component**: Node.js/Express routing engine utilizing token-bucket rate limiting to send messages via AWS SES and Amazon SNS.
- **Audit & Metrics Component**: Node.js/Express logging service recording non-PII delivery statuses to Amazon CloudWatch.

## Relationships
- Checkout & Order -> Event Consumer Component: Triggers order and notification events [AWS SQS via HTTPS/TLS 1.3]
- Event Consumer Component -> Template Renderer Component: Passes parsed event payloads [In-memory asynchronous function calls]
- Template Renderer Component -> Preference Validation Middleware: Forwards rendered messages with consent context [In-memory asynchronous function calls]
- Preference Validation Middleware -> Dispatch Engine Component: Authorizes compliant messages [In-memory asynchronous function calls]
- Dispatch Engine Component -> Registered Customer: Delivers emails and SMS [SMTP/HTTPS via AWS SES and Amazon SNS]
- Audit & Metrics Component -> Store Administrator: Exposes secured delivery and bounce logs [OAuth2/OIDC secured HTTPS interface via Identity Provider]

## Technology Stack
- **Node.js / Express**: Core runtime and framework for all Notification Service internal components due to asynchronous I/O performance.
- **AWS SQS**: Asynchronous message queue for decoupling checkout from notification dispatch.
- **AWS SES & Amazon SNS**: Cloud messaging channels for transactional email and SMS delivery.
- **Handlebars / MJML**: Template engines for responsive, localized email formatting.
- **AWS Secrets Manager & AWS KMS**: Security services managing configuration keys and at-rest data encryption.
- **Amazon CloudWatch**: Metrics and logging platform with strict PII masking policies.

## Rationale
This component-based architecture isolates compliance logic and rendering responsibilities to guarantee GDPR/CCPA adherence without blocking core checkout performance. Asynchronous queuing and token-bucket rate limiting ensure 99.95% availability and high scalability under peak e-commerce traffic.