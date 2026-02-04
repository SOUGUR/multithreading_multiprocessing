Cell Analytics Engine – Multithreading vs Multiprocessing
This project is a small FastAPI-based benchmark service that compares single-threaded, multithreaded, and multiprocess processing of a large CSV dataset (data/cells.csv). It exposes simple HTTP endpoints that trigger different execution modes and return timing, CPU usage, and result statistics so you can observe the impact of multithreading and multiprocessing on a realistic data-processing workload.
​

Features
FastAPI service exposing a clean HTTP API for benchmarking.
​

Three execution modes:

Single process (no concurrency).
​

Multithreading.
​

Multiprocessing.
​

Reads and processes cells.csv in configurable chunk sizes.
​

Returns:

Total rows processed.

Execution time in seconds.

CPU usage percentage.

A checksum of processed rows.

A tabular summary of the run (converted to a JSON-serializable dict).
​

Convenience endpoint to fetch a sample of processed rows.
​

Project Structure
text
multithreading_multiprocessing/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entrypoint
│   ├── api.py           # API routes (endpoints)
│   ├── services/        # Execution + benchmarking logic (single/thread/process)
│   └── utils/           # Helper utilities
├── data/
│   └── cells.csv        # Input dataset used for benchmarks
├── results/
│   └── output.json      # Example output / saved benchmark results
└── requirements.txt
Note: app/services contains the core logic (executor, benchmark etc.), which are imported in the API layer.
​

Installation
Clone the repository:

bash
git clone https://github.com/SOUGUR/multithreading_multiprocessing.git
cd multithreading_multiprocessing
(Optional) Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows
Install dependencies (once requirements.txt is populated):

bash
pip install -r requirements.txt
​

Running the API
From the project root, run the FastAPI app using Uvicorn:

bash
uvicorn app.main:app --reload
The service will start at http://127.0.0.1:8000 by default.
​

Interactive API docs (Swagger UI) will be available at http://127.0.0.1:8000/docs.
​

app.main creates the FastAPI instance and includes the API router defined in app.api under the default root path.
​

API Endpoints
1. POST /benchmark
Runs the benchmark in the requested mode and returns execution statistics.
​

Query parameters

mode (required): one of:

"single" – single-process, no concurrency.

"thread" – multithreading.

"process" – multiprocessing.
​

chunksize (optional, default: 5000): number of rows per chunk when reading/processing data/cells.csv.
​

Example request

bash
curl -X POST "http://127.0.0.1:8000/benchmark?mode=thread&chunksize=5000"
Response (JSON)

json
{
  "mode": "thread",
  "rows_processed": 250000,
  "time_seconds": 1.42,
  "cpu_percent": 87.5,
  "checksum": "e3b0c44298...",
  "summary": {
    "...": "pandas summary or custom stats as a dict"
  }
}
Response fields

mode: execution mode requested (single, thread, or process).
​

rows_processed: total number of rows processed across all chunks.
​

time_seconds: time taken to complete the run.
​

cpu_percent: CPU utilization during the run (as computed in benchmark_execution).
​

checksum: a checksum over the processed rows, computed by checksum_rows, useful to verify consistency across modes.
​

summary: a serialized summary (e.g. pandas DataFrame .to_dict()) of the results.
​

Internally:

The endpoint always reads from data/cells.csv.
​

It dispatches to:

run_single for mode="single".

run_threaded for mode="thread".

run_processes for mode="process".

All of these are wrapped by benchmark_execution, which measures time, CPU, and collects row data.
​

2. POST /rows
Returns a small sample of processed rows using the multiprocessing mode.
​

Query parameters

limit (optional, default: 20): maximum number of rows to return.
​

Example request

bash
curl -X POST "http://127.0.0.1:8000/rows?limit=10"
Response (JSON)

json
[
  {
    "col1": "value",
    "col2": 123,
    "...": "..."
  },
  {
    "col1": "value2",
    "col2": 456
  }
]
This endpoint:

Runs run_processes("data/cells.csv", chunksize=5000) to process the CSV in multiprocessing mode.
​

Takes the resulting DataFrame, applies .head(limit), and returns it as a list of dicts via .to_dict(orient="records").
​

Usage Notes
data/cells.csv must exist and be reasonably large to see meaningful differences between single, threaded, and process-based execution.
​

results/output.json can be used as an example storage file for persisting benchmark results, dashboards, or offline analysis.
​

You can wrap these endpoints in a UI (e.g. simple React dashboard) to visualize time vs CPU across different modes and chunk sizes.

Local Development
Add Pydantic response models in app/schemas.py to enforce and document response schemas for /benchmark and /rows.
​

Extend app/services with:

Additional metrics (memory, I/O wait, per-core CPU).

Different workloads (e.g., CPU-bound transforms vs I/O-bound operations).
​

Integrate proper logging to compare runs over time and environments.
