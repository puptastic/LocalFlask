import asyncio as an
import pandas as pd
import random as rd

async def fetch_data(source: str) -> pd.DataFrame:
    """
    :param source_one: file or url location of source
    :return: DataFrame
    """
    raise NotImplementedError


async def coalesce_data(source_one: str, source_two: str, unite_field: str) -> pd.DataFrame:
    """
    Method that fetches two sets of JSON data into a single dataframe
    :param source_one: file or url location of first source
    :param source_two: file or url location of second source
    "unite_field": field that allows a join
    :return: DataFrame
    """
    raise NotImplementedError


async def basic_async(delay: int, additive: int) -> int:
    print(f"Starting async call with delay {delay}")
    await an.sleep(delay)  # Simulate other operation
    print(f"Finished async call with delay {delay}")
    return rd.randint(1, 6) + additive


async def main():
    task1 = an.create_task(basic_async(delay=rd.randint(2, 5), additive=4))
    task2 = an.create_task(basic_async(delay=rd.randint(2, 5), additive=3))

    result1 = await task1
    result2 = await task2

    print(result1 + result2)


if __name__ == '__main__':
    an.run(main())