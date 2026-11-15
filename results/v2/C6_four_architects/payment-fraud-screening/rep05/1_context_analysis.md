## Overview
This system screens card-not-present payment authorizations for fraud in real-time and provides a case management interface for analysts to review suspicious transactions. It ensures sub-50ms latency at high throughput while maintaining PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
* Payment Gateway / Core Ledger
* Fraud Analyst
* Card Schemes / Tokenization Provider
* Identity Provider (IdP)
* Notification Service
* API Gateway / Edge Router (Envoy / AWS API Gateway)
* Scoring Engine (Go / Rust)
* Case Management Backend (Node.js / Python)
* Feature Store (Redis / Dragonfly)
* Audit & Transaction Datastore (AWS Aurora PostgreSQL with S3 Object Lock)
* Async Event Bus (AWS EventBridge)
* Model Registry / Rule Storage (AWS S3)
* Frontend Application (React on AWS S3 + CloudFront)
* Background Worker / Model Synchronizer (Go)

## Relationships
* Payment Gateway to API Gateway / Edge Router via gRPC (mTLS)
* API Gateway to Scoring Engine via gRPC
* Scoring Engine to Feature Store via TCP/RESP
* Scoring Engine to Async Event Bus via Async Event
* Async Event Bus to Case Management Backend via Event Push
* Fraud Analyst to Frontend Application via HTTPS
* Frontend Application to API Gateway via HTTPS / WebSockets
* Background Worker to Model Registry via HTTPS

## Technology Stack
* AWS (eu-west-1): Cloud provider hosting all infrastructure within the fixed budget constraints
* Go / Rust: Powers the high-performance Scoring Engine to guarantee sub-50ms P99 latency
* Redis / Dragonfly: Acts as the low-latency Feature Store for real-time velocity lookups
* AWS Aurora PostgreSQL with S3 Object Lock: Provides tamper-evident storage for 7-year audit compliance
* AWS S3 + CloudFront: Hosts the React frontend with minimal operational overhead for a 3-engineer team

## Rationale
The architecture combines a stateless Go/Rust scoring container with an in-memory Redis feature store to achieve sub-50ms P99 latency at 3,000 TPS. Using AWS-managed serverless primitives minimizes operational burden, fitting within the 25,000 EUR monthly budget and supporting a 3-engineer team.