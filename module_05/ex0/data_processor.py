#! /usr/bin/python3
"""
This modules focuses on the use of abstract base classes (ABCs)

Notes :
Abstract Class : can't be instancianted, raises a TypeError.
Serves as a blueprint
"""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    _Base Abstract Class, used for blueprinting other classes_

    Args:
        ABC (_type_): _Base Abstract Class_
    """

    def __init__(self) -> None:
        """
        Init fuction.
        `self._processed_data` -> Store main parsed data.
        `self._processing_rank` -> Store order in which data has been stored
        """
        super().__init__()
        self._processed_data: list[tuple[int, str]] = []
        self._processing_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        _Abstract Method for validating data_

        Args:
            data (Any): _raw data to parse_

        Returns:
            bool: _returns `True` is matches format, `False` otherwise_
        """

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """
        _Abstract Method for ingesting data_

        Args:
            data (Any): _raw data to save_
        """

    # No need to override this method
    def output(self) -> tuple[int, str]:
        """
        Pop the tuple at index `[0]` from `self._processed_data`, and return it

        Returns:
            tuple[int, str]: _self._processed_data.pop(0)_
        """
        return self._processed_data.pop(0)


class NumericProcessor(DataProcessor):
    """
    _Child class of `DataProcessor`, used for parsing and saving
    numeric data_

    Args:
        DataProcessor (_type_): _Base Abstract Class `DataProcessor_
    """

    # ! Note : No need of __init__ method
    def validate(self, data: Any) -> bool:
        """
        Parse if `data` is of type `int`, `float`, `list[int]`, `list[float]`
        or `list[int | float]`

        Args:
            data (Any): _raw data to parse_

        Returns:
            bool: _returns `True` is matches format, `False` otherwise_
        """
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            # Check the whole list first
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            # From here, the data is valid
            return True
        return False  # any other type is false

    def ingest(
        self, data: int | float | list[int] | list[float] | list[int | float]
    ) -> None:
        """
        Ingest data to `self._processed_data`

        Args:
            data (list | dict): _data to ingest_
        """
        if self.validate(data):
            # Check if data is either a simple `int` or `float`
            if isinstance(data, (int, float)):
                to_append = (self._processing_rank, str(data))
                self._processed_data.append(to_append)
                self._processing_rank += 1
            else:  # Only lists
                for item in data:
                    self._processed_data.append(
                        (self._processing_rank, str(item))
                    )
                    self._processing_rank += 1
        else:
            raise TypeError("Incorrect Provided Data.")


class TextProcessor(DataProcessor):
    """
    _Child class of `DataProcessor`, used for parsing and saving
    text data_

    Args:
        DataProcessor (_type_): _Base Abstract Class `DataProcessor_
    """

    def validate(self, data: Any) -> bool:
        """
        Parse if `data` is of type either `str` or `list[str]`

        Args:
            data (Any): _raw data to parse_

        Returns:
            bool: _returns `True` is matches format, `False` otherwise_
        """
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            # Check the whole list first
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        """
        Ingest data to `self._processed_data`

        Args:
            data (list | dict): _data to ingest_
        """
        if self.validate(data):
            if isinstance(data, str):
                # self._processed_data.append(data)
                to_append = (self._processing_rank, data.strip())
                self._processed_data.append(to_append)
                self._processing_rank += 1
            else:
                for item in data:
                    self._processed_data.append(
                        (self._processing_rank, item.strip())
                    )
                    self._processing_rank += 1
        else:
            raise TypeError("Incorrect Provided Data.")


class LogProcessor(DataProcessor):
    """
    _Child class of `DataProcessor`, used for parsing and saving
    log data_

    Args:
        DataProcessor (_type_): _Base Abstract Class `DataProcessor_
    """

    def __init__(self) -> None:
        super().__init__()
        self._log_levels = [
            "EMERGENCY",
            "ALERT",
            "CRITICAL",
            "ERROR",
            "WARNING",
            "NOTICE",
            "INFO",
            "DEBUG",
        ]

    def _validate_dict(self, data: Any) -> bool:
        """
        Validate if data is of the following format :
        ```
        {'log_level': 'WARNING', 'log_message': 'message'}
        ```

        With `log_level` value part of `self._log_levels`

        Args:
            data (Any): _Data to parse_

        Returns:
            bool: _returns `True` is matches format, `False` otherwise_
        """
        for key, value in data.items():
            # Check that each node are a str:str pair
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        # Check that keys matches this format
        if list(data) != ["log_level", "log_message"] or list(data) != [
            "log_message",
            "log_level",
        ]:
            return False
        # Check that first key stripped and UPPER matches the log levels
        if list(data.values())[0].strip().upper() not in self._log_levels:
            return False
        return True

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for internal_dict in data:
                # Check if every node is a dict of size 2
                if (
                    not isinstance(internal_dict, dict)
                    or len(internal_dict) != 2
                ):
                    return False
                return self._validate_dict(internal_dict)
        elif isinstance(data, dict):
            if len(data) != 2:
                return False
            return self._validate_dict(data)
        return False

    def _ingest_dict(self, data: dict[str, str]) -> None:
        """
        Create a tuple with combined `log_level` and `log_message` and append
        it to `self._processed_data`

        Args:
            data (dict): _dict data_
        """
        log_level = data["log_level"].strip().upper()
        log_message = data["log_message"].strip()
        self._processed_data.append(
            (self._processing_rank, f"{log_level}: {log_message}")
        )
        self._processing_rank += 1

    def ingest(self, data: list[dict[str, str]] | dict[str, str]) -> None:
        """
        Ingest data to `self._processed_data`

        Args:
            data (list | dict): _data to ingest_
        """
        if self.validate(data):
            if isinstance(data, list):
                for dict_item in data:
                    self._ingest_dict(dict_item)
            else:
                self._ingest_dict(data)

def test_numeric(true_data: list, false_data: )

def main() -> None:
    """
    Main function
    """
    authorized_log_levels = [
        "EMERGENCY",
        "ALERT",
        "CRITICAL",
        "ERROR",
        "WARNING",
        "NOTICE",
        "INFO",
        "DEBUG",
    ]

    numeric_data: list = [
        42,
        0,
        -42,
        42.42,
        0.1,
        -42.42,
        [42, -42],
        [42.42, -42.42],
        [42, 42.42],
        [42, 42.42, 42, 0, 0.998, 100000],
    ]

    text_data = [
        "test",
        "test2",
        "",
        "t",
        ["t"],
        ["t", "test"],
        ["t", "test"],
        ["t", "test", "test,4"],
    ]

    log_data = [
        # Simple dicts
        {"log_level": "NOTICE", "log_message": "This is a message of notice"},
        {
            "log_message": "This is a message of warning",
            "log_level": "WarNinG",
        },
        # Build all authorized log possibilities in a list of all dicts
        [
            {"log_level": log, "log_message": f"Message of {log}"}
            for log in authorized_log_levels
        ],
    ]

    mixed_numeric_data: list = [
        42,
        0,
        -42,
        "test2",
        "",
        "t",
        ["t"],
        42.42,
        0.1,
        -42.42,
        [42, -42],
        [42.42, -42.42],
        [42, 42.42],
        [
            {"log_level": log, "log_message": f"Message of {log}"}
            for log in authorized_log_levels
        ],
    ]

    mixed_text_data = [
        "test",
        "test2",
        -42.42,
        [42, -42],
        "",
        "t",
        ["t"],
        ["t", "test"],
        {
            "log_message": "This is a message of warning",
            "log_level": "WarNinG",
        },
        ["t", "test"],
        ["t", "test", "test,4"],
    ]

    mixed_log_data = [
        [
            {"log_level": log, "log_message": f"Message of {log}"}
            for log in authorized_log_levels
        ],
        {"log_level": "NOTICE", "log_message": "This is a message of notice"},
        "t",
        ["t", "test", "test,4"],
        42.42,
        0.1,
        -42.42,
        [42, -42],
    ]



if __name__ == "__main__":
    main()
