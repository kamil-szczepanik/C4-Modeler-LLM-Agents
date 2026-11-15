## Overview
The Message Broker container manages asynchronous event-driven workflows for the Online Bookstore across AWS regions. It ensures reliable service decoupling, fault tolerance, and compliance auditing for 1 million monthly active users.

## Key Elements
* **Event Router**: Amazon EventBridge for content-based domain event routing.
* **Notification Dispatcher**: Amazon SNS for broadcasting fan-out messages.
* **Task Queue Manager**: Amazon SQS for durable queue management and decoupling.
* **DLQ Monitor**: Amazon CloudWatch and AWS Lambda for alerting on unprocessable messages.

## Relationships
* Order & Checkout Service -> Event Router: Publishes domain events [HTTPS / AWS SDK]
* Event Router -> Task Queue Manager: Dispatches asynchronous tasks [AWS internal routing]
* Task Queue Manager -> Recommendation Service: Delivers payloads [HTTP / SQS Long Polling]
* Task Queue Manager -> DLQ Monitor: Forwards unprocessable messages [Amazon SQS Redrive Policy]
* DLQ Monitor -> Store Administrator: Sends operational alerts [Amazon SNS / Email]

## Technology Stack
* **Amazon EventBridge**: Selected for serverless content-based event routing.
* **Amazon SNS**: Chosen for reliable fan-out messaging to external services.
* **Amazon SQS**: Used for durable queuing and asynchronous decoupling.
* **Amazon CloudWatch & AWS Lambda**: Implemented for monitoring Dead-Letter Queues and triggering alerts.

## Rationale
This architecture ensures 99.95% availability by asynchronously decoupling services to handle traffic spikes. It also provides fault tolerance and compliance auditing through automated dead-letter queue monitoring.