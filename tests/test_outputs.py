import json
from pathlib import Path
from collections import Counter
import re


def _ground_truth():
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
    return total, len(ips), paths.most_common(1)[0][0]


def _report():
    assert Path("/app/report.json").exists(), "no report.json found"
    with open("/app/report.json") as f:
        return json.load(f)


def test_report_exists_and_valid_json():
    """Verifies instruction.md criterion 1: report.json exists and is valid JSON."""
    report = _report()
    assert isinstance(report, dict)


def test_total_requests():
    """Verifies instruction.md criterion 2: total_requests matches the log."""
    total, _, _ = _ground_truth()
    report = _report()
    assert report.get("total_requests") == total


def test_unique_ips():
    """Verifies instruction.md criterion 3: unique_ips matches the log."""
    _, unique_ips, _ = _ground_truth()
    report = _report()
    assert report.get("unique_ips") == unique_ips


def test_top_path():
    """Verifies instruction.md criterion 4: top_path matches the log."""
    _, _, top_path = _ground_truth()
    report = _report()
    assert report.get("top_path") == top_path