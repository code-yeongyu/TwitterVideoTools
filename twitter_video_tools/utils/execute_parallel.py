import multiprocessing
import multiprocessing.dummy
from typing import Any, Callable


def execute_parallel(func: Callable[[str], None], *args: Any, **kwargs: Any) -> None:
    pool = multiprocessing.dummy.Pool(multiprocessing.cpu_count())
    pool.starmap(func, *args, **kwargs)
