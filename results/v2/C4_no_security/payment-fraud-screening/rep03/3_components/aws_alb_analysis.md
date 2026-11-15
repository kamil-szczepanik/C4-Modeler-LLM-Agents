## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud and manage reviews. It ensures high availability, PCI-DSS compliance, and sub-50ms decision latency for mid-size payment processors.

## Key Elements
* Payment Gateway (External System)
* AWS Application Load Balancer (ALB) (Container)
* Scoring Engine Container (Go/Rust, AWS ECS Fargate) (Container)
* Case Management Container (Node.js, AWS ECS Fargate) (Container)
* Amazon ElastiCache Redis (Container)
* Amazon SQS / Kinesis Data Firehose (Container)
* Amazon S3 Object Lock (Container)
* Fraud Analyst & Risk Manager (Person)

## Relationships
* Payment Gateway -> AWS Application Load Balancer: Routes authorization requests [HTTPS]
* AWS Application Load Balancer -> Scoring Engine Container: Forwards valid requests [HTTP/2 over TLS]
* Scoring Engine Container -> Amazon ElastiCache Redis: Low-latency feature lookups [Redis Protocol]
* Scoring Engine Container -> Amazon SQS / Kinesis Data Firehose: Async event publishing [AWS SDK / HTTPS]
* Case Management Container -> Amazon S3 Object Lock: Tamper-evident audit storage [AWS API / HTTPS]

## Technology Stack
* AWS ECS Fargate: Runs backend services without server management to fit the 3-engineer team constraint.
* AWS Application Load Balancer: Handles SSL termination, WAF, and native target group health checks for traffic routing.
* Go / Rust: Ensures P99 decision latency below 50 ms for scoring.
* Node.js: Powers the case management and analyst reporting interface.
* Amazon S3 Object Lock: Implements tamper-evident audit storage for 7-year retention requirements.

## Rationale
This architecture leverages managed AWS primitives to meet strict PCI-DSS Level 1 compliance and sub-50ms latency SLAs within a fixed 25,000 EUR monthly budget. It minimizes operational overhead, allowing a three-engineer team to maintain high reliability and zero-downtime updates.