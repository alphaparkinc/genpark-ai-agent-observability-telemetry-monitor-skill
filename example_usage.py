from client import AiAgentObservabilityTelemetryMonitorClient

def main():
    client = AiAgentObservabilityTelemetryMonitorClient()
    logs = [{"step": 1, "tool": "search", "status": "success"}, {"step": 2, "tool": "write", "status": "success"}]
    res = client.monitor_telemetry(logs)
    print(f"Total Token Usage: {res['total_token_usage']}")
    print(f"P95 Latency: {res['latency_p95_ms']}ms")

if __name__ == "__main__":
    main()
