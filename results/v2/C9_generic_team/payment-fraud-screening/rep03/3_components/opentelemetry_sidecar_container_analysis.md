## Overview
The OpenTelemetry Sidecar Container provides lightweight, stateless telemetry collection for the Real-Time Payment Fraud Screening system on AWS ECS Fargate. It ensures high-performance observability while protecting system latency and budget constraints.

## Key Elements
- OpenTelemetry Sidecar Container (AWS Distro for OpenTelemetry)
- Modular Monolith Core Scoring Engine (AWS ECS Fargate)
- Monitoring Backend
- AWS SSM Parameter Store

## Relationships
- OpenTelemetry Sidecar Container -> Monitoring Backend: Exports telemetry and metrics [OTLP over gRPC/HTTP with Gzip compression]
- Modular Monolith Core Scoring Engine -> OpenTelemetry Sidecar Container: Sends telemetry and queries queue health [HTTP/gRPC over localhost]
- OpenTelemetry Sidecar Container <- AWS SSM Parameter Store: Retrieves centralized collector configurations [AWS API]

## Technology Stack
- AWS Distro for OpenTelemetry (ADOT): Chosen for standardized, zero-code OpenTelemetry semantic conventions.
- AWS ECS Fargate: Utilized with strict CPU/memory limits and startup dependencies for resource isolation.
- AWS SSM Parameter Store: Selected for centralized, zero-redeploy configuration management.
- Gzip OTLP Compression: Implemented to minimize network bandwidth and cloud egress costs.

## Rationale
This architecture fits the requirements by enforcing stateless sidecar patterns, resource limits, and head-based sampling that protect the strict <50 ms P99 latency threshold. Furthermore, it minimizes operational toil for a three-engineer team while maintaining compliance and staying within the 25k EUR monthly budget.