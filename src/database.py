import sqlite3

def save_result(contract_address, result):
    conn = sqlite3.connect("spoofing_detector.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS results (
                 contract_address TEXT, 
                 result TEXT)""")
    c.execute("INSERT INTO results VALUES (?, ?)", (contract_address, result))
    conn.commit()
    conn.close()
    print("Result saved to database")
