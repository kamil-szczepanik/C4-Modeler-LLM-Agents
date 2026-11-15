## Overview
- Secure, highly available Checkout/Payment Container handling multi-currency transactions and payment processing for the global online bookstore.
- Ensures strict compliance with GDPR, CCPA, and PCI-DSS mandates while maintaining sub-second latency across three AWS regions.

## Key Elements
- **Customer (Shopper):** Primary user driving checkout and payment interactions.
- **Checkout/Payment Container:** Core microservice processing secure transactions, idempotency, and localized totals.
- **Third-Party Payment APIs:** External system for payment authorization and processing.
- **Currency Localization Container:** Internal service providing localized pricing in USD, EUR, and GBP.
- **AWS Infrastructure:** Amazon EKS, AWS KMS, AWS Secrets Manager, AWS CloudWatch, and Istio service mesh.

## Relationships
- **Customer (Shopper) -> API Gateway:** Initiates checkout and payment requests [HTTPS]
- **API Gateway -> Checkout/Payment Container:** Routes internal requests [mTLS via Istio service mesh]
- **Checkout/Payment Container -> Third-Party Payment APIs:** Authorizes payments with circuit breakers [HTTPS with circuit breakers]
- **Checkout/Payment Container -> Currency Localization Container:** Retrieves localized totals and taxes [gRPC / REST]
- **Checkout/Payment Container -> AWS Secrets Manager:** Fetches encrypted API credentials dynamically [IRSA / IAM]

## Technology Stack
- **Orchestration:** Amazon EKS with ArgoCD for GitOps deployments and canary rollouts.
- **Security & Networking:** Istio service mesh for mTLS and egress filtering, AWS KMS for encryption at rest, AWS Secrets Manager for runtime secrets.
- **Runtime Security:** eBPF-based security (Cilium Tetragon / Falco) within a dedicated PCI-scoped Kubernetes namespace.
- **Observability:** Prometheus, Datadog, AWS X-Ray, and OpenTelemetry for distributed tracing and SLO monitoring.

## Rationale
- Multi-region active-active readiness across `us-east-1`, `eu-west-1`, and `ap-southeast-1` ensures 99.95% availability and performance under 1M MAU scale.
- Zero local PCI-DSS storage, client-side tokenization, and strict network isolation mitigate OWASP Top-10 risks and guarantee regulatory compliance.