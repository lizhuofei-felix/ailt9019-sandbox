# Tutorial 1 Live Demo

A small, dependency-free page that converts HKD to USD.

## About Me
A statistics undergraduate student at the University of Hong Kong.

## Run the page

From this folder, run:

```bash
python3 app.py
```

The server starts at <http://127.0.0.1:8501> and attempts to open the page in your browser. Press `Ctrl+C` in the terminal to stop it.

To start the server without opening a browser:

```bash
python3 app.py --no-browser
```

## Run the test

```bash
python3 -m unittest -v
```

The demo uses a fixed teaching rate of `1 HKD = 0.1282 USD`. It is not a live exchange-rate service.
