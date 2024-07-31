from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from .enums import BusinessCriticality, Enviroment, Lifecycle, MetaCount

@dataclass
class ProjectsQueryParams:
    target_id: Optional[List[str]] = None
    target_reference: Optional[str] = None
    target_file: Optional[str] = None
    target_runtime: Optional[str] = None
    meta_count: Optional[MetaCount] = None
    ids: Optional[List[str]] = None
    names: Optional[List[str]] = None
    names_start_with: Optional[List[str]] = None
    origins: Optional[List[str]] = None
    types: Optional[List[str]] = None
    expand: Optional[List[str]] = None
    meta_latest_issue_counts: Optional[bool] = None
    meta_latest_dependency_total: Optional[bool] = None
    cli_monitored_before: Optional[str] = None
    cli_monitored_after: Optional[str] = None
    importing_user_public_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    business_criticality: Optional[List[BusinessCriticality]] = None
    environment: Optional[List[Enviroment]] = None
    lifecycle: Optional[List[Lifecycle]] = None
    starting_after: Optional[str] = None
    ending_before: Optional[str] = None
    limit: Optional[int] = 10

    def to_dict(self) -> Dict[str, str]:
        return {
            f"{field}": f"{self._datatype_convert(value)}" for field, value in vars(self).items() if value is not None
        }

    def _datatype_convert(self, value: Any) -> str:
        args = value.__args__
        inner_type = type(args[0])
        if inner_type == type(list):
            return ",".join(value)
        elif inner_type == type(dict):
            return ",".join([f"{key}:{value}" for key, value in value.items()])
        elif inner_type == type(bool):
            return str(value).lower()
        else:
            return str(value)
