import time
from contextlib import contextmanager

@contextmanager
def timed():
    time_begin = time.monotonic()
    yield
    time_elapsed = time.monotonic() - time_begin
    print(f"{time_elapsed:.2f} seconds elapsed")
