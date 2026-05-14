# SlugHarvester
A Python-based WP-JSON API user enumerator and slug extractor for security auditing.

# WordPress User Enumerator (API Check) 🚀

This tool is designed to extract WordPress usernames (slugs) via the **WP-JSON REST API**. It includes a pre-flight check to ensure the API is reachable before attempting extraction.

> **Note:** This script only works if the target site has the WordPress REST API enabled and the `/wp/v2/users` endpoint is public.

## ✨ Features

- 🔌 **Dependency Check**: Verifies API availability before execution.
- 📂 **Export to TXT**: Automatically saves slugs to a file for brute-force tools (Wpscan, Hydra, Burp, etc.).
- 👤 **Detail**: Displays ID, Slug, and Display Name in the terminal.

## 📋 Requirements
- Python 3.x
- `requests` library (`pip install requests`)

## 🛠 Usage

Basic enumeration:
```bash
python3 enumerate_wp_users.py -u https://target-site.com
```
Enumerate and save slugs to a file:
```bash
python3 enumerate_wp_users.py -u https://target-site.com -o usernames.txt
```

## ⚖️ Disclaimer
This script is intended for legal security audits and educational purposes only. Unauthorized access to computer systems is illegal.

Author: Alejandro Baño Andrés aka @alexb_616
