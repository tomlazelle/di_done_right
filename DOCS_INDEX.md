# Python Dependency Injection Framework - Documentation Index

Welcome to the complete documentation for the Python Dependency Injection Framework! This .NET-inspired DI system provides powerful dependency injection capabilities for Python applications.

## 📚 Documentation Structure

### 🚀 Getting Started
- **[README.md](README.md)** - Project overview, installation, and quick examples
- **[Quick Reference Guide](QUICK_REFERENCE.md)** - Concise reference for common patterns

### 📖 Comprehensive Guides
- **[Complete User Documentation](DOCUMENTATION.md)** - Full feature guide with detailed examples
  - Quick Start tutorial
  - Core concepts explanation
  - Service registration patterns
  - Lifetime management
  - Keyed services
  - Static container management
  - FastAPI integration
  - Advanced scenarios
  - Best practices
  - Troubleshooting guide

### 💻 Code Examples
- **[examples/basic_usage.py](examples/basic_usage.py)** - Basic DI container usage
- **[examples/advanced_usage.py](examples/advanced_usage.py)** - Advanced features (factories, instances)
- **[examples/concrete_types_usage.py](examples/concrete_types_usage.py)** - Concrete type registration
- **[examples/keyed_services_usage.py](examples/keyed_services_usage.py)** - Multiple implementations
- **[examples/static_container_usage.py](examples/static_container_usage.py)** - Global container management
- **[examples/fastapi_example.py](examples/fastapi_example.py)** - FastAPI integration
- **[examples/comprehensive_example.py](examples/comprehensive_example.py)** - Complete e-commerce system

## 🎯 Quick Navigation

### For First-Time Users
1. Start with **[README.md](README.md)** for project overview
2. Follow the **[Quick Reference Guide](QUICK_REFERENCE.md)** for immediate usage
3. Run **[examples/basic_usage.py](examples/basic_usage.py)** to see it in action

### For Detailed Learning
1. Read the **[Complete User Documentation](DOCUMENTATION.md)**
2. Study the **[comprehensive example](examples/comprehensive_example.py)**
3. Explore specific feature examples in the `examples/` directory

### For FastAPI Users
1. Review **[FastAPI Integration](DOCUMENTATION.md#fastapi-integration)** section
2. Run **[examples/fastapi_example.py](examples/fastapi_example.py)**
3. Study the API endpoints in **[comprehensive_example.py](examples/comprehensive_example.py)**

### For Advanced Users
1. Check **[Advanced Scenarios](DOCUMENTATION.md#advanced-scenarios)** section
2. Review **[Best Practices](DOCUMENTATION.md#best-practices)**
3. Explore keyed services and scoped lifetime examples

## 🏗️ Framework Architecture

```
di_container/
├── __init__.py          # Public API exports
├── container.py         # Core DI container implementation
├── service_provider.py  # Static container management
├── registration.py      # Service registration logic
├── enums.py            # Service lifetimes and constants
├── exceptions.py       # Custom exceptions
└── fastapi_integration.py  # FastAPI-specific utilities
```

## 🔧 Key Features Documentation

| Feature | Documentation | Example |
|---------|---------------|---------|
| **Basic DI** | [Core Concepts](DOCUMENTATION.md#core-concepts) | [basic_usage.py](examples/basic_usage.py) |
| **Service Lifetimes** | [Service Lifetimes](DOCUMENTATION.md#service-lifetimes) | [advanced_usage.py](examples/advanced_usage.py) |
| **Keyed Services** | [Keyed Services](DOCUMENTATION.md#keyed-services) | [keyed_services_usage.py](examples/keyed_services_usage.py) |
| **Static Container** | [Static Container](DOCUMENTATION.md#static-container-management) | [static_container_usage.py](examples/static_container_usage.py) |
| **FastAPI Integration** | [FastAPI Integration](DOCUMENTATION.md#fastapi-integration) | [fastapi_example.py](examples/fastapi_example.py) |
| **Concrete Types** | [Service Registration](DOCUMENTATION.md#service-registration-details) | [concrete_types_usage.py](examples/concrete_types_usage.py) |

## 📝 Development Resources

- **[Project Structure](README.md#structure)** - Codebase organization
- **[Testing](tests/)** - Unit tests and test examples
- **[Type Annotations](di_container/)** - Full type safety throughout
- **[Error Handling](DOCUMENTATION.md#troubleshooting)** - Common issues and solutions

## 🤝 Contributing

This project follows Python best practices with comprehensive testing, type annotations, and clear documentation. See the individual files for implementation details and contribution guidelines.

---

*Choose your path based on your needs and experience level. All documentation is designed to be self-contained while cross-referencing related concepts.*
