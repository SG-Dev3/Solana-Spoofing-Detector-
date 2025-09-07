from data_fetcher import fetch_transactions
from analyzer import detect_spoofing
from database import save_result
from alerts import generate_alert

def main():
    print("🚀 Solana Spoofing Detector Running...")
    contract_address = input("Enter Token Contract Address: ")

    # Step 1: Fetch data
    data = fetch_transactions(contract_address)

    # Step 2: Analyze data
    result = detect_spoofing(data)

    # Step 3: Save result
    save_result(contract_address, result)

    # Step 4: Generate alert
    generate_alert(contract_address, result)

if __name__ == "__main__":
    main()
