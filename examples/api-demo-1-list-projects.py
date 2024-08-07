import argparse

from snyk import SnykClient
from utils import get_default_token_path, get_token


def parse_command_line_args():
    parser = argparse.ArgumentParser(description="Snyk API Examples")
    parser.add_argument(
        "--orgId", type=str, help="The Snyk Organisation ID", required=True
    )
    return parser.parse_args()


snyk_token_path = get_default_token_path()
snyk_token = get_token(snyk_token_path)
args = parse_command_line_args()
org_id = args.orgId

client = SnykClient(token="0add96ab-0ef0-42d9-8373-c6e80458b8dc", debug=True)
params = {"tags": [{"key": "2", "value": "tag3"}]}
for proj in client.organizations.get(org_id).projects.all(params=params):
    tags = proj.tags.all()
    print("\nProject name: %s" % proj.name)
    print("  Issues Found:")
    print("      High  : %s" % proj.issueCountsBySeverity.high)
    print("      Medium: %s" % proj.issueCountsBySeverity.medium)
    print("      Low   : %s" % proj.issueCountsBySeverity.low)
    print("Tags: ", tags)

for proj in client.projects.all(params=params):
    print("\nProject name: %s" % proj.name)
