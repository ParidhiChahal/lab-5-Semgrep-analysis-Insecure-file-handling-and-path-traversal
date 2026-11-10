# Semgrep Analysis: Insecure File Handling and Path Traversal

This repository contains code samples demonstrating path traversal vulnerabilities and their mitigation, scanned using Semgrep[span_4](start_span)[span_4](end_span).

## Lab Tasks & Overview
1. **vulnerable.py**: Accepts user input and opens files without sanitization, exposing the application to path traversal[span_5](start_span)[span_5](end_span).
2. **Semgrep Scan (Before Fix)**: Identifying insecure file access patterns.
3. **secure.py**: Implements strict path prefix checking (`os.path.commonpath` or `.startswith`) to restrict file reads to the intended safe folder[span_6](start_span)[span_6](end_span).
4. **Semgrep Scan (After Fix)**: Demonstrates remediation of the vulnerability[span_7](start_span)[span_7](end_span).
5.
