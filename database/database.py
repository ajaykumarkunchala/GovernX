import sqlite3


def create_database():
    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS risk_assessments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_name TEXT,
        asset_value REAL,
        risk_score INTEGER,
        risk_level TEXT,
        estimated_loss REAL
    )
    """)

    conn.commit()
    conn.close()


def save_risk_assessment(asset_name,
                         asset_value,
                         risk_score,
                         risk_level,
                         estimated_loss):

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO risk_assessments
    (asset_name, asset_value, risk_score, risk_level, estimated_loss)

    VALUES (?, ?, ?, ?, ?)
    """, (
        asset_name,
        asset_value,
        risk_score,
        risk_level,
        estimated_loss
    ))

    conn.commit()
    conn.close()


def get_all_assessments():

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        asset_name,
        asset_value,
        risk_score,
        risk_level,
        estimated_loss
    FROM risk_assessments
    """)

    rows = cursor.fetchall()

    conn.close()

    assessments = []

    for row in rows:
        assessments.append({
            "id": row[0],
            "asset_name": row[1],
            "asset_value": row[2],
            "risk_score": row[3],
            "risk_level": row[4],
            "estimated_loss": row[5]
        })

    return assessments

def get_dashboard_summary():

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM risk_assessments")
    total_assets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM risk_assessments WHERE risk_level='Critical'")
    critical = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM risk_assessments WHERE risk_level='High'")
    high = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM risk_assessments WHERE risk_level='Medium'")
    medium = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM risk_assessments WHERE risk_level='Low'")
    low = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(risk_score) FROM risk_assessments")
    avg = cursor.fetchone()[0]

    conn.close()

    if avg is None:
        avg = 0

    return {
        "total_assets": total_assets,
        "critical_assets": critical,
        "high_assets": high,
        "medium_assets": medium,
        "low_assets": low,
        "average_risk_score": round(avg, 2)
    }
def get_assessments_by_level(level):

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               asset_name,
               asset_value,
               risk_score,
               risk_level,
               estimated_loss
        FROM risk_assessments
        WHERE risk_level = ?
    """, (level,))

    rows = cursor.fetchall()
    conn.close()

    assessments = []

    for row in rows:
        assessments.append({
            "id": row[0],
            "asset_name": row[1],
            "asset_value": row[2],
            "risk_score": row[3],
            "risk_level": row[4],
            "estimated_loss": row[5]
        })

    return assessments

def get_assessments_by_level(level):

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               asset_name,
               asset_value,
               risk_score,
               risk_level,
               estimated_loss
        FROM risk_assessments
        WHERE risk_level = ?
    """, (level,))

    rows = cursor.fetchall()
    conn.close()

    assessments = []

    for row in rows:
        assessments.append({
            "id": row[0],
            "asset_name": row[1],
            "asset_value": row[2],
            "risk_score": row[3],
            "risk_level": row[4],
            "estimated_loss": row[5]
        })

    return assessments

def search_asset(asset_name):

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            asset_name,
            asset_value,
            risk_score,
            risk_level,
            estimated_loss
        FROM risk_assessments
        WHERE asset_name LIKE ?
    """, ('%' + asset_name + '%',))

    rows = cursor.fetchall()

    conn.close()

    assets = []

    for row in rows:
        assets.append({
            "id": row[0],
            "asset_name": row[1],
            "asset_value": row[2],
            "risk_score": row[3],
            "risk_level": row[4],
            "estimated_loss": row[5]
        })

    return assets

def update_risk_assessment(id, asset_name, asset_value,
                           risk_score, risk_level,
                           estimated_loss):

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE risk_assessments
        SET
            asset_name = ?,
            asset_value = ?,
            risk_score = ?,
            risk_level = ?,
            estimated_loss = ?
        WHERE id = ?
    """, (
        asset_name,
        asset_value,
        risk_score,
        risk_level,
        estimated_loss,
        id
    ))

    conn.commit()
    conn.close()
def delete_risk_assessment(id):

    conn = sqlite3.connect("database/governx.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM risk_assessments
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()