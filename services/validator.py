# services/validator.py

REQUIRED_FIELDS = [
    "asset_name",
    "asset_value",
    "public_access",
    "encryption",
    "mfa",
    "firewall_enabled",
    "open_ports",
    "critical_vulnerabilities",
    "backup_enabled"
]


def validate_input(data):

    missing_fields = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            missing_fields.append(field)

    if missing_fields:
        return False, {
            "status": "error",
            "message": "Missing required fields",
            "missing_fields": missing_fields
        }

    return True, None