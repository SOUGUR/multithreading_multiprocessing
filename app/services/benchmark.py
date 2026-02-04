import time
import psutil
from typing import Callable, Any, Tuple

def checksum_rows(df):
    return float(df.drop(columns=["CellId"]).sum().sum())


def benchmark_execution(fn: Callable[..., Tuple[Any, Any]], *args, **kwargs):
    """
    Benchmarks execution time and CPU usage for a computation function.
    The function must return (rows_df, summary_df).
    """

    # Reset CPU stats
    psutil.cpu_percent(interval=None)

    start = time.perf_counter()
    rows, summary = fn(*args, **kwargs)
    elapsed = time.perf_counter() - start

    cpu_used = psutil.cpu_percent(interval=None)

    return {
        "rows": rows,
        "summary": summary,
        "time_seconds": round(elapsed, 3),
        "cpu_percent": cpu_used
    }
