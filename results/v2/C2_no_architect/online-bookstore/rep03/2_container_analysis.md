## Overview
[Global E-Commerce Platform designed for high-availability book retail, supporting 1M MAU across three AWS regions while enforcing strict GDPR/CCPA compliance and OWASP security controls.]

## Key Elements
*   **People:** Customer (Shopper), Site Administrator, Content Moderator, Customer Support Agent.
*   **Systems:** Warehouse / Fulfillment Partner, Third-Party Payment APIs.
*   **Containers:** API Gateway, Catalog Container, Recommendation Engine Container, Checkout/Payment Container, Currency Localization Container, Support/Moderation Portals.
*   **Infrastructure:** AWS CloudFront, AWS WAF, Amazon EKS, AWS KMS, AWS Secrets Manager, AWS X-Ray.

## Relationships
*   **Customer to AWS CloudFront:** Browses catalogue and executes secure checkout via HTTPS.
*   **AWS CloudFront to API Gateway:** Forwards regional traffic using HTTPS.
*   **API Gateway to Containers:** Routes internal requests using mTLS via service mesh.
*   **Containers to Third-Party Systems:** Integrates with payment APIs and shipping partners via HTTPS with circuit breakers.

## Technology Stack
*   **Cloud Provider:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region active-active deployment.
*   **Orchestration:** Amazon EKS for container management and autoscaling.
*   **Deployment:** GitOps via ArgoCD for continuous delivery and environment parity.
*   **Security & Compliance:** AWS WAF, AWS KMS, AWS Secrets Manager, and Istio/AWS App Mesh for mTLS.
*   **Observability:** AWS X-Ray for distributed tracing and centralized SIEM for audit logging.

## Rationale
[Separating high-traffic catalog and recommendation workloads from sensitive checkout containers ensures PCI-DSS compliance and protects payment availability under heavy load. Multi-region EKS deployment with edge caching guarantees sub-2-second page loads and 99.95% uptime for a global user base.]