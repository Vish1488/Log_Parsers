import re
from pathlib import Path
from collections import Counter, defaultdict
from dateutil import parser as dtparser

LOG_DIR = Path(__file__).resolve().parents[1] / "logs"
Report_DIR = Path(__file__).resolve().parents[1] / "reports"

def Parse_line(line):
    #to extract timestamp, service, message
    #regex to parse logs
    m = re.match(r'^(?P<ts>\w+ \d+ \d+:\d+:\d+) (?P<host>\S+) (?P<svc>\S+)\[(?P<pid>\d+)\]: (?P<msg>.+)$', line)
    if not m:
        return None
    ts = dtparser.parse(m.group("ts"))
    return {"ts":ts, "service": m.group("svc"), "'pid": m.group("pid"), "msg": m.group("msg")}

def main():
    failed_ip = Counter()
    for f in LOG_DIR.glob("*.log"):
        with f.open() as fh:
            for line in fh:
                rec = Parse_line(line.strip())
                if not rec:
                    continue
                #failed login detection
                if "Invalid user" in rec["msg"]:
                    #extracting IP address from msg
                    ip_m = re.search(r' from (\d+\.\d+\.\d+\.\d+)',rec["msg"])
                    if ip_m:
                        failed_ip[ip_m.group(1)] += 1
    Report_DIR.mkdir(exist_ok=True)
    with (Report_DIR/"report.txt").open("w") as out:
        out.write("Failed login counts by IP:\n")
        for ip, c in failed_ip.most_common(100):
            out.write(f"{ip}: {c}\n")

if __name__ == "__main__":
    main()
