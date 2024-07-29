from enum import Enum

class MetaCount(Enum):
    ONLY = 'ONLY'


class BusinessCriticality(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    CRITICAL = 'critical'


class Enviroment(Enum):
    FRONTEND = 'frontend'
    BACKEND = 'backend'
    INTERNAL = 'internal'
    EXTERNAL = 'external'
    MOBILE = 'MOBILE'
    SAAS = 'saas'
    ONPREM = 'onprem'
    HOSTED = 'hosted'
    DISTRIBUTED = 'distributed'

class Lifecycle(Enum):
    PRODUCTION = 'production'
    DEVELOPMENT = 'development'
    SANDBOX = 'sandbox'