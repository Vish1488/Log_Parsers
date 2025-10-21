This project automates the process of parsing and analyzing SSH authentication logs to detect potential brute-force attacks, reconnaissance attempts, and suspicious login activities.

It extracts key patterns such as:

Invalid login attempts

Failed password attempts

Repeated access from the same IP

Possible break-in attempts

The script processes raw logs and generates a summarized report for security monitoring and analysis.

Features: 
* Extracts and counts invalid login attempts
* Aggregates failed logins by IP address
* Highlights top offending IPs
* Generates a clean, human-readable report
* Easily extendable to include:

**How It Works**

The script reads the SSH log file from logs/auth.log.

It uses regular expressions (regex) to match lines that contain Invalid user or other suspicious login patterns.

Each matching IP address is counted using Python’s collections.Counter.

Results are sorted and written into a report (reports/report.txt) showing the top 50 suspicious IPs by failed login count.


Example Use Cases

Detecting brute-force login attempts on SSH servers

Tracking reconnaissance patterns before an attack

Identifying repeat offender IPs

Automating log analysis for security monitoring
