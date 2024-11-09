import subprocess
import json
import base64
from dataclasses import dataclass
from urllib.parse import urlparse

namespace = "default"
secret_name = "databases"

result = subprocess.run(
    ["kubectl", "get", "secret", secret_name, "-n", namespace, "-o", "json"],
    capture_output=True,
    text=True,
)


@dataclass
class DatabaseDetails:
    username: str
    password: str
    database: str


secret_data = json.loads(result.stdout)
data = secret_data.get("data", {})
database_details = []
for secret_name, secret_value_encoded in data.items():
    secret_value = base64.b64decode(secret_value_encoded).decode("utf-8")
    parsed_url = urlparse(secret_value)

    database_details.append(
        DatabaseDetails(
            username=base64.b64encode(parsed_url.username.encode()).decode(),
            password=base64.b64encode(parsed_url.password.encode()).decode(),
            database=parsed_url.path.lstrip("/"),
        )
    )
pass
