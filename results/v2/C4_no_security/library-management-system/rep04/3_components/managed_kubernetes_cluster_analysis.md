## Overview
The Library Management System utilizes a cloud-native container infrastructure hosted in the EU to catalogue items, manage circulation, and provide self-service portals. It guarantees EU-only data residency, zero-downtime deployments, and audit compliance.

## Key Elements
*   **Managed Kubernetes Cluster (EKS/AKS)**: EU-central deployment infrastructure enforcing data residency.
*   **GitOps Operator (ArgoCD)**: Declarative continuous delivery and zero-downtime rolling updates.
*   **Ingress Controller (Nginx Ingress)**: Routes external traffic with TLS termination.
*   **Cluster Autoscaler & HPA**: Dynamically scales nodes and pods for cost efficiency during off-peak hours.
*   **OpenTelemetry Collector & Fluentbit**: DaemonSets for batch-exporting logs, metrics, and API server audit logs.
*   **Backup Tool (Velero)**: Automated encrypted cluster-state backups.

## Relationships
*   **Managed Kubernetes Cluster -> EU-hosted Log & Metrics Aggregator**: Streams telemetry and audit logs [OpenTelemetry/Vector over HTTPS].
*   **API Gateway -> Ingress Controller**: Routes external user and staff traffic [HTTPS].
*   **ArgoCD -> Git Repository**: Pulls declarative manifests for continuous deployment [HTTPS].

## Technology Stack
*   **Kubernetes (EKS/AKS in EU-central)**: Cloud container orchestration ensuring strict data residency.
*   **ArgoCD**: GitOps deployment engine enabling continuous delivery and rollback capabilities.
*   **Nginx Ingress**: Edge routing and TLS termination.
*   **OpenTelemetry & Fluentbit**: Observability and compliance log forwarding.
*   **Velero**: Disaster recovery state management targeting EU object storage.

## Rationale
This architecture ensures strict compliance with EU data residency laws while optimizing operational costs for public libraries through autoscaling and native Kubernetes controls. GitOps automation and strict PodDisruptionBudgets guarantee high availability and continuous release velocity without downtime.