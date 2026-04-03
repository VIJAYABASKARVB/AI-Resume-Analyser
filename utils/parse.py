def parse_response(raw_text):
    result = {}
    for line in raw_text.strip().splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip()
    return result


def get(data, key):
    return data.get(key, "N/A")


def get_score(data, key):
    raw = data.get(key, "0")
    digits = "".join(c for c in raw if c.isdigit() or c == ".")
    try:
        return float(digits)
    except:
        return 0.0


def get_list(data, key):
    raw = data.get(key, "")
    if not raw or raw == "N/A":
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]


def get_bullets(raw_text, marker="-"):
    lines = []
    for line in raw_text.splitlines():
        line = line.strip()
        if line.startswith(marker):
            lines.append(line.lstrip(marker).strip())
    return lines
