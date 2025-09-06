# Solana Pre-Launch Liquidity Spoofing Detector

## Overview
This project is designed to detect spoofing activities in pre-launch liquidity pools on the Solana blockchain. 
It allows traders to input token contract addresses, fetches relevant data, analyzes liquidity movements, and generates alerts.

## Features
- Input token contract address
- Liquidity inflow/outflow monitoring
- Spoofing detection logic
- Database storage of transactions and alerts
- User-friendly reporting system

## Technologies
- Python
- Solana RPC API (`solana-py`)
- SQLite / PostgreSQL
- Flask or Streamlit for UI

## Project Structure
spoofing-detector:

src:

main.py

analyzer.py

database.py

utils.py


tests:

requirements.txt

README.md