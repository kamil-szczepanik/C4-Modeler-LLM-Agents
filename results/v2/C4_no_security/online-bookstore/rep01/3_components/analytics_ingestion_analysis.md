## Overview
[The Analytics Ingestion container provides real-time event streaming and clickstream processing for the Online Bookstore. It securely ingests user interaction data to power recommendations while strictly enforcing GDPR and CCPA compliance.]

## Key Elements
- **Ingestion API Handler** (Go, HTTP/JSON)
- **Sanitization & Validation Middleware** (Go)
- **Buffer & Retry Manager** (Go, In-memory ring-buffer)
- **Kinesis Producer Client** (Go, AWS SDK for Go)
- **Amazon Kinesis** (AWS Streaming Service)
- **AWS SQS** (Dead-letter queue fallback)

## Relationships
- **API Management -> Ingestion API Handler**: Forwards clickstream requests [HTTPS/JSON]
- **Ingestion API Handler -> Sanitization & Validation Middleware**: Passes raw event payloads [In-memory Go structs]
- **Sanitization & Validation Middleware -> Buffer & Retry Manager**: Offloads validated events during throttling [In-memory Go channels]
- **Buffer & Retry Manager -> Amazon Kinesis**: Publishes event streams with exponential backoff [AWS Kinesis API over HTTPS/TCP]
- **Buffer & Retry Manager -> AWS SQS**: Stores overflow events during prolonged outages [AWS SQS API over HTTPS]

## Technology Stack
- **Go**: Chosen for high-throughput, low-latency concurrent processing of clickstream events.
- **Amazon Kinesis**: Selected for real-time streaming scale supporting 1M MAU.
- **AWS SDK for Go**: Utilized for resilient AWS service integration.
- **CloudWatch & Prometheus**: Deployed for operational metrics and throughput alarms.

## Rationale
[This architecture ensures high availability and sub-10ms processing overhead while preventing Personally Identifiable Information (PII) leakage through local sanitization. The buffer and retry mechanism guarantees fault tolerance and zero data loss during traffic surges.]