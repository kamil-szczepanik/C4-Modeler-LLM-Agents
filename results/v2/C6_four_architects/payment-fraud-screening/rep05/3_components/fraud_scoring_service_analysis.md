## Overview
The Fraud Scoring Service screens card-not-present payment authorizations in real-time to detect fraud, while enabling analyst reviews. It ensures PCI-DSS compliance and sub-50ms P99 latency within AWS constraints.

## Key Elements
* API Handler Component (Python, FastAPI)
* Feature Aggregator Component (Python, async Redis client)
* Inference Engine Component (C-based ONNX Runtime via Python bindings)
* Rules Evaluator Component (Python, lightweight expression engine)
* Audit Dispatcher Component (Python, boto3)
* Model & Rule Manager Component (Python, background thread/async task)

## Relationships
* API Handler -> Feature Aggregator: Requests user velocity features [In-memory async call]
* API Handler -> Rules Evaluator: Evaluates hard-coded and dynamic business rules [In-memory call]
* API Handler -> Inference Engine: Invokes ONNX model for probabilistic scoring [In-memory C-binding call]
* API Handler -> Audit Dispatcher: Dispatches payload for asynchronous logging [Non-blocking queue]
* Model & Rule Manager -> Amazon S3 Model Registry: Fetches artifacts [HTTPS]
* Model & Rule Manager -> Inference Engine & Rules Evaluator: Updates active models/rules [Thread-safe reference swap]
* Feature Aggregator -> Amazon ElastiCache (Redis): Retrieves user profiling data [TCP/RESP]
* Audit Dispatcher -> Amazon SQS: Publishes tamper-evident audit events [HTTPS]

## Technology Stack
* Python & FastAPI: Powers the API Handler for high-throughput request validation and routing.
* ONNX Runtime: Executes serialized machine learning models in-memory to meet strict sub-50ms latency targets.
* Amazon ECS Fargate: Runs the containerized service within fixed infrastructure budgets.
* Amazon ElastiCache (Redis): Stores low-latency feature states and velocity counters.
* Amazon S3 Model Registry: Stores versioned ML models and JSON rules for zero-downtime hot-reloading.

## Rationale
This architecture uses in-process components and C-based ONNX inference to eliminate network hops and meet the stringent sub-50ms P99 latency requirement. Decoupled asynchronous components and thread-safe hot-swapping ensure zero-downtime updates and strict PCI-DSS data protection within the 25,000 EUR monthly AWS budget.