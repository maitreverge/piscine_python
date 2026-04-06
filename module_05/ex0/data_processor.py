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

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for internal_dict in data:
                # Check if every node is a dict of size 2
                if (
                    not isinstance(internal_dict, dict)
                    or len(internal_dict) != 2
                ):
                    return False
                else:
                    # Now check the internal dict
                    for key, value in internal_dict.items():
                        # Check that each node are both strings
                        if not isinstance(key, str) or not isinstance(value, str):
                            return False
                        if list(internal_dict) != ['log_level', 'log_message']:
                            return False
                        if 
                        


def main() -> None:
    """
    Main function
    """


if __name__ == "__main__":
    main()
