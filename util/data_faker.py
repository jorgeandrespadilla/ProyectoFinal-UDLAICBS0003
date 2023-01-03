import csv
from datetime import datetime
from faker import Faker
import pandas as pd
import random
import re
from typing import Callable, Union

fake = Faker(['es_CO', 'es_MX'])
date_format = "%Y-%m-%d"


def random_choice(data: dict) -> str:
    """
    Chooses a random element from a dictionary, where the key (str) is the element and the value (int) is the weight.

    Returns
    -------
    String with the chosen element.
    """
    keys = list(data.keys())
    values = list(data.values())
    return random.choices(keys, weights=values)[0]


def generate_phrase(n: int, callback: Callable[[], str], unique=True) -> str:
    """
    Generates a phrase with n words, given a callback to generate words.

    Parameters
    ----------
    n: 
        Number of words.
    callback:
        Callback to generate words. The callback should return a string with the word.
        If the callback returns a string with multiple words, they will be split by spaces.
    unique:
        If the words should be unique.

    Returns
    -------
    String with the phrase
    """
    words = []
    while len(words) < n:
        word = callback()
        word_list = word.split(r'\s+')  # Split by spaces
        for word in word_list:
            if len(words) >= n:
                break
            if unique and word in words:
                continue
            words.append(word)
    return ' '.join(words)


def normalize_str(name: str) -> str:
    """
    Returns a normalized string, removing quotes if they are the first and last characters.

    Parameters
    ----------
    name:
        String to normalize.

    Returns
    -------
    Normalized string.
    """
    quotes = ('"', "'")
    new_name = name.strip()
    if new_name.startswith(quotes) and new_name.endswith(quotes):
        new_name = new_name[1:-1]
    new_name = re.sub(r'\s+', ' ', new_name)  # Remove extra spaces
    return new_name.strip()


def generate_fullname() -> str:
    """
    Generates a full name.
    """
    first_name = normalize_str(fake.first_name())
    last_name = generate_phrase(2, lambda: fake.last_name())
    return f"{first_name} {last_name}"


def generate_code(prefix: str, index: Union[str, int], length: int) -> str:
    """
    Returns a string with the given prefix and index, adding zeros to the left of the index to match the given length.
    """
    return f"{prefix}{str(index).zfill(length)}"


def generate_date(from_str: str, to_str: str) -> str:
    """
    Generates a date between the given dates.
    """
    from_date = datetime.strptime(from_str, date_format)
    to_date = datetime.strptime(to_str, date_format)
    return fake.date_between_dates(from_date, to_date).strftime(date_format)


def add_record(df: pd.DataFrame, record: dict) -> pd.DataFrame:
    """
    Adds a record to a given dataframe.
    """
    df = pd.concat([df, pd.DataFrame.from_records([record])],
                   ignore_index=True)
    return df


def generate_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Generates a CSV file with the given dataframe.
    """
    df.to_csv(file_path, quoting=csv.QUOTE_NONNUMERIC, index=False)
