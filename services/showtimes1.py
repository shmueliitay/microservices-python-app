from typing import Dict, Any, List
from pathlib import Path
import json
from flask import Flask
from werkzeug.exceptions import NotFound
from services import root_dir, nice_json
import os

app = Flask(__name__)
# Add an instance identifier to differentiate between services
INSTANCE_ID = os.getenv("INSTANCE_ID", "unknown")
PORT = int(os.getenv("PORT", "5002"))

# Path to your showtimes database file
showtimes_file = "showtimes.json"

def load_showtimes() -> Dict[str, List[str]]:
    """Load showtimes data from JSON file"""
    showtimes_file = root_dir() / "database" / "showtimes.json"
    try:
        with open(showtimes_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        app.logger.error(f"Showtimes database file not found at {showtimes_file}")
        return {}
    except json.JSONDecodeError:
        app.logger.error(f"Invalid JSON in showtimes database file {showtimes_file}")
        return {}

showtimes = load_showtimes()

@app.route("/", methods=['GET'])
def hello() -> Dict[str, Any]:
    """Root endpoint showing available routes"""
    return {
        "uri": "/",
        "subresource_uris": {
            "showtimes": "/showtimes",
            "showtime": "/showtimes/<date>"
        }
    }

@app.route("/showtimes/<date>", methods=['GET'])
def showtimes_by_date(date: str) -> List[str]:
    """Get movie IDs for shows on a specific date"""
    if date not in showtimes:
        app.logger.warning(f"No showtimes found for date {date}")
        raise NotFound(description=f"No showtimes found for date {date}")
    return showtimes[date]


@app.route("/showtimes/", methods=['GET'])
def showtimes_list() -> Dict[str, List[str]]:
    """Get all showtimes"""
    return {
	"instance": INSTANCE_ID,
	"showtimes": showtimes
}
def main() -> None:
    """Main entry point for the application"""
    app.run(host="0.0.0.0", port=PORT, debug=True)

if __name__ == "__main__":
    main()
