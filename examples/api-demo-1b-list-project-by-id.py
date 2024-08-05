import argparse

from snyk import SnykClient
from utils import get_default_token_path, get_token


def parse_command_line_args():
    parser = argparse.ArgumentParser(description="Snyk API Examples")
    parser.add_argument("--orgId", type=str, help="The Snyk Organisation Id")

    parser.add_argument("--projectId", type=str, help="The project ID in Snyk")

    args = parser.parse_args()

    if args.orgId is None:
        parser.error("You must specify --orgId")

    if args.projectId is None:
        parser.error("You must specify --projectId")

    return args


snyk_token_path = get_default_token_path()
snyk_token = get_token(snyk_token_path)
args = parse_command_line_args()
org_id = args.orgId
project_id = args.projectId

# client = SnykClient(token=snyk_token, url="")
client = SnykClient("0add96ab-0ef0-42d9-8373-c6e80458b8dc", debug=True)
proj = client.organizations.get(org_id).projects.get(project_id)
params = {
          "business_criticality": ["critical", "high"],
          "lifecycle": ["development", "production"],
          "tags": [{"key": "2", "value": "tag3"}]
}
proj = client.organizations.get(org_id).projects.all(
    params={"ids": ["df7667d2-a79f-47ce-875b-99c93bf45426", "95610e38-5156-47ae-b638-9e494978a5b0"]})
proj = client.projects.all(params=params)[0]
# TODO lists are not serialized correctly as query params
proj = client.projects.all(params=params)[0]
tags = proj.attributes.tags
print("Org id: %s" % proj.organization.id)
print("\nProject name: %s" % proj.attributes.name)
print("Project id: %s\n" % proj.id)
print("  Issues Found:")
print("      High  : %s" % proj.meta.latest_issue_counts.high)
print("      Medium: %s" % proj.meta.latest_issue_counts.medium)
print("      Low   : %s" % proj.meta.latest_issue_counts.low)

if tags is not None:
    for tag in tags:
        print("  Tag: %s" % tag)
