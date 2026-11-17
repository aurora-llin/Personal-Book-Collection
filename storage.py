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
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)
    except OSError as error:
        raise StorageError("Could not save to " + path + ": " + str(error))


def preserve_damaged_file(path):
    """Rename a damaged file (never delete it) and return its new name."""
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    new_name = path + ".damaged-" + stamp
    try:
        os.replace(path, new_name)
    except OSError as error:
        raise StorageError("Could not preserve damaged file: " + str(error))
    return new_name
