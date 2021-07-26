"""Dexter-Register

Raises:
    AttributeError: Module could not find the (class | function) you are looking for.

"""
from importlib import import_module, resources

PLUGINS = dict()

filter_names = lambda apps: [
    # Filter names that do not start with "___" from {module}.__dir__() list.
    cls_or_def
    for cls_or_def in apps
    if not cls_or_def.startswith("__") and cls_or_def not in ["register"]
]


def group(*items) -> dict:
    """Return dict of all of the registered (classes & functions)"""
    dexter_lib = dict()
    for app in items:
        allowed = filter_names(app.__dir__())
        for name in allowed:
            module_name = f"""{ app.__name__ }.{ name }"""
            active = getattr(app, name)
            allowed_2 = filter_names(dir(active))
            for name_2 in allowed_2:
                the_name = f"{module_name}.{name_2}"
                the_action = getattr(active, name_2)
                dexter_lib[the_name] = the_action
    return dexter_lib


def get_keys(*items) -> list:
    """Get all of the available (classes & functions)"""
    dexter_lib = list()
    for app in items:
        for package in filter_names(app.__dir__()):
            module_name = f"""{ app.__name__ }.{ package }"""
            active = getattr(app, package)
            for module in filter_names(dir(active)):
                the_name = f"{module_name}.{module}"
                dexter_lib.append(the_name)
    return dexter_lib


def register(func):
    """Decorator to register plug-ins"""
    name = func.__name__
    PLUGINS[name] = func
    return func


def __getattr__(name):
    """Return a named plugin"""
    try:
        return PLUGINS[name]
    except KeyError:
        _import_plugins()
        if name in PLUGINS:
            return PLUGINS[name]
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None


def __dir__():
    """List available plug-ins"""
    _import_plugins()
    return list(PLUGINS.keys())


def _import_plugins():
    """Import all resources to register plug-ins"""
    for name in resources.contents(__name__):
        if name.endswith(".py"):
            import_module(f"{__name__}.{name[:-3]}")
