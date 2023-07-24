import http.server
import socketserver
import json
import os
import logging

def start_server(directory_path, port):
    # Check if the provided directory path is valid
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Error: The specified directory does not exist.")
        return

    # Set up the server configuration
    handler = http.server.SimpleHTTPRequestHandler

    # Change to the directory that you want to serve
    os.chdir(directory_path)

    # Start the server on localhost
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at port {port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()

def setup_logging(logging_config):
    if not logging_config["enabled"]:
        return

    log_file = logging_config["log_file"]
    log_level = logging_config["log_level"].upper()

    # Map log level to standard logging levels
    log_levels_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    log_level = log_levels_map.get(log_level, logging.INFO)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

if __name__ == "__main__":
    # Read configuration from settings.json
    with open('settings.json') as config_file:
        config = json.load(config_file)

    # Get the server configuration from the config
    server_config = config['server']
    directory_path = server_config['directory']
    port = server_config['port']

    # Start the server
    start_server(directory_path, port)

    # Set up logging if enabled
    logging_config = config['logging']
    setup_logging(logging_config)
