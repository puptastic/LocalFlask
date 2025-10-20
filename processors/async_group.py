import asyncio as an
import pandas as pd
from pandasql import sqldf
import random as rd
from essential_functions import timing

@timing
async def fetch_data(source: str) -> pd.DataFrame:
    """
    :param source_one: file or url location of source
    :return: DataFrame
    """
    try:
        if "https://" in source:
            raise NotImplementedError
        else:
            df = pd.read_csv(source)

        return df
    except Exception as e:
        print(f"The following error occurred: {e}")


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

@timing
async def main():
    task1 = an.create_task(basic_async(delay=rd.randint(2, 5), additive=4))
    task2 = an.create_task(basic_async(delay=rd.randint(2, 5), additive=3))

    result1 = await task1
    result2 = await task2

    print(result1 + result2)

@timing
async def main2():
    task1 = an.create_task(fetch_data("../local_data/Bri_Pay.csv"))

    df = await task1

    df = df.rename(columns={'$/Hours': 'Hourly_Wage', 'Day of week': 'Day_of_Week'})  # Renaming trouble columns
    df['Day_of_Week'] = df['Day_of_Week'].str.strip()
    #print(df.to_string())  # "to_string()" to print entirety in console

    q1 = df['Hourly_Wage'].quantile(0.25)
    q3 = df['Hourly_Wage'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Omitting outliers
    query = f"""
    SELECT Club, Type, AVG(Hourly_Wage) as 'Average', COUNT(Club) as 'Visits' 
    FROM df
    WHERE Hourly_Wage >= {lower_bound} AND Hourly_Wage <= {upper_bound}
    GROUP BY Club
    ORDER BY Average DESC
    """

    query2 = f"""
    SELECT Day_of_Week, AVG(Hourly_Wage) as 'Average', COUNT(Club) as 'Visits' 
    FROM df
    WHERE Hourly_Wage >= {lower_bound} AND Hourly_Wage <= {upper_bound}
    GROUP BY Day_of_Week
    ORDER BY Average DESC
    
    
    """

    result_df = sqldf(query)
    mean = result_df['Average'].mean()
    std = result_df['Average'].std()
    median = result_df['Average'].median()
    print(result_df.to_string())
    print(f"\nData insights on $/Hour: mean={mean:.2f}, std={std:.2f}, median={median:.2f}")

    result_df2 = sqldf(query2)
    print(f"\n{result_df2.to_string()}")

if __name__ == '__main__':
    an.run(main2())