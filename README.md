# Cell Analytics Engine: Multithreading vs. Multiprocessing Benchmark

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional performance benchmarking suite built with **FastAPI** to demonstrate and compare different execution models in Python. This project provides a hands-on laboratory for observing how **Multithreading** and **Multiprocessing** impact CPU-intensive data processing tasks.

## 🚀 Project Overview

The **Cell Analytics Engine** is designed to process large-scale biological cell datasets (CSV format) and perform complex geometric and volumetric computations. By exposing these operations through a REST API, the project allows developers and researchers to trigger benchmarks and analyze real-time metrics including execution time, CPU utilization, and data integrity.

### Core Objectives
- **Demonstrate Concurrency**: Practical implementation of `concurrent.futures` for parallel execution.
- **Performance Benchmarking**: Comparative analysis of Single-threaded vs. Multi-threaded vs. Multi-processed workloads.
- **Data Processing**: Efficient handling of large CSV files using `pandas` and `numpy`.
- **API-First Design**: Easy-to-use endpoints for triggering benchmarks and retrieving results.

---

## 🧠 Multithreading vs. Multiprocessing

This repository highlights the critical differences between the two primary concurrency models in Python:

| Feature | **Multithreading** | **Multiprocessing** |
|:---|:---|:---|
| **Mechanism** | Multiple threads within a single process. | Multiple independent processes. |
| **Memory** | Shared memory space between threads. | Separate memory space for each process. |
| **GIL Impact** | Limited by the Global Interpreter Lock (GIL). | Bypasses the GIL by using separate interpreters. |
| **Best For** | I/O-bound tasks (API calls, DB queries). | CPU-bound tasks (heavy math, image processing). |
| **Overhead** | Low (fast thread creation). | High (process creation and IPC overhead). |

> **Note:** In this project, you will observe that **Multiprocessing** typically outperforms Multithreading for the mathematical computations performed on the cell data, as it utilizes multiple CPU cores simultaneously.

---

## 🛠️ Technologies Used

- **Language:** Python 3.10+
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous Web API)
- **Data Science:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Concurrency:** `concurrent.futures` (ThreadPoolExecutor & ProcessPoolExecutor)
- **Monitoring:** `psutil` (for CPU tracking)
- **Web Server:** [Uvicorn](https://www.uvicorn.org/)

---

## 📂 Project Structure

```text
multithreading_multiprocessing/
├── app/
│   ├── main.py          # FastAPI application entrypoint
│   ├── api.py           # REST API route definitions
│   ├── services/        # Core business logic
│   │   ├── compute.py   # Mathematical & analytical functions
│   │   ├── executor.py  # Concurrency implementation logic
│   │   └── benchmark.py # Performance measurement utilities
│   └── utils/           # Data loading and helper utilities
├── data/
│   └── cells.csv        # Source dataset for analysis
├── results/
│   └── output.json      # Sample benchmark results
└── requirements.txt     # Project dependencies
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SOUGUR/multithreading_multiprocessing.git
   cd multithreading_multiprocessing
   ```

2. **Environment Setup** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃 Running the Project

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

- **API Documentation**: Access the interactive Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Base URL**: `http://127.0.0.1:8000`

---

## 📊 API Endpoints & Usage

### 1. Run Performance Benchmark
`POST /benchmark`

Executes the analytical workload using the specified mode.

**Parameters:**
- `mode` (Required): `single`, `thread`, or `process`.
- `chunksize` (Optional): Number of rows to process per batch (default: 5000).

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/benchmark?mode=process&chunksize=10000"
```

### 2. Retrieve Processed Data
`POST /rows`

Returns a preview of the processed cell data.

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/rows?limit=5"
```

---

## 📝 Example Output Explanation

When running a benchmark, the API returns a detailed JSON response:

```json
{
  "mode": "process",
  "rows_processed": 250000,
  "time_seconds": 0.85,
  "cpu_percent": 92.4,
  "checksum": "a1b2c3d4...",
  "summary": { ... }
}
```

- **time_seconds**: Total duration. Compare this across modes to see efficiency gains.
- **cpu_percent**: Average CPU load. Multiprocessing will show significantly higher utilization on multi-core systems.
- **checksum**: Ensures data integrity; the value should be identical across all execution modes.

---

## 👨‍💻 Author
**SOUGUR**
- GitHub: [@SOUGUR](https://github.com/SOUGUR)

---
*Developed for educational purposes to showcase advanced Python concurrency patterns.*
