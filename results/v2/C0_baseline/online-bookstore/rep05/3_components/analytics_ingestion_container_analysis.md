## Overview
The Analytics Ingestion Container collects, sanitizes, and streams real-time telemetry for the Online Bookstore across multiple global regions. It ensures high-throughput, low-latency event processing while strictly enforcing GDPR and CCPA compliance.

## Key Elements
* **Analytics Ingestion Container**: Core ECS Fargate container running Node.js/Fastify
* **Ingestion API Endpoint**: Fastify REST/WebSocket server receiving telemetry
* **Consent & PII Sanitizer Middleware**: Component validating cryptographic consent proofs and masking PII
* **Event Validator & Enricher**: Schema validation and timestamp appending component
* **Telemetry Dispatcher**: Forwards events to streaming storage with SQS DLQ overflow
* **Amazon Kinesis Data Stream**: Downstream event streaming pipeline
* **Amazon SQS (DLQ)**: Dead-letter queue for backpressure management

## Relationships
* **SPA** -> **Amazon API Gateway**: Sends telemetry (`HTTPS/WSS`)
* **Amazon API Gateway** -> **Ingestion API Endpoint**: Forwards authenticated telemetry (`HTTPS/WSS`, AWS IAM SigV4)
* **Telemetry Dispatcher** -> **Amazon Kinesis Data Stream**: Streams sanitized events (`TCP/AWS SDK`)
* **Telemetry Dispatcher** -> **Amazon SQS (DLQ)**: Offloads failed ingestion events (`TCP/AWS SDK`)

## Technology Stack
* **Amazon ECS (Fargate)**: Container runtime for scalable, serverless microservice execution
* **Node.js / Fastify**: Chosen for high-throughput, low-latency asynchronous event processing
* **Amazon Kinesis Data Streams**: Real-time event ingestion pipeline meeting <5s freshness
* **Amazon SQS**: Dead-letter queue implementation for backpressure and failure overflow
* **AWS KMS**: Regional customer-managed encryption keys for data sovereignty

## Rationale
This architecture uses Node.js on ECS Fargate behind Kinesis to scale effortlessly to 1M MAU while guaranteeing sub-5-second data freshness. Integrated regional KMS keys and sanitization middleware ensure strict GDPR and CCPA compliance without degrading client-side performance.