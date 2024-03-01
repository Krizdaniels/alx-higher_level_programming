#!/usr/bin/python3
"""It fetches https://intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status using requests"""
    try:
        response = requests.get('https://intranet.hbtn.io/status')
        response.raise_for_status()  # Check if the request was successful

        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")

    except requests.RequestException as e:
        print(f"Error making the request: {e}")
