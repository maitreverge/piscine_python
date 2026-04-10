#! /usr/bin/python3
"""
This modules focuses on the use of abstract base classes (ABCs)

Notes :
str(c.__class__.__name__) to print a class name
An bool is a int
assert(True, int) => Okay

To make a difference, assert type(boolean_value)in (float, int) => assert err

Protocol Class : Allows
"""

from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    """
    _Protocol for export plugins_

    Args:
        Protocol (_type_): _Protocol class for export plugins_
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """
        _Method to process output data_

        Args:
            data (list[tuple[int, str]]): _data to process_
        """


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

    def get_total_processed(self) -> int:
        """
        Return the total number of processed data

        Returns:
            int: _Total number of processed data_
        """
        return self._processing_rank

    def get_total_remaining(self) -> int:
        """
        Return the total number of remaining data

        Returns:
            int: _Total number of remaining data_
        """
        return len(self._processed_data)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        _Abstract Method for validating data_

        Args:
            data (Any): _raw data to parse_

        Returns:
            bool: _returns `True` is matches format, `False` otherwise_
        """

    def stats_data_processed(self) -> tuple[int, int]:
        """
        Return a tuple of `(Total processed data, Remaining Data)`

        Returns:
            tuple[int, int]: _Processed Data stats_
        """
        return (self._processing_rank, len(self._processed_data))

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
        assert len(self._processed_data) > 0, "No data left"
        return self._processed_data.pop(0)


class DataStream:
    """
    _Class for managing a stream of data processors_
    """

    def __init__(self) -> None:
        print("Initiating DataStream...\n")
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """
        _Register a data processor. Reject if already registered_

        Args:
            proc (DataProcessor): _Data processor to register_

        Raises:
            ValueError: _Raised if the processor is already registered_
        """
        assert isinstance(
            proc, DataProcessor
        ), "DataStream.register_processor. `proc` arguent not `DataProcessor`"
        if proc in self._processors:
            # ! NOTE `str(proc.__class__.__name__` print the class name
            print(f"WARNING: {proc.__class__.__name__} already in DataStream")
            return
        self._processors.append(proc)
        print(f"{proc.__class__.__name__} processor successfully registered")

    def process_stream(self, stream: list[Any]) -> None:
        """
        _Process a stream of data_

        Args:
            stream (list[Any]): _Stream of data to process_
        """
        for item in stream:
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    break
            else:
                print(f"Current data :\n---\n{item}\n---\nCan't be processed")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        _Output a specified number of items from each processor_

        Args:
            nb (int): _number of items to output from each processor_
            plugin (ExportPlugin): _plugin to process output data_
        """
        assert (
            isinstance(nb, int) and nb > 0
        ), "DataStream.output_pipeline : `nb` is not a positive int"
        result: list[tuple[int, str]] = []

        for processor in self._processors:
            max_it: int = nb

            if processor.get_total_remaining() < max_it:
                max_it = processor.get_total_remaining()
                print(f"WARNING : {processor.__class__.__name__} ", end="")
                print(f"can't process above {nb} output_pipelines.", end="")
                print(f"Will process {max_it}.")

            print(f"Output {max_it} items from {processor.__class__.__name__}")
            for _ in range(max_it):
                result.append(processor.output())
            plugin.process_output(result)
            result.clear()

    def print_processors_stats(self) -> None:
        """
        Need to know how much data has been processed + how much remaining
        """
        print("=== Data Stream Statistics ===")
        if len(self._processors) == 0:
            print("No processor registered, so stats to display\n")
            return

        for processor in self._processors:
            proc_name: str = processor.__class__.__name__
            total, remaining = processor.stats_data_processed()
            print(f"{proc_name} : {total} items processed ", end="")
            print(f"remaining {remaining} on processor")


class CsvExport:
    """
    _Class for exporting data in CSV format_
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """
        _Process output data in CSV format_
        Args:
            data (list[tuple[int, str]]): _data to process_
        """
        print("CSV Output: ")
        len_data: int = len(data)
        for i, item in enumerate(data, 1):
            print(f"{item[1]}", end="")
            if i != len_data:
                print(", ", end="")
        print("")


class JsonExport:
    """
    _Class for exporting data in JSON format_
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """
        _Process output data in JSON format_
        Args:
            data (list[tuple[int, str]]): _data to process_
        """
        print("JSON Output: ")
        len_data: int = len(data)
        print("{")
        for i, item in enumerate(data, 1):
            nb, message = item
            print(f'"item_{nb}": "{message}"', end="")
            if i != len_data:
                print(",", end="")
        print("}")


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
        # if isinstance(data, (int, float)):
        if type(data) in (int, float):
            return True
        if isinstance(data, list):
            # Check the whole list first
            for item in data:
                # if not isinstance(item, (int, float)):
                if type(item) not in (int, float):
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
        if list(data) not in [
            ["log_level", "log_message"],
            ["log_message", "log_level"],
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


def main() -> None:
    """
    Main function
    """
    print("=== Code Nexus - Data Pipeline ===")
    data_stream = DataStream()

    data_stream.print_processors_stats()

    data_batch_1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    data_batch_2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": " ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    text_p = TextProcessor()
    num_p = NumericProcessor()
    log_p = LogProcessor()

    try:
        data_stream.register_processor(text_p)
        # data_stream.register_processor(text_p)  #! Raises a warning
        data_stream.register_processor(num_p)
        data_stream.register_processor(log_p)
        # data_stream.register_processor(num_p)  #! Raises a warning
        data_stream.process_stream(data_batch_1)
        data_stream.print_processors_stats()
        data_stream.output_pipeline(3, CsvExport())
        data_stream.print_processors_stats()
        data_stream.process_stream(data_batch_2)
        data_stream.output_pipeline(5, JsonExport())
        data_stream.print_processors_stats()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
