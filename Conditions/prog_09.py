#This program analyzes website requests, HTTP status codes, failed requests, and popular pages.
def analyze_server_logs(logs: list[dict]) -> None:
    status_counts = {}
    endpoint_counts = {}
    failed_requests = []
    total_response_time = 0

    for log in logs:
        status_code = log["status_code"]
        endpoint = log["endpoint"]
        response_time = log["response_time"]

        status_counts[status_code] = (
            status_counts.get(status_code, 0) + 1
        )

        endpoint_counts[endpoint] = (
            endpoint_counts.get(endpoint, 0) + 1
        )

        total_response_time += response_time

        if status_code >= 400:
            failed_requests.append(log)

    average_response_time = total_response_time / len(logs)

    print("\nHTTP STATUS REPORT")
    print("-" * 45)

    for status_code, count in status_counts.items():
        print(f"Status {status_code}: {count} requests")

    print("\nENDPOINT USAGE")
    print("-" * 45)

    most_visited_endpoint = ""
    highest_visits = 0

    for endpoint, count in endpoint_counts.items():
        print(f"{endpoint:<25}: {count}")

        if count > highest_visits:
            highest_visits = count
            most_visited_endpoint = endpoint

    print("\nFAILED REQUESTS")
    print("-" * 45)

    for request in failed_requests:
        print(
            f"IP: {request['ip_address']:<15} "
            f"Endpoint: {request['endpoint']:<20} "
            f"Status: {request['status_code']}"
        )

    print("-" * 45)
    print(f"Average response time : {average_response_time:.2f} ms")
    print(f"Most visited endpoint : {most_visited_endpoint}")
    print(f"Total failed requests : {len(failed_requests)}")


server_logs = [
    {
        "ip_address": "192.168.1.10",
        "endpoint": "/login",
        "status_code": 200,
        "response_time": 125
    },
    {
        "ip_address": "192.168.1.12",
        "endpoint": "/products",
        "status_code": 200,
        "response_time": 180
    },
    {
        "ip_address": "192.168.1.15",
        "endpoint": "/login",
        "status_code": 401,
        "response_time": 95
    },
    {
        "ip_address": "192.168.1.18",
        "endpoint": "/checkout",
        "status_code": 500,
        "response_time": 450
    },
    {
        "ip_address": "192.168.1.20",
        "endpoint": "/products",
        "status_code": 200,
        "response_time": 160
    }
]
analyze_server_logs(server_logs)