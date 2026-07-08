import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_report_exists():
    """The agent produced a report file."""
    assert REPORT_PATH.exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert REPORT_PATH.stat().st_size > 0, "report.json is empty"


def test_report_values_correct():
    """The report contains the correct computed values, not just any output."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("total_requests") == 6, f"expected 6 total_requests, got {data.get('total_requests')}"
    assert data.get("unique_ips") == 3, f"expected 3 unique_ips, got {data.get('unique_ips')}"
    assert data.get("top_path") == "/index.html", f"expected top_path '/index.html', got {data.get('top_path')}"