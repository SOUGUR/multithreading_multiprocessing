import pandas as pd
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from app.utils.data_loader import load_csv_in_chunks
from app.services.compute import compute_row_metrics, aggregate_metrics


def run_single(csv_path: str, chunksize: int):
    frames = []
    for chunk in load_csv_in_chunks(csv_path, chunksize):
        frames.append(compute_row_metrics(chunk))

    rows = pd.concat(frames)
    summary = aggregate_metrics(rows)
    return rows, summary


def run_threaded(csv_path: str, chunksize: int, workers: int = 4):
    chunks = list(load_csv_in_chunks(csv_path, chunksize))

    with ThreadPoolExecutor(max_workers=workers) as executor:
        frames = list(executor.map(compute_row_metrics, chunks))

    rows = pd.concat(frames)
    summary = aggregate_metrics(rows)
    return rows, summary


def run_processes(csv_path: str, chunksize: int, workers: int = None):
    chunks = list(load_csv_in_chunks(csv_path, chunksize))

    with ProcessPoolExecutor(max_workers=workers) as executor:
        frames = list(executor.map(compute_row_metrics, chunks))

    rows = pd.concat(frames)
    summary = aggregate_metrics(rows)
    return rows, summary
