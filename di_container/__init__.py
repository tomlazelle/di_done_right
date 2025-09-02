"""
Python Dependency Injection Framework

A dependency injection framework inspired by .NET's DI container system.
"""

from .container import DIContainer, DIScope
from .registration import ServiceRegistration, ServiceRegistry
from .enums import ServiceLifetime, RegistrationStrategy
from .exceptions import (
    DIException,
    ServiceNotRegisteredException,
    CircularDependencyException,
    InvalidRegistrationException,
    ScopeException
)
from .service_provider import ServiceProvider, get_service, get_keyed_service, try_get_service

__version__ = "0.1.0"
__all__ = [
    "DIContainer",
    "DIScope",
    "ServiceRegistration",
    "ServiceRegistry",
    "ServiceLifetime",
    "RegistrationStrategy",
    "DIException",
    "ServiceNotRegisteredException",
    "CircularDependencyException",
    "InvalidRegistrationException",
    "ScopeException",
    "ServiceProvider",
    "get_service",
    "get_keyed_service",
    "try_get_service",
]
