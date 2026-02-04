import pandas as pd
from typing import Iterator

def load_csv_in_chunks(
    csv_path: str,
    chunksize: int = 5000
) -> Iterator[pd.DataFrame]:
    """
    Lazily load CSV data in chunks.
    This simulates large-file processing.
    """
    return pd.read_csv(csv_path, chunksize=chunksize)
