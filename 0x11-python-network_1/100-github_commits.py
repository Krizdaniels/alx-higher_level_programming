#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: {} <repository> <owner>".format(argv[0]))
        exit(1)

    repo = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for request errors
        res_list = r.json()

        for i in range(min(10, len(res_list))):
            print("{}: {}".format(res_list[i]['sha'],
                                  res_list[i]['commit']['author']['name']))

    except requests.RequestException as e:
        print("Error making the request:", e)
    except IndexError:
        print("Not enough commits available.")
