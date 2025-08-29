import os
from datetime import datetime

import requests

# Replace with your actual LeetCode session cookie
SESSION_COOKIE = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNzgyODQ3NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVmMTliNDZhZWZiMzcxOWZmMDc0MzdhNjYwZmM4NTBhNmU4MTBlNTNhNGQ4MTVmMzhjYWY0YmI0NTczZWNiNWEiLCJzZXNzaW9uX3V1aWQiOiJmMjlhZGQwNSIsImlkIjo3ODI4NDc0LCJlbWFpbCI6ImFwa3VuZXNoQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiU2VlTWV3IiwidXNlcl9zbHVnIjoiU2VlTWV3IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL1NlZU1ldy9hdmF0YXJfMTczNDk4Mzc0My5wbmciLCJyZWZyZXNoZWRfYXQiOjE3NTY0ODc0MTcsImlwIjoiMTM0LjIwNC41Ni4xMTQiLCJpZGVudGl0eSI6ImM1YzNlZDcwMTg2ODAzN2ZiYTU5YTQyNjUyNzUwZTVlIiwiZGV2aWNlX3dpdGhfaXAiOlsiZDZmNDMzZjhkM2M3MGFhOGY4NTZkZWFkZDE4Y2Q3ODMiLCIxMzQuMjA0LjU2LjExNCJdLCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.FKncbHg1oIELY6jfzvox-Rexq8XKksYrem-ADTETHrY"
HEADERS = {
    "cookie": f"LEETCODE_SESSION={SESSION_COOKIE}",
    "referer": "https://leetcode.com",
    "content-type": "application/json",
}

GRAPHQL_URL = "https://leetcode.com/graphql/"

LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!) {
  submissionList(offset: $offset, limit: $limit) {
    submissions {
      id
      title
      titleSlug
      timestamp
    }
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
  }
}
"""


DETAIL_QUERY = """
query submissionDetails($id: Int!) {
  submissionDetails(submissionId: $id) {
    id
    code
  }
}
"""


def fetch_submissions(limit=20):
    offset = 0
    all_subs = []
    while True:
        resp = requests.post(
            GRAPHQL_URL,
            headers=HEADERS,
            json={"query": LIST_QUERY, "variables": {"offset": offset, "limit": limit}},
        )
        subs = resp.json()["data"]["submissionList"]["submissions"]
        if not subs:
            break
        all_subs.extend(subs)
        offset += limit
    return all_subs


def fetch_submission_detail(sub_id):
    resp = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": DETAIL_QUERY, "variables": {"id": int(sub_id)}},
    )
    return resp.json()["data"]["submissionDetails"]


def fetch_question_number(title_slug: str):
    resp = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": QUESTION_QUERY, "variables": {"titleSlug": title_slug}},
    )
    return resp.json()["data"]["question"]["questionFrontendId"]


def save_submission(sub, detail):
    folder = "submissions"
    ext = ".py"

    qid = fetch_question_number(sub["titleSlug"])
    safe_title = sub["title"].replace(" ", "_")
    qid_str = f"{int(qid):04d}"

    filename = os.path.join(folder, f"lc_{qid_str}_{safe_title}{ext}")

    # Write the code
    with open(filename, "w") as f:
        if detail:
            f.write(detail["code"] if detail.get("code") is not None else "")
            print(f"Saved {filename}")
        else:
            print(f"Detail not found for {filename}, may have to add manually.")


if __name__ == "__main__":
    submissions = fetch_submissions(limit=20)
    print(f"Fetched {len(submissions)} submissions")

    seen_titles = set()
    for sub in submissions:
        title = sub["title"]
        if title in seen_titles:
            continue  # skip older submissions for this problem
        detail = fetch_submission_detail(sub["id"])
        save_submission(sub, detail)
        seen_titles.add(title)
