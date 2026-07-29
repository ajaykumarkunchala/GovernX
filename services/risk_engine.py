RISK_RULES = {
    "public_access": 30,
    "encryption": 20,
    "mfa": 15,
    "firewall_enabled": 15,
    "open_ports": 10,
    "critical_vulnerabilities": 10,
    "backup_enabled": 10
}


def calculate_risk(data):

    score = 0
    findings = []
    recommendations = []

    if data.get("public_access"):
        score += RISK_RULES["public_access"]
        findings.append("Public access is enabled")
        recommendations.append("Restrict public access using IAM policies or VPN.")

    if not data.get("encryption"):
        score += RISK_RULES["encryption"]
        findings.append("Encryption is disabled")
        recommendations.append("Enable encryption for sensitive data.")

    if not data.get("mfa"):
        score += RISK_RULES["mfa"]
        findings.append("MFA is disabled")
        recommendations.append("Enable Multi-Factor Authentication (MFA).")

    if not data.get("firewall_enabled"):
        score += RISK_RULES["firewall_enabled"]
        findings.append("Firewall is disabled")
        recommendations.append("Enable and properly configure the firewall.")

    if data.get("open_ports", 0) > 5:
        score += RISK_RULES["open_ports"]
        findings.append("Too many open ports")
        recommendations.append("Close unnecessary open ports.")

    if data.get("critical_vulnerabilities", 0) > 0:
        score += RISK_RULES["critical_vulnerabilities"]
        findings.append("Critical vulnerabilities found")
        recommendations.append("Apply the latest security patches immediately.")

    if not data.get("backup_enabled"):
        score += RISK_RULES["backup_enabled"]
        findings.append("Backup is disabled")
        recommendations.append("Enable automated backups and test recovery.")

    # Limit score to 100
    score = min(score, 100)

    # Decide Risk Level
    if score >= 80:
        level = "Critical"
    elif score >= 60:
        level = "High"
    elif score >= 40:
        level = "Medium"
    elif score >= 20:
        level = "Low"
    else:
        level = "Safe"

    return {
        "asset_name": data.get("asset_name"),
        "risk_score": score,
        "risk_level": level,
        "findings": findings,
        "recommendations": recommendations
    }