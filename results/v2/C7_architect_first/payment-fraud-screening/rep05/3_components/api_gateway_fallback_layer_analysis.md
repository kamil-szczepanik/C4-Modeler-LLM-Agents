## Overview
[The API Gateway & Fallback Layer secures, routes, and monitors ingress REST/JSON traffic for the Real-Time Payment Fraud Screening system while ensuring zero-downtime availability.]

## Key Elements
* Ingress Router (Amazon API Gateway)
* Circuit Breaker & Fallback Engine (AWS Lambda)
* Telemetry & Audit Emitter (Amazon CloudWatch / AWS X-Ray)
* AWS WAF
* AWS CodeDeploy
* CloudWatch Synthetics Canary

## Relationships
* Payment Gateway / Acquirer Systems -> Ingress Router: Sends ingress REST/JSON traffic for authorization [HTTPS / mTLS / SigV4]
* Ingress Router -> Circuit Breaker & Fallback Engine: Routes scoring requests [AWS Lambda internal invocation]
* Circuit Breaker & Fallback Engine -> Real-Time Scoring Service: Forwards scoring requests [REST/gRPC]
* Telemetry & Audit Emitter -> Immutable Audit Log Sink: Pushes sanitized request metadata [HTTPS]

## Technology Stack
* Amazon API Gateway: Terminates TLS, enforces WAF rules, and handles rate limiting with minimal operational overhead.
* AWS Lambda: Executes serverless fallback logic to satisfy budget constraints (<= 25k EUR/month).
* AWS X-Ray & CloudWatch: Provides distributed tracing for sub-50ms P99 latency tracking.
* CloudWatch Synthetics: Runs 24/7 mock payment checks for proactive availability monitoring.
* AWS CodeDeploy: Manages canary deployments for zero-downtime rule updates.

## Rationale
[This serverless edge architecture maintains strict PCI-DSS compliance and high availability within a lean 3-engineer team capacity. It guarantees zero merchant disruption during downstream outages while enforcing strict payload sanitization.]