## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for unstable network connections.

## Key Elements
- **Patients & Clinicians**: External users accessing the platform via mobile and web apps.
- **Google Cloud Global Load Balancer & Cloud Armor**: Anycast IP termination, WAF, and geo-based rate-limiting.
- **API Gateway / BFF**: Built with Go, handling gRPC and REST routing.
- **Core Telehealth Service**: Node.js and TypeScript backend logic.
- **Video Consultation Service**: Golang with LiveKit WebRTC SFU supporting low-bandwidth degraded modes.
- **AI Orchestrator**: Python with FastAPI for traceable symptom checking.
- **E-Prescription Integrator**: Java with Spring Boot.
- **Data Storage**: Cloud SQL (PostgreSQL), Cloud Storage, and Cloud Bigtable.

## Relationships
- Patients & Clinicians -> Google Cloud Global Load Balancer & Cloud Armor: Accesses platform features [HTTPS, WebSockets with geo-routing]
- Google Cloud Global Load Balancer & Cloud Armor -> API Gateway / BFF (Regional NEGs): Routes regionally-pinned traffic [HTTPS]
- API Gateway / BFF -> Core Telehealth Service & Microservices: Internal orchestration [gRPC]
- Video Consultation Service -> Patients: Streams video [WebRTC with adaptive bitrate]
- AI Orchestrator -> AI Model Provider / LLM API: Sends anonymized prompts [HTTPS]
- E-Prescription Integrator -> National Pharmacy Networks (EU) & US Pharmacy Systems: Transmits prescriptions [REST/HL7 FHIR/National Standards]

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data isolation.
- **Load Balancing**: Google Cloud HTTP(S) Global Load Balancing with Cloud Armor for geo-routing and security.
- **Video Streaming**: LiveKit (WebRTC SFU) to handle unstable rural connections below 300 kbit/s.
- **Database & Storage**: Cloud SQL (PostgreSQL), Cloud Storage, and Cloud Bigtable with region-specific deployments.
- **Interoperability**: HL7 FHIR for US systems and national e-prescription standards for the EU.

## Rationale
This architecture uses GCP multi-region deployment to strictly separate EU and US health data, satisfying GDPR and HIPAA requirements. Regional NEGs and LiveKit ensure low-latency regional routing and resilient video streaming for rural users.