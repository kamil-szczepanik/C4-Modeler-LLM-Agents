## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages suspicious payment reviews for a mid-size payment processor. It operates on AWS in the eu-west-1 region to ensure strict PCI-DSS Level 1 compliance, high availability, and auditability.

## Key Elements
* Fraud Analyst, ML Engineer / Data Scientist, Finance / Operations Manager, Merchant / Merchant Success Manager, and Compliance / Risk Officer
* Payment Gateway / Core Processing Engine and Card Schemes / Identity Providers
* AWS API Gateway / NLB (Ingress)
* Fraud Scoring Engine (Go microservice)
* Case Management Backend (Java / Spring Boot with React UI)
* Audit Logger (AWS Lambda / Worker)
* Feature Store (AWS ElastiCache for Redis)
* Relational Store (Amazon RDS for PostgreSQL)
* Tamper-Evident Storage (Amazon S3 with Object Lock in Compliance Mode)
* Message Queue (Amazon SQS with AWS KMS encryption)

## Relationships
* Payment Gateway / Core Processing Engine routes authorization traffic to AWS API Gateway / NLB via HTTPS
* AWS API Gateway / NLB invokes Fraud Scoring Engine via gRPC
* Fraud Scoring Engine queries AWS ElastiCache for Redis via low-latency TCP
* Fraud Scoring Engine asynchronously publishes decision payloads to Amazon SQS
* Audit Logger consumes from Amazon SQS and writes tamper-evident logs to Amazon S3 with Object Lock
* Fraud Analysts and Managers access Analyst UI / Case Management via HTTPS/REST
* Case Management Backend persists state in Amazon RDS for PostgreSQL

## Technology Stack
* AWS API Gateway / NLB: Edge ingress and tokenization for PCI-DSS scope reduction
* Go: High-performance language for Fraud Scoring Engine to meet <50ms P99 latency
* Java / Spring Boot & React: Robust backend and frontend for Case Management and merchant analytics
* AWS ElastiCache for Redis: Low-latency feature store for real-time model scoring
* Amazon RDS for PostgreSQL: Relational persistence for case management data
* Amazon SQS: Asynchronous message decoupling to protect scoring latency
* Amazon S3 with Object Lock: WORM storage guaranteeing 7-year tamper-evident auditability

## Rationale
The architecture utilizes Go and gRPC to strictly satisfy the sub-50ms P99 performance requirement under heavy load. Asynchronous SQS queuing and S3 Object Lock compliance mode securely enforce 7-year tamper-evident auditability and PCI-DSS compliance without impacting real-time transaction latency or exceeding the 25,000 EUR monthly infrastructure budget.