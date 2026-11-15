## Overview
The Online Bookstore system is a scalable e-commerce platform designed for purchasing physical and electronic books, featuring reviews and personalized recommendations. It utilizes AWS CloudFront and Amazon S3 to securely deliver static assets globally while meeting strict performance and availability requirements.

## Key Elements
* Customers (End-users accessing via web and mobile)
* AWS CloudFront (Content Delivery Network at the edge)
* Amazon S3 (Primary and replicated object storage buckets)
* AWS WAF (Web Application Firewall integrated at the edge)
* CloudFront Functions (Edge compute for dynamic configuration and nonces)
* CloudWatch Synthetics (Global monitoring canaries)

## Relationships
* Customers -> AWS CloudFront: Fetch static assets and SPA via HTTPS
* AWS CloudFront -> Amazon S3: Origin fetch via Origin Access Control (OAC) using SigV4
* Amazon S3 (Primary) -> Amazon S3 (Replication Bucket): Cross-Region Replication (CRR) via HTTPS
* AWS WAF -> AWS CloudFront: Inspects and filters inbound traffic at the edge

## Technology Stack
* AWS CloudFront: Global CDN for low-latency asset delivery and edge security enforcement
* Amazon S3: Durable object storage with Cross-Region Replication (CRR) for high availability
* AWS WAF: Edge-level rate-limiting and DDoS/OWASP protection
* CloudFront Functions: Lightweight edge compute for runtime configuration injection and CSP nonces
* Terraform/AWS CDK & Checkov: Infrastructure as Code and automated policy-as-code guardrails

## Rationale
This architecture leverages a globally distributed CDN and object storage to satisfy the sub-2-second page load SLA on 3G networks and 99.95% availability. Edge security controls and immutable asset versioning ensure compliance with OWASP Top-10 requirements and data protection standards.