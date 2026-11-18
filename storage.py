import json
import os
from datetime import datetime


class DataFileError(Exception):
    """The file exists but its contents are damaged."""


class StorageError(Exception):
    """The file could not be read, saved, or moved."""


def load_records(path):
    """Return the saved list of records. A missing file means no records yet."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except ValueError:
        raise DataFileError("the file is not valid JSON")
    except OSError as error:
        raise StorageError("Could not read " + path + ": " + str(error))
    if not isinstance(data, list):
        raise DataFileError("the file does not contain a list of records")
    return data


def save_records(path, records):
    text = json.dumps(records, indent=2)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as error:
        raise StorageError("Could not save to " + path + ": " + str(error))


