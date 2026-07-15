# Log Report Analysis & Verification Agent

## 📌 Project Overview
This project is a containerized log analysis tool designed to process server access logs. It uses a Python-based environment to run automated verification tests. The project was built and executed using the Harbor agent framework to ensure secure and reproducible results.

## 🛠️ Technical Troubleshooting (The Docker Fix)
A major part of this project involved ensuring the integrity of the build environment. 

*   **The Problem:** The initial build failed with an `invalid checksum digest length` exception. This was caused by an extra character in the SHA256 digest string in the Dockerfile (65 characters instead of the required 64).
*   **The Solution:** I used `docker inspect` to pull the exact repository digest from the machine and piped it directly to the clipboard. This eliminated manual transcription errors and successfully fixed the build.
*   **Security:** The Dockerfile was further optimized to run as a non-root `agent` user to follow security best practices.

## 📂 Understanding the Results (The "Jobs" Folder)
The output of every run is stored in the `jobs/` directory, organized by unique timestamps.

### 📍 Which one is the "Original"?
Because this project involved multiple iterations and testing phases:
1.  **The Final Output:** The folder with the **latest (most recent) timestamp** is the official and final verified output of this project.
2.  **Practice History:** All other timestamped folders represent my **practice runs, debugging, and checked versions** created while perfecting the environment and fixing the Docker configuration.

### 📄 Output Components
Inside each job folder (e.g., `jobs/2024-07-15_19-45-00/`), you will find:
- `result.json`: The final validation status.
- `verifier/ctrf.json`: The structured test results in CTRF format.
- `verifier/test-stdout.txt`: The full execution logs from the Python testing suite.

## 🚀 How to Execute
To build the environment and trigger a new verification job:

1. **Build the Docker Image:**
   ```cmd
   docker build -t log-report .
