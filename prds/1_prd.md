# Product Requirements Document: TalentProof
## Agentic Talent Intelligence Platform

**Version:** 1.0  
**Last Updated:** January 2026  
**Status:** Draft

---

## Executive Summary

**TalentProof** is an Agentic Talent Intelligence Platform that solves the two biggest problems in modern technical hiring:

1. **The Black Box Problem** — AI tools that give scores without explanations
2. **The Paper Tiger Problem** — Candidates with AI-optimized resumes who fail technical interviews

### Vision Statement

> Transform technical hiring from "resume filtering" to "talent verification" by combining explainable AI reasoning with real-world proof-of-work verification.

### Target Users

| User | Primary Pain | Job to Be Done |
|------|-------------|----------------|
| **Technical Recruiters** | 500+ applicants per role, can't verify claims | Narrow to top 10 verified candidates in minutes |
| **Engineering Managers** | Paper tigers waste interview slots | Only interview candidates with proven skills |
| **Recruiting Agencies** | Clients blame them for bad hires | Verify before presenting candidates |

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Screening Accuracy** | 80%+ of "High Match" candidates pass first technical round | Post-interview feedback loop |
| **Time Saved** | 80% reduction in manual CV review | Time tracking comparison |
| **User Retention** | 70%+ return for second job posting | Monthly cohort analysis |
| **NPS Score** | 50+ | Quarterly surveys |

---

## Product Phases Overview

| Phase | Name | Duration | Focus | Key Outcome |
|-------|------|----------|-------|-------------|
| **Phase 1** | Foundation & Core Screening | 6-8 weeks | Basic screening with XAI | Working MVP with explainable rankings |
| **Phase 2** | Verification Engine | 4-6 weeks | GitHub/LinkedIn verification | Proof-of-work validation live |
| **Phase 3** | Intelligence & Memory | 4-6 weeks | Personalization & NLP filtering | Recruiter-adaptive system |
| **Phase 4** | Compliance & Enterprise | 4-6 weeks | Bias audits, integrations | Enterprise-ready product |
| **Phase 5** | Scale & Automation | Ongoing | Outreach, analytics, team features | Full platform maturity |

---

## Phase 1: Foundation & Core Screening (MVP)

**Goal:** Launch a working product that screens resumes with explainable AI reasoning.

**Duration:** 6-8 weeks

### 1.1 Authentication & User Management

| Feature | Priority | Description |
|---------|----------|-------------|
| Email/Password Authentication | P0 | Secure signup/login with email verification |
| OAuth (Google/GitHub) | P1 | One-click signup for faster onboarding |
| User Profile Management | P0 | Basic profile with company info and preferences |
| Workspace/Team Setup | P1 | Create workspace, invite team members |

### 1.2 Job Description Management

| Feature | Priority | Description |
|---------|----------|-------------|
| JD Creation | P0 | Create job descriptions with title, requirements, nice-to-haves |
| JD Import | P1 | Paste existing JD and auto-extract requirements |
| Skills Extraction | P0 | AI extracts required skills, experience levels from JD |
| JD Templates | P2 | Pre-built templates for common technical roles |

### 1.3 Resume Ingestion

| Feature | Priority | Description |
|---------|----------|-------------|
| PDF Upload (Single) | P0 | Upload individual resume PDF |
| Bulk Upload | P0 | Drag-and-drop up to 100 PDFs at once |
| Resume Parsing | P0 | Extract structured data: contact, experience, skills, education |
| Duplicate Detection | P1 | Identify and flag duplicate candidates |
| Progress Tracking | P0 | Real-time progress bar during bulk processing |

### 1.4 Semantic Skill Analysis

| Feature | Priority | Description |
|---------|----------|-------------|
| Concept Extraction | P0 | Extract skills as concepts, not keywords (e.g., "IaC" = "Terraform") |
| Skill Graph Mapping | P0 | Map related skills (e.g., "Distributed Systems" implies "Scalability") |
| Experience Level Inference | P0 | Infer Junior/Mid/Senior from context, not just titles |
| Technology Stack Detection | P0 | Identify primary tech stack and frameworks |

### 1.5 Explainable AI Scoring (XAI) ⭐ Core Differentiator

| Feature | Priority | Description |
|---------|----------|-------------|
| Match Score (0-100) | P0 | Overall fit score for JD-candidate match |
| Reasoning Report | P0 | 3-section analysis: Strengths, Gaps, Red Flags |
| Citation Links | P0 | Every claim linked to specific resume sentence |
| Suggested Interview Questions | P1 | AI-generated questions based on gaps/red flags |
| Confidence Indicator | P1 | Show AI confidence level for each assessment |

### 1.6 Candidate Dashboard

| Feature | Priority | Description |
|---------|----------|-------------|
| Ranked Candidate List | P0 | Sortable list ranked by match score |
| Filter & Search | P0 | Filter by skills, experience, score range |
| Candidate Detail View | P0 | Full analysis with reasoning and citations |
| Bulk Actions | P1 | Multi-select for shortlist, reject, export |
| Status Tracking | P1 | Pipeline stages: New, Reviewed, Shortlisted, Rejected |

### 1.7 Basic Onboarding

| Feature | Priority | Description |
|---------|----------|-------------|
| Welcome Flow | P0 | Guided first-time experience |
| Sample JD + Resumes | P1 | Pre-loaded demo data to show product value |
| Quick Start Guide | P0 | Contextual tooltips and help |

---

## Phase 2: Verification Engine ⭐ Key Differentiator

**Goal:** Verify candidate claims against real-world proof-of-work.

**Duration:** 4-6 weeks

### 2.1 GitHub Verification Agent

| Feature | Priority | Description |
|---------|----------|-------------|
| GitHub URL Extraction | P0 | Auto-extract GitHub URL from resume |
| Repository Analysis | P0 | Analyze recent repos: languages, commit frequency, code quality |
| Contribution Assessment | P0 | Evaluate contribution patterns and consistency |
| Skill Verification | P0 | Cross-reference claimed skills with actual code |
| Seniority Validation | P0 | Check if code complexity matches claimed seniority |
| Discrepancy Flagging | P0 | Flag mismatches between resume claims and GitHub reality |

### 2.2 LinkedIn Cross-Reference

| Feature | Priority | Description |
|---------|----------|-------------|
| LinkedIn URL Extraction | P0 | Extract LinkedIn URL from resume |
| Employment Verification | P1 | Validate job titles and dates against resume |
| Tenure Analysis | P1 | Analyze job-hopping patterns and career trajectory |
| Discrepancy Reports | P1 | Flag inconsistencies between resume and LinkedIn |

### 2.3 Verification Status Dashboard

| Feature | Priority | Description |
|---------|----------|-------------|
| Verification Status Indicator | P0 | Show: Pending, Verified, Discrepancy Found |
| Verification Details | P0 | Detailed breakdown of what was checked |
| Combined Score Adjustment | P0 | Adjust match score based on verification results |
| Verification History | P1 | Log of all verification checks performed |

### 2.4 Blind Recruitment Mode

| Feature | Priority | Description |
|---------|----------|-------------|
| Anonymization Toggle | P0 | One-click removal of name, gender, age, photo |
| School Name Removal | P1 | Option to hide educational institution names |
| Bias-Free Ranking | P0 | Rank purely on skills and experience |
| De-anonymization Control | P1 | Reveal identity only after shortlisting |

---

## Phase 3: Intelligence & Memory

**Goal:** Make the system learn and adapt to each recruiter's preferences.

**Duration:** 4-6 weeks

### 3.1 Recruiter Memory System

| Feature | Priority | Description |
|---------|----------|-------------|
| Feedback Loop | P0 | Capture recruiter decisions (accept/reject) and reasons |
| Preference Learning | P0 | Learn what "Senior" means to this specific recruiter |
| Historical Pattern Analysis | P1 | Analyze past hiring decisions to improve future recommendations |
| Preference Profile | P1 | Editable profile showing learned preferences |

### 3.2 Natural Language Filtering (Chat Interface)

| Feature | Priority | Description |
|---------|----------|-------------|
| Chat-Based Search | P0 | "Find me candidates with Python and startup experience" |
| Complex Queries | P0 | "Show top 5 who are like [Employee X] but more senior" |
| Contextual Follow-ups | P1 | "Now filter those to only remote-friendly" |
| Query Suggestions | P1 | AI-suggested queries based on JD |

### 3.3 Smart Recommendations

| Feature | Priority | Description |
|---------|----------|-------------|
| Similar Candidate Suggestions | P0 | "Candidates similar to [Shortlisted Person]" |
| Re-discovery | P1 | Surface past candidates who match new roles |
| Talent Pool Alerts | P2 | Notify when new candidates match saved searches |

### 3.4 Advanced Soft Skill Analysis

| Feature | Priority | Description |
|---------|----------|-------------|
| Career Trajectory Analysis | P1 | Analyze promotion frequency and growth patterns |
| Stability Indicators | P1 | Predict likelihood of long-term retention |
| Communication Style Inference | P2 | Infer communication patterns from writing samples |

---

## Phase 4: Compliance & Enterprise

**Goal:** Make the product enterprise-ready with compliance features and integrations.

**Duration:** 4-6 weeks

### 4.1 Bias Audit & Compliance Module

| Feature | Priority | Description |
|---------|----------|-------------|
| NYC LL144 Compliance Report | P0 | Generate annual bias audit report meeting NYC requirements |
| Demographic Impact Analysis | P0 | Four-fifths rule analysis across protected groups |
| EEOC Compliance Dashboard | P1 | Track and report on fair hiring metrics |
| Audit Trail | P0 | Complete log of all AI decisions for legal review |
| Exportable Compliance Reports | P0 | PDF/CSV exports for legal and HR teams |

### 4.2 ATS Integrations

| Feature | Priority | Description |
|---------|----------|-------------|
| Greenhouse Integration | P0 | Two-way sync with Greenhouse ATS |
| Workday Integration | P1 | Connect with Workday Recruiting |
| Lever Integration | P2 | Sync with Lever ATS |
| Generic Webhook API | P1 | Allow custom integrations via webhooks |

### 4.3 Team & Access Management

| Feature | Priority | Description |
|---------|----------|-------------|
| Role-Based Access Control | P0 | Admin, Recruiter, Hiring Manager roles |
| SSO Integration | P0 | SAML/OAuth SSO for enterprise clients |
| Team Analytics | P1 | View team-wide screening metrics |
| Audit Logs | P0 | Track all user actions for compliance |

### 4.4 Billing & Subscription

| Feature | Priority | Description |
|---------|----------|-------------|
| Stripe Integration | P0 | Subscription billing via Stripe |
| Usage-Based Pricing | P1 | Track and bill by screening volume |
| Plan Management | P0 | Self-service plan upgrades/downgrades |
| Invoice Generation | P1 | Automated invoicing for enterprise |

---

## Phase 5: Scale & Automation

**Goal:** Add productivity features and scale the platform.

**Duration:** Ongoing

### 5.1 Automated Outreach

| Feature | Priority | Description |
|---------|----------|-------------|
| Email Template Builder | P1 | Create personalized outreach templates |
| AI-Personalized Emails | P1 | Auto-generate personalized emails per candidate |
| Email Scheduling | P2 | Schedule outreach campaigns |
| Response Tracking | P2 | Track email opens, responses, and engagement |

### 5.2 Analytics & Reporting

| Feature | Priority | Description |
|---------|----------|-------------|
| Screening Funnel Analytics | P1 | Visualize candidate flow through stages |
| Time-to-Hire Metrics | P1 | Track efficiency improvements |
| Quality of Hire Tracking | P2 | Long-term tracking of hired candidate performance |
| Custom Report Builder | P2 | Build custom reports for stakeholders |

### 5.3 Advanced Features

| Feature | Priority | Description |
|---------|----------|-------------|
| Portfolio/Website Analysis | P2 | Verify skills from personal websites/portfolios |
| Video Introduction Screening | P2 | AI analysis of candidate video intros |
| Interview Scheduling Integration | P2 | Connect with Calendly/Google Calendar |
| Mobile App (iOS/Android) | P2 | Review candidates on the go |

---

## Technical Architecture Overview

> [!NOTE]
> This section provides high-level architecture guidance without implementation details.

### Core Components

| Component | Purpose | Key Requirements |
|-----------|---------|-----------------|
| **Frontend** | User interface | Fast, responsive, real-time updates |
| **API Layer** | Business logic | RESTful, rate-limited, authenticated |
| **Agent Orchestrator** | Manage AI workflows | Queue-based, resumable, observable |
| **LLM Service** | AI reasoning | Low latency, cost-optimized, fallback support |
| **Verification Agents** | GitHub/LinkedIn checks | Rate-limit aware, cached, retry logic |
| **Database** | Data persistence | Relational + vector search support |
| **File Storage** | Resume PDFs | Secure, encrypted, versioned |

### Scalability Requirements

| Metric | Phase 1 Target | Phase 4 Target |
|--------|---------------|----------------|
| Concurrent Users | 100 | 10,000 |
| Resumes/day | 1,000 | 100,000 |
| API Response Time | <500ms | <200ms |
| Agent Processing | <30s per resume | <10s per resume |

### Security Requirements

| Requirement | Priority | Description |
|-------------|----------|-------------|
| Data Encryption | P0 | Encrypt all data at rest and in transit |
| SOC 2 Compliance | P1 | Achieve SOC 2 Type II by Phase 4 |
| GDPR Compliance | P0 | Data deletion, portability, consent management |
| Penetration Testing | P1 | Quarterly third-party security audits |

---

## Pricing Tiers (Proposed)

| Tier | Monthly Price | Target User | Included |
|------|--------------|-------------|----------|
| **Free** | $0 | Individual exploring | 10 screenings/mo, basic XAI |
| **Starter** | $99/mo | Solo recruiter | 50 screenings/mo, GitHub verification |
| **Professional** | $199/mo | Small teams | 200 screenings/mo, memory, integrations |
| **Team** | $399/mo | Growing teams | 500 screenings/mo, compliance reports |
| **Enterprise** | Custom | Large orgs | Unlimited, SSO, dedicated support |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|-----------|
| GitHub API Rate Limits | Medium | High | Aggressive caching, GitHub API paid tier |
| LinkedIn Blocking Scraping | High | Medium | Require user-provided URLs, use official APIs |
| LLM Hallucination | Medium | High | Grounded generation with citations, confidence scores |
| Regulatory Changes | Medium | High | Build compliance-first, monitor legislation |
| Competitor Response | Medium | Medium | Move fast, focus on XAI + verification moat |

---

## Appendix: Feature Priority Legend

| Priority | Meaning | Commitment |
|----------|---------|-----------|
| **P0** | Must have | Required for phase launch |
| **P1** | Should have | High value, include if possible |
| **P2** | Nice to have | Schedule for future iteration |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 2026 | — | Initial PRD based on market research |
