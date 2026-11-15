## Overview
The Online Bookstore system utilizes an AWS-powered static asset and media storage container to deliver high-performance e-commerce experiences globally. It provides secure, low-latency distribution of React SPA artifacts and encrypted digital e-books while enforcing strict GDPR and CCPA compliance.

## Key Elements
* Static Web Hosting Bucket (Amazon S3)
* Digital Assets Bucket (Amazon S3)
* CDN Distribution (Amazon CloudFront with Lambda@Edge)
* Access Logging Bucket (Amazon S3)
* Media Processing Trigger (AWS Lambda)

## Relationships
* React SPA Container -> CDN Distribution: Loads static JS/CSS/HTML via HTTPS
* Catalog & Order Services -> CDN Distribution: Requests signed URLs for e-book downloads via HTTPS
* CDN Distribution -> Digital Assets Bucket: Fetches private media via Origin Access Control (OAC) and HTTPS
* CDN Distribution -> Access Logging Bucket: Streams access logs via S3 API and HTTPS
* Privacy Service -> Digital Assets Bucket: Manages data deletion and anonymization via AWS SDK (HTTPS)
* Digital Assets Bucket -> Media Processing Trigger: Invokes processing upon new image upload via S3 Event Notifications (JSON/HTTPS)

## Technology Stack
* Amazon S3 (Standard): Stores built React SPA artifacts and logs with lifecycle policies.
* Amazon S3 (Standard-IA/Glacier): Securely stores encrypted e-book files and high-resolution media.
* Amazon CloudFront: Edge-caches static assets and protects digital books using signed URLs.
* Lambda@Edge: Validates signed URLs at the edge for optimal performance.
* Python / AWS Lambda: Automatically optimizes and generates thumbnails for user-uploaded review images.

## Rationale
This architecture leverages Amazon CloudFront and Lambda@Edge to meet the strict sub-2-second page load requirement on 3G connections. Furthermore, integrating Origin Access Control, signed URLs, dedicated logging buckets, and Privacy Service hooks ensures robust OWASP security and seamless GDPR/CCPA compliance.