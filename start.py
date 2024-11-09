import signal
import subprocess
import time
import os


def kill_process_on_port(port):
    try:
        # Use lsof to find any process IDs (PIDs) using the specified port
        result = subprocess.run(
            ["lsof", "-t", f"-i:{port}"], capture_output=True, text=True, check=True
        )

        # Get list of PIDs from the result
        pids = result.stdout.strip().split()

        # Terminate each PID
        for pid in pids:
            os.kill(int(pid), signal.SIGKILL)
            print(f"Killed process {pid} on port {port}")
    except subprocess.CalledProcessError:
        print(f"No process found on port {port}.")


services = [
    ("tunnels", "tunnel-datamarket-db", 31113, 5432),
    ("tunnels", "tunnel-datasets-db", 31114, 5432),
    ("tunnels", "tunnel-files-db", 31115, 5432),
    ("tunnels", "tunnel-iam-db", 31116, 5432),
    ("tunnels", "tunnel-maps-db", 31117, 5432),
    ("tunnels", "tunnel-ml-db", 31118, 5432),
    ("tunnels", "tunnel-payments-db", 31119, 5432),
    ("tunnels", "tunnel-rasters-db", 31121, 5432),
    ("tunnels", "tunnel-stitching-db", 31122, 5432),
    ("tunnels", "tunnel-vectors-db", 31123, 5432),
]
processes = []

for namespace, service_name, local_port, target_port in services:
    kill_process_on_port(local_port)
    process = subprocess.Popen(
        [
            "kubectl",
            "port-forward",
            f"svc/{service_name}",
            f"{local_port}:{target_port}",
            "-n",
            namespace,
        ]
    )
    processes.append(process)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for process in processes:
        process.terminate()
    print("Port-forwarding stopped.")
