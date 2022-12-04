import multiprocessing.dummy
from multiprocessing import cpu_count as get_cpu_count
from typing import Any, Callable


def execute_parallel(func: Callable[[str], None], *args: Any, **kwargs: Any) -> None:
    pool = multiprocessing.dummy.Pool(get_cpu_count())
    pool.starmap(func, *args, **kwargs)
