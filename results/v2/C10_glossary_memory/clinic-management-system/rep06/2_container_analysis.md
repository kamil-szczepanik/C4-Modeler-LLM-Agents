## Overview
- A hybrid-cloud Clinic Management System designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing.
- Ensures high availability (99.99%), HIPAA/GDPR compliance, and sub-second EMR performance while securely integrating with external health systems and clearinghouses.

## Key Elements
- Patients (Person)
- Receptionists/Admins (Person)
- Clinicians/Doctors (Person)
- Billing Specialists (Person)
- Compliance/Security Officers (Person)
- Hospital/Clinic Management (Person)
- Patient Portal (Container)
- Internal Staff Application (Container)
- API Gateway (Container)
- Patient Admission Service (Container)
- Scheduling Service (Container)
- EMR Service (Container)
- Billing Service (Container)
- Integration Engine (Container)
- Data Store (Container)
- External Identity Provider (IdP) (External System)
- External Lab & Imaging Systems (External System)
- Insurance Clearinghouse (External System)

## Relationships
- Patients -> Patient Portal: HTTPS (Web/Mobile)
- Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance Officers, Management -> Internal Staff Application: HTTPS (Web)
- Patient Portal & Internal Staff Application -> API Gateway: HTTPS (mTLS/OIDC)
- API Gateway -> Core Services (Admission, Scheduling, EMR, Billing): gRPC / REST over internal mesh
- Integration Engine -> External Lab & Imaging Systems: HL7 FHIR over HTTPS (REST/JSON) with mTLS
- Integration Engine -> Insurance Clearinghouse: EDI over SFTP / HTTPS
- Core Services -> Data Store: PostgreSQL protocol with AES-256

## Technology Stack
- Frontend: React / TypeScript served via Nginx for high-performance UI rendering
- API Gateway: Kong / Envoy for mTLS, rate limiting, and token validation
- Backend Services: Go / Node.js for Core Services and Java Spring Boot for Billing to ensure high throughput
- Database & Storage: PostgreSQL (multi-region, active-passive) with AES-256 encryption at rest, plus WORM object storage for 10-year audit retention
- Infrastructure & Security: Kubernetes (`on-prem-k8s` and `eu-central-1`), Istio/Linkerd service mesh, HashiCorp Vault for secrets management

## Rationale
- Segregating public patient portals from high-privilege internal staff applications isolates attack surfaces and ensures strict boundary-level access control.
- Utilizing Go/Node.js for core microservices alongside an optimized active-passive PostgreSQL topology guarantees sub-second EMR screen loads and 99.99% availability without split-brain write conflicts.