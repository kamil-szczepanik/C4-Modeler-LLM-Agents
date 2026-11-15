## Overview
The Online Bookstore asynchronous messaging architecture utilizes AWS SQS and SNS to decouple microservices and ensure scalable, resilient order processing. It supports 1 million monthly active users while complying with GDPR and CCPA regulations.

## Key Elements
- **SNS Topics:** `OrderEventsTopic` and `CatalogEventsTopic` using fan-out patterns
- **SQS Queues:** `OrderProcessing-HighPriorityQueue`, `OrderProcessing-StandardQueue`, `NotificationQueue`, and `RecommendationQueue`
- **Dead-Letter Queues (DLQs):** Dedicated failure queues paired with CloudWatch alarms
- **Consumers:** Java/Spring Boot (`Order & Checkout`), Node.js/Express (`Notification`), and Python/FastAPI (`Recommendation`)
- **Infrastructure & Security:** AWS KMS, AWS IAM, Terraform, and AWS X-Ray

## Relationships
- **Order & Checkout Service -> OrderEventsTopic:** Publishes encrypted JSON events over HTTPS using AWS SDK
- **OrderEventsTopic -> SQS Queues:** Dispatches filtered messages using SNS filter policies and subscription protocols
- **SQS Queues -> Consumers:** Pulls messages using AWS SDK with exponential backoff and jitter
- **Consumers -> AWS Aurora/DynamoDB:** Fetches raw PII data securely via authenticated API calls using tokenized IDs

## Technology Stack
- **Amazon SQS & SNS:** Pull-based queuing and push-based pub/sub for asynchronous microservice decoupling
- **AWS KMS:** Customer-managed keys for server-side encryption (SSE-SQS/SSE-SNS) to protect data at rest
- **Terraform:** Infrastructure as Code for multi-region deployments across `us-east-1`, `eu-west-1`, and `ap-southeast-1`
- **CloudEvents & AWS X-Ray:** Standardized JSON message payloads and distributed tracing for observability

## Rationale
This messaging architecture guarantees 99.95% uptime and handles high traffic without degradation by isolating critical checkout flows from background tasks using priority queues. PII minimization and KMS encryption ensure compliance with GDPR and CCPA security mandates.