## Overview
The Explainability Service asynchronously processes real-time fraud scoring events to generate human-readable explanations and audit trails. It ensures compliance and analyst efficiency without impacting the core scoring engine's latency.

## Key Elements
* Explainability Service (Python, FastAPI container)
* Event Consumer Component (Python, Celery/FastAPI background worker)
* SHAP Calculator Component (Python, `shap` library + ONNX Runtime)
* Feature Formatter Component (Python)
* Audit & Indexing Dispatcher (Python, AWS SDK)
* Amazon SQS
* Amazon S3 Object Lock
* Feature Store & Metadata DB (PostgreSQL RDS)
* AWS Secrets Manager / AWS IAM

## Relationships
* Real-Time Scoring Engine -> Amazon SQS: Emits scoring event payloads [JSON over AWS SDK]
* Event Consumer Component -> Amazon SQS: Consumes scoring events [Pull via AWS SDK]
* Audit & Indexing Dispatcher -> Amazon S3 Object Lock: Writes tamper-readable explanations [HTTPS / AWS SDK]
* Audit & Indexing Dispatcher -> Feature Store & Metadata DB (PostgreSQL RDS): Updates explanation metadata [SQL over psycopg2]

## Technology Stack
* Python & FastAPI: High-performance asynchronous processing for microservices
* `shap` library & ONNX Runtime: Efficient calculation of feature attribution weights
* Amazon SQS: Asynchronous message decoupling to protect P99 scoring latency
* Amazon S3 Object Lock (Compliance Mode): Tamper-evident 7-year audit retention
* PostgreSQL RDS & AWS Secrets Manager: Secure metadata storage and least-privilege database access

## Rationale
Decoupling via Amazon SQS preserves the strict 50 ms P99 latency target while supporting rigorous audit requirements. S3 Object Lock in Compliance Mode and tokenized payloads satisfy PCI-DSS Level 1 compliance and 7-year regulatory mandates.