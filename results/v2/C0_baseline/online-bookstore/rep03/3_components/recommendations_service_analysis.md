## Overview
The Online Bookstore system is a multi-region e-commerce platform providing scalable book browsing, search, secure checkout, reviews, and personalized recommendations. It guarantees high availability and regulatory compliance for millions of global active users.

## Key Elements
- **Customers & Marketing Manager**: Primary human actors interacting with the system.
- **Recommendation API Controller**: FastAPI service handling real-time recommendation requests.
- **Rules & Merchandising Engine**: FastAPI component managing business overrides and fallback lists.
- **Async Batch Inference Worker**: AWS SageMaker / ECS task handling offline machine learning workloads.
- **Data Access & Privacy Layer**: Boto3-based component interacting with storage and event queues.
- **Amazon DynamoDB**: Multi-region database utilizing Global Tables with AWS KMS encryption.
- **Amazon SQS / EventBridge**: Messaging backbone for user activity and GDPR purge events.

## Relationships
- **Recommendation API Controller -> Amazon DynamoDB**: Reads pre-computed vectors via TLS [<10ms].
- **Recommendation API Controller & Rules Engine**: In-process function calls.
- **Async Batch Inference Worker -> Amazon SQS**: Consumes user activity streams via AMQP.
- **Data Access & Privacy Layer -> Amazon DynamoDB**: Performs TLS-encrypted writes and GDPR purges.

## Technology Stack
- **Python / FastAPI**: Chosen for the Recommendations Service to deliver high-performance asynchronous API handling.
- **Amazon DynamoDB (Global Tables)**: Selected for multi-region low-latency data replication and high scalability.
- **AWS SageMaker / ECS Tasks**: Used for isolated, offline batch machine learning inference to protect online API performance.
- **AWS KMS**: Implemented for regional encryption-at-rest to satisfy strict GDPR and CCPA security constraints.

## Rationale
Decoupling heavy offline batch inference from the online API path prevents resource exhaustion and ensures sub-2-second page loads on 3G networks. Multi-region DynamoDB replication and strict security controls guarantee 99.95% availability while meeting global compliance mandates.