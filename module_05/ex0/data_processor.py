#! /usr/bin/python3
from abc import ABC, abstractmethod
from typing import Any

"""
This modules focuses on the use of abstract base classes (ABCs) 
"""

"""
Notes :
Abstract Class : can't be instancianted, raises a TypeError.
Serves as a blueprint
"""


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._processed_data: list[tuple[int, str]] = []
        self._processing_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # No need to override this method
    def output(self) -> tuple[int, str]: ...


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

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
        elif isinstance(data, list):
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
    def __init__(self) -> None:
        super().__init__()

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
        elif isinstance(data, list):
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
                to_append = (self._processing_rank, data)
                self._processed_data.append(to_append)
                self._processing_rank += 1
            else:
                for item in data:
                    self._processed_data.append((self._processing_rank, item))
                    self._processing_rank += 1
        else:
            raise TypeError("Incorrect Provided Data.")


class LogProcessor(DataProcessor):
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
        if list(data) != ["log_level", "log_message"]:
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

    def _ingest_dict(self, data: dict) -> None:
        """
        Create a tuple with combined `log_level` and `log_message` and append it to `self._processed_data`

        Args:
            data (dict): _dict data_
        """
        log_level = data["log_level"].strip().upper()
        log_message = data["log_message"].strip()
        self._processed_data.append(
            (self._processing_rank, f"{log_level}: {log_message}")
        )
        self._processing_rank += 1

    def ingest(self, data: list | dict) -> None:
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


def main() -> None:
    """
    Main function
    """


if __name__ == "__main__":
    main()
