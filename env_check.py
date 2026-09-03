"""Check whether an environment variable exists without printing its value."""

import os
import sys


def variable_exists(name: str) -> bool:
    """Return only whether the named environment variable exists."""
    return name in os.environ


if __name__ == "__main__":
    variable_name = sys.argv[1] if len(sys.argv) > 1 else "AILT9019_PRACTICE_FLAG"
    print(variable_exists(variable_name))
