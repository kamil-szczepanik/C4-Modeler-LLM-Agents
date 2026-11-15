## Overview
[System: Online Bookstore System (Recommendation Service container). Core Purpose: Provides personalized 'Customers also bought' book recommendations for shoppers.]

## Key Elements
* Shopper
* Recommendation Service (Container, Python, FastAPI, AWS ECS Fargate)
* API Router / Component (FastAPI)
* Recommendation Orchestrator Component
* External Engine Client Component
* Recommendation Analytics & Feedback Component
* Third-Party Recommendation Engine (External System)
* Amazon SQS / AWS EventBridge
* AWS Secrets Manager, AWS X-Ray, AWS Security Groups

## Relationships
* Shopper -> Recommendation Service: Views recommendations [HTTPS via API Gateway & AWS App Mesh]
* API Router Component -> Recommendation Orchestrator Component: Forwards validated requests [Internal Python function call]
* Recommendation Orchestrator Component -> External Engine Client Component: Queries external engine [Internal Python function call]
* External Engine Client Component -> Third-Party Recommendation Engine: Fetches recommendations with circuit breakers [HTTPS API calls with Envoy]
* Recommendation Orchestrator Component -> Recommendation Analytics & Feedback Component: Emits interaction events [JSON over Amazon SQS / AWS EventBridge]

## Technology Stack
* Python & FastAPI: Core runtime and framework for fast request processing
* AWS ECS Fargate: Serverless container deployment for autoscaling
* Amazon SQS / AWS EventBridge: Asynchronous message bus for non-blocking analytics
* AWS Secrets Manager: Dynamic credential injection for external APIs
* AWS X-Ray & Envoy: Distributed tracing and sidecar proxy for telemetry and routing
* AWS Security Groups & Network Firewall: Strict egress filtering to whitelist external endpoints

## Rationale
[This architecture enforces strict separation of concerns by removing non-core currency logic and utilizing asynchronous messaging, ensuring sub-2-second performance and 99.95% availability under high load. It maintains GDPR/CCPA compliance through rigorous PII pseudonymization, least-privilege IAM roles, and secure egress filtering.]