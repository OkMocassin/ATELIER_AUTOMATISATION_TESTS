from tester.tests import *
import time

def run_tests():
    tests = [
        ("status", test_status),
        ("json", test_json),
        ("fields", test_fields),
        ("types", test_types),
        ("invalid", test_invalid),
        ("latency", test_latency)
    ]

    results = []
    latencies = []
    passed = 0

    for name, test in tests:
        start = time.time()
        ok = test()
        latency = (time.time() - start) * 1000

        if ok:
            passed += 1

        latencies.append(latency)

        results.append({
            "name": name,
            "status": "PASS" if ok else "FAIL",
            "latency": latency
        })

    return {
        "passed": passed,
        "failed": len(tests) - passed,
        "latency_avg": sum(latencies)/len(latencies),
        "results": results
    }
