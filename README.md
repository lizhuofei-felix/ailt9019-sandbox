# AILT9019 Getting Started Practice

This small practice repository follows the AILT9019 Getting Started Guide.

## Goal

Practice the basic workflow of running Python, reading an error, testing a function, and using Git safely.

## Setup

Use Python 3 and run the examples from this directory:

```bash
python3 --version
python3 hello.py
python3 practice.py
python3 env_check.py AILT9019_PRACTICE_FLAG
```

## What works

- `hello.py` prints a greeting after the text-change exercise.
- `practice.py` calculates `final_price(price, discount)` for two values, including discount `0`.
- `env_check.py` prints only `True` or `False`; it never prints an environment-variable value.
- The missing-quote exercise produced `SyntaxError: unterminated string literal`, and the quote was restored before committing.

The AI-assisted change was explained before implementation: `final_price` follows the guide's formula, and `env_check.py` checks only whether a named variable exists. Both scripts were run locally after the change.

## Successful runs

```text
$ python3 --version
Python 3.14.5
$ python3 hello.py
Hello, AILT9019! Python and Git are working.
$ python3 practice.py
final_price(100, 0.2) = 80.0
final_price(50, 0) = 50
$ python3 env_check.py AILT9019_PRACTICE_FLAG
False
$ AILT9019_PRACTICE_FLAG=present python3 env_check.py AILT9019_PRACTICE_FLAG
True
```

## Limitations

This is a learning exercise, not a production pricing or configuration system. The function expects a decimal discount such as `0.20` and does not validate input ranges.

## Safety

No `.env` file, password, API key, private dataset, or credential is included. `.gitignore` excludes local secrets, key files, generated Python files, and temporary files.
