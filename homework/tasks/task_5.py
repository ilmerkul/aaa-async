import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine,
                               max_execution_time: float) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить, однако иногда она выполняется
    # слишком долго, это время необходимо ограничить переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена, и все они завершились за заданное
    # время.

    try:
        wait = asyncio.wait_for(coro, timeout=max_execution_time)
        await wait
    except asyncio.TimeoutError:
        pass


async def limit_execution_time_many(*coros: Coroutine,
                                    max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time, но корутин на вход приходит несколько.
    await asyncio.gather(*[limit_execution_time(coro, max_execution_time)
                           for coro in coros])
