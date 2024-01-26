import time

import anyio
from asyncer import asyncify


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


async def print_message():
    message = await asyncify(do_sync_work)(name="World")
    print(message)


anyio.run(print_message)
