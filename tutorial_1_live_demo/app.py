import argparse
import math
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


HKD_TO_USD = 0.1282
HOST = "127.0.0.1"
DEFAULT_PORT = 8501
PROJECT_DIR = Path(__file__).resolve().parent


def convert_hkd_to_usd(amount):
    """Convert a non-negative HKD amount to USD using the demo rate."""
    if (
        isinstance(amount, bool)
        or not isinstance(amount, (int, float))
        or not math.isfinite(amount)
        or amount < 0
    ):
        raise ValueError("amount must be a non-negative number")

    return round(amount * HKD_TO_USD, 2)


class DemoRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIR), **kwargs)


def main():
    parser = argparse.ArgumentParser(description="Serve the HKD to USD demo page.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="start the server without opening a browser window",
    )
    args = parser.parse_args()

    server = ThreadingHTTPServer((HOST, args.port), DemoRequestHandler)
    url = f"http://{HOST}:{args.port}"
    print(f"Serving the demo at {url}")
    print("Press Ctrl+C to stop the server.")

    if not args.no_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping the demo server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
