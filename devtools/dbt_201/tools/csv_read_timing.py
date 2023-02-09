from functools import wraps
from time import time

import pandas as pd

DATA_FILE = "target/People_data.csv"
OUT_DATA_FILE = "target/People_data_PD1.parquet"


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te - ts))
        return result

    return wrap


@timing
def _parquet_read():
    df = pd.read_parquet(OUT_DATA_FILE)
    print(f'Read Back: {df.shape}')
    print(df)


def main():
    # _csv_to_parquet_plain_pandas()
    _parquet_read()


@timing
def _csv_to_parquet_plain_pandas():
    df = pd.read_csv(DATA_FILE)
    df.to_parquet(OUT_DATA_FILE, compression=None)
    print(f"df: {df.shape}")


@timing
def _csv_to_parquet_plain_pandas_pyarrow():
    df = pd.read_csv(DATA_FILE, engine="pyarrow")
    df.to_parquet(OUT_DATA_FILE, compression=None)
    print(f"df: {df.shape}")


if __name__ == '__main__':
    main()
