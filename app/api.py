from fastapi import APIRouter, Query
from app.services.executor import (
    run_single,
    run_threaded,
    run_processes
)
from app.services.benchmark import benchmark_execution, checksum_rows

router = APIRouter()

@router.post("/benchmark")
def benchmark(
    mode: str = Query(..., enum=["single", "thread", "process"]),
    chunksize: int = 5000
):
    csv_path = "data/cells.csv"

    if mode == "single":
        stats = benchmark_execution(run_single, csv_path, chunksize)
    elif mode == "thread":
        stats = benchmark_execution(run_threaded, csv_path, chunksize)
    else:
        stats = benchmark_execution(run_processes, csv_path, chunksize)

    return {
        "mode": mode,
        "rows_processed": len(stats["rows"]),
        "time_seconds": stats["time_seconds"],
        "cpu_percent": stats["cpu_percent"],
        "checksum": checksum_rows(stats["rows"]),
        "summary": stats["summary"].to_dict()
    }



@router.post("/rows")
def rows(limit: int = 20):
    rows, _ = run_processes("data/cells.csv", chunksize=5000)
    return rows.head(limit).to_dict(orient="records")


