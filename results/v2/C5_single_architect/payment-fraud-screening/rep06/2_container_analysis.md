## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS for a mid-size payment processor. It provides real-time scoring, analyst case management, and tamper-evident auditing.

## Key Elements
* Payment Gateway / Acquirer Systems
* Fraud Analysts and Auditors
* AWS API Gateway (REST)
* Scoring Engine (Go microservice on AWS ECS Fargate)
* Case Management Backend (Node.js/Go service on ECS Fargate)
* Amazon DynamoDB and Amazon Aurora PostgreSQL
* Amazon Kinesis Data Firehose and Amazon S3 with Object Lock

## Relationships
* Payment Gateway to AWS API Gateway via HTTPS/JSON for authorization requests
* Scoring Engine to Amazon DynamoDB via AWS SDK for rule/model state
* Scoring Engine to Amazon Kinesis Data Firehose via HTTPS for audit logs
* Kinesis Data Firehose to Amazon S3 Object Lock for 7-year immutable retention
* Fraud Analysts to Case Management Backend via HTTPS for case reviews

## Technology Stack
* AWS ECS (Fargate) for minimal operational overhead with a 3-engineer team
* Go for the Scoring Engine to ensure sub-50ms P99 latency at 3,000 req/s
* Amazon DynamoDB for low-latency state and audit logs
* Amazon S3 with Object Lock for PCI-DSS Level 1 compliant tamper-evident storage

## Rationale
This architecture uses serverless and managed AWS components to meet strict PCI-DSS and audit requirements while staying within a 25,000 EUR monthly budget. It prioritizes low-latency technologies (Go, ECS Fargate, DynamoDB) to achieve sub-50ms P99 performance at scale.