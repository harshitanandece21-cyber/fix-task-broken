import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_report_exists_and_nonempty():
    """Criterion 1: a non-empty report file exists at /app/report.json."""
    assert REPORT_PATH.exists(), "no report.json found"
    assert REPORT_PATH.stat().st_size > 0, "report.json is empty"


def test_report_has_required_fields():
    """Criterion 2: report is valid JSON with total_requests, unique_ips, top_path."""
    data = json.loads(REPORT_PATH.read_text())
    for field in ("total_requests", "unique_ips", "top_path"):
        assert field in data, f"missing field: {field}"


def test_report_values_correct():
    """Criterion 3: field values are correct for the given access log."""
    data = json.loads(REPORT_PATH.read_text())
    assert data["total_requests"] == 6, f"expected 6 total_requests, got {data['total_requests']}"
    assert data["unique_ips"] == 3, f"expected 3 unique_ips, got {data['unique_ips']}"
    assert data["top_path"] == "/index.html", f"expected top_path '/index.html', got {data['top_path']}"