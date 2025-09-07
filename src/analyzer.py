def detect_spoofing(data):
    print("Analyzing data for spoofing patterns...")
    if sum(data["liquidity_moves"]) < 0:
        return "Suspicious activity detected"
    return "No spoofing detected"
