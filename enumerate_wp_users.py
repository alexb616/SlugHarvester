import requests
import argparse
import sys

AUTHOR = "Alejandro Baño aka @alexb_616"

BANNER = f"""
#######################################################
#                                                     #
#   🚀  WP USER ENUMERATOR                            #
#   🔍  Author: {AUTHOR}         #
#   ⚠️  Only works if WP-JSON is accessible           #
#                                                     #
#######################################################
"""

def print_banner():
    print(BANNER)

def check_api_status(url):
    """Verifies if the WordPress REST API is active and accessible."""
    api_url = f"{url.rstrip('/')}/wp-json/"
    try:
        response = requests.get(api_url, timeout=10)
        # Check for 200 OK and JSON content type
        if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
            return True
        return False
    except requests.exceptions.RequestException:
        return False

def get_wp_users(url, output_file=None):
    """Fetches users and optionally saves slugs to a text file."""
    users_endpoint = f"{url.rstrip('/')}/wp-json/wp/v2/users"
    params = {'per_page': 100}

    try:
        response = requests.get(users_endpoint, params=params, timeout=10)

        if response.status_code == 200:
            users = response.json()
            if not users:
                print("⚠️  No public users were found.")
                return

            print(f"✅ Found {len(users)} users:\n")
            print(f"{'ID':<6} | {'Slug (Username)':<20} | {'Name'}")
            print("-" * 50)

            slugs = []
            for user in users:
                user_id = user.get('id', 'N/A')
                slug = user.get('slug', 'N/A')
                name = user.get('name', 'N/A')
                slugs.append(slug)
                print(f"👤 {user_id:<4} | {slug:<20} | {name}")

            # Save to file if requested
            if output_file:
                try:
                    with open(output_file, 'w') as f:
                        for s in slugs:
                            f.write(f"{s}\n")
                    print(f"\n💾 Slugs successfully saved to: {output_file}")
                except IOError as e:
                    print(f"\n❌ Error saving to file: {e}")

        else:
            print(f"❌ Error accessing users. Status Code: {response.status_code}")
            print("💡 Site might have restricted the /users endpoint.")

    except Exception as e:
        print(f"💥 An error occurred: {e}")

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="WP User Enumerator (Requires REST API access)")
    parser.add_argument("-u", "--url", help="Target WordPress URL (e.g., https://example.com)", required=True)
    parser.add_argument("-o", "--output", help="Output filename to save slugs (e.g., users.txt)", required=False)

    args = parser.parse_args()
    target_url = args.url

    if not target_url.startswith("http"):
        print("❌ Error: Include the protocol (http:// or https://)")
        sys.exit(1)

    print(f"🔍 Checking API status at: {target_url}...")

    if check_api_status(target_url):
        print("🌐 API detected and active. Proceeding...\n")
        get_wp_users(target_url, args.output)
    else:
        print("🚫 Stopped: The WordPress REST API is not active or is blocked.")
        sys.exit(1)

if __name__ == "__main__":
    main()
