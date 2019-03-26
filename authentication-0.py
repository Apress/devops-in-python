def canonical_query_string(query):
    if not query:
        return ""
    parsed = parse_qs(url.query, keep_blank_values=True)
    return "?" + urlencode(parsed, doseq=True)