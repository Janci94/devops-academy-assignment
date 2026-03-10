# 🚀 Cloud & DevOps Project Portfolio

Welcome to the root of this project. This repository is structured into three specialized sections, each addressing a core pillar of modern DevOps: **Infrastructure as Code (IaC)**, **CI/CD Optimization**, and **Production Incident Management**.

---

## 📂 Project Structure

This repository acts as a monorepo where each directory contains its own source code and dedicated documentation.

### 🏗️ [Task A: Terraform-managed AWS VPC](./section-1/task-a/)
This section focuses on **Infrastructure as Code (IaC)** to build a secure and scalable AWS networking environment.
* **Goal:** Deploy a multi-AZ VPC with isolated public and private tiers.
* **Key Tech:** Terraform, AWS VPC Modules, NAT Gateways.
* **Highlights:** Cost-optimized NAT configuration and modular resource management.
* **Documentation:** [Go to Task A README](./section-1/task-a/README.md)

### 🐳 [Task B: CI/CD & Docker Storage Optimization](./section-2/task-c)
A technical deep-dive into resolving pipeline bottlenecks related to storage and build efficiency.
* **Goal:** Fix `no space left on device` errors and optimize Docker image sizes.
* **Key Tech:** Docker, Alpine Linux, Layer Caching, BuildKit.
* **Highlights:** Migration to lightweight base images and automated cache pruning.
* **Documentation:** [Go to Task B README](./section-2/task-c/README.md)

### 🧠 [Section 3: Production Incident Response](./section-3/task-a/)
A strategic framework for Site Reliability Engineering (SRE) and production support operations.
* **Goal:** Establish a systematic approach to investigating and resolving production outages.
* **Key Concepts:** Golden Signals, Triage, Rollback Strategies, and Post-Mortem Analysis.
* **Highlights:** A step-by-step investigation guide from "Alert" to "Resolution."
* **Documentation:** [Go to Section 3 README](./section-3/task-a/README.md)
