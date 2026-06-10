import re, os

p = 'vibe.ipynb'
if os.path.exists(p):
    s = open(p, 'r', encoding='utf-8').read()
    new = s
    # Redact common Google API key pattern
    new = re.sub(r'AIza[0-9A-Za-z_\-]{35}', '[REDACTED_GCP_API_KEY]', new)
    # Redact tokens that start with AQ.
    new = re.sub(r'AQ\.[A-Za-z0-9_\-]{20,100}', '[REDACTED_API_KEY]', new)
    # Redact any api_key="..." or api_key='...'
    new = re.sub(r'(api_key\s*=\s*)["\']([^"\']+)["\']', r"\1\"[REDACTED]\"", new)
    if new != s:
        open(p, 'w', encoding='utf-8').write(new)
        print('Scrubbed secrets in', p)
else:
    print(p, 'not found')
