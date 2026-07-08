There is an access log in the working directory. Analyze the traffic and summarize
what you find — how many requests there were, the clients involved, and which pages
were popular. Save your findings so they can be reviewed.

Success criteria:
1. A non-empty report file exists at `/app/report.json`.
2. The report is valid JSON containing the fields `total_requests`, `unique_ips`,
   and `top_path`.
3. The values of those fields are correct for the given access log.