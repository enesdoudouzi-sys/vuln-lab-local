import socket
import concurrent.futures

def scan_port(host, port, timeout=0.5):
    """Scannt einen einzelnen Port – nur legale Nutzung in eigener Umgebung!"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return port, (result == 0)
    except Exception:
        return port, False

def scan_range(host, start_port, end_port):
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = [
            executor.submit(scan_port, host, port)
            for port in range(start_port, end_port + 1)
        ]
        for future in futures:
            port, open_flag = future.result()
            results[port] = open_flag
    return results

