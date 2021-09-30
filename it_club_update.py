#!/bin/env python

import requests
import textwrap

API_URL = "https://api.github.com/orgs/IT-Club-Pulchowk/repos?sort=name"
WEBPAGE_BASE_URL = "https://it-club-pulchowk.github.io/"
AVOID_REPOS = "IT-Club-Pulchowk.github.io"

README_BASE = """
<img src="assets/images/logo-128.png">

# IT Club, Pulchowk
**GitHub Organization for IT Club, Pulchowk**

📍 Pulchowk Campus, IOE, Nepal

📧 itclub@pcampus.edu.np

Twitter: [@ITClubPulchowk](https://twitter.com/ITClubPulchowk)

---

# Repositories


"""


README_BODY = ""


def update_content(name, description, stargazers_count, repo_url, webpage_url):
    global README_BODY
    description = "  " if description is None else description.strip()
    content = textwrap.dedent(
        f"""\
     ## {name}

     ⭐: {stargazers_count}
 
     **{description}**
 
     Repo: [{repo_url}]({repo_url})
 
     Webpage: [{webpage_url}]({webpage_url})
    

    """
    )

    README_BODY += content


def save_file():
    readme_full = README_BASE + README_BODY
    with open("README.md", "w") as f:
        f.write(readme_full)


def fetch_repos():
    repos = requests.get(API_URL).json()

    for repo in repos:
        name = repo["name"]
        if name in AVOID_REPOS:
            continue
        description = repo["description"]
        stargazers_count = repo["stargazers_count"]
        repo_url = repo["html_url"]
        webpage_url = WEBPAGE_BASE_URL + name

        update_content(name, description, stargazers_count, repo_url, webpage_url)


def main():
    fetch_repos()
    save_file()


if __name__ == "__main__":
    main()
