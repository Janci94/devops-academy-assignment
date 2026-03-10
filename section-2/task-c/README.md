# CI/CD Infrastructure Optimization: Docker Storage Management

## 📌 Issue Overview
The CI/CD pipeline encountered a critical failure with the error `no space left on device` during the Docker build process. This blocked all subsequent deployments and required immediate intervention.

## 🔍 Root Cause Diagnosis
The disk exhaustion was caused by three primary factors:
1. **Unoptimized Base Images:** Using a heavy OS distribution (Ubuntu) led to large image footprints.
2. **Docker Object Accumulation:** The CI runner was saturated with "dangling" images (untagged layers) and obsolete containers from previous build cycles.
3. **BuildKit Cache Bloat:** The Docker build cache grew indefinitely without a retention policy, eventually consuming all available storage on the runner.

---

## 🛠️ Implemented Solutions

### 1. Dockerfile Optimization
* **Lightweight Foundation:** Migrated the application from a heavy Ubuntu-based image to a minimal Alpine Linux distribution, significantly reducing storage requirements.
* **Layer Efficiency:** Reordered instructions to maximize Docker’s layer caching. By separating dependency installation from source code copying, we ensure that heavy layers are only rebuilt when dependencies change.
* **Cache Cleanup:** Integrated commands to purge package manager caches immediately after installation within the same build layer.

### 2. CI/CD Pipeline Enhancements
* **Targeted Triggers:** Implemented path-based filtering to ensure the build process only initiates when changes occur in the specific project directory.
* **Pre-emptive Space Recovery:** Added a cleanup stage for GitHub-hosted runners to remove unnecessary pre-installed SDKs and tools that are not required for this project.
* **Automated Pruning:** Integrated a post-build maintenance step that automatically removes unused Docker objects and build cache older than 24 hours.

---

## 📈 Monitoring & Prevention Measures

To ensure the long-term health of the CI environment, the following measures have been established:

* **Retention Policy:** A 24-hour retention window for build artifacts ensures a balance between build speed (reusing recent cache) and storage availability.
* **Disk Usage Visibility:** The pipeline now outputs disk usage statistics (`df -h`) before and after the build process for easier auditing and troubleshooting.
* **Build Context Control:** Explicitly defined build contexts to prevent unnecessary large files from being sent to the Docker daemon.

---

## 🚀 Local Maintenance
Developers can maintain their local environments using the same logic by running filtered prune commands to remove only stale data while preserving active development caches.