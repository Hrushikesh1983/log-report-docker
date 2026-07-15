There is an access log at /app/access.log. Parse it and write a JSON
summary report to /app/report.json with the following fields:

- total_requests: the total number of request lines in the log.
- unique_ips: the number of distinct client IP addresses that made requests.
- top_path: the request path (e.g. /index.html) that appears most often.

Success criteria:
1. /app/report.json exists and contains valid JSON.
2. total_requests equals the total number of lines in /app/access.log.
3. unique_ips equals the number of distinct IP addresses in /app/access.log.
4. top_path equals the most frequently requested path in /app/access.log.