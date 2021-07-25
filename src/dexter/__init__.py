from importlib import import_module
from importlib import resources

PLUGINS = dict()

filter_names = lambda apps:  [ i for i in apps if not i.startswith("__") and i not in ['register'] ]

def group(*items) -> dict:
    DexterLib = dict()
    for app in items:
        allowed = filter_names(app.__dir__())
        for name in allowed:
            module_name = f'''{ app.__name__ }.{ name }'''
            active = getattr(app, name)
            allowed_2 = filter_names(dir(active))
            for name in allowed_2:
                the_name = f"{module_name}.{name}"
                the_action = getattr(active, name)
                DexterLib[the_name]=the_action
    return DexterLib

def get_keys(*items) -> list:
    DexterLib = list()
    for app in items:
        for package in filter_names(app.__dir__()):
            module_name = f'''{ app.__name__ }.{ package }'''
            active = getattr(app, package)
            for module in filter_names(dir(active)):
                the_name = f"{module_name}.{module}"
                DexterLib.append(the_name)
    return DexterLib
    
    
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
        else:
            raise AttributeError(
                f"module {__name__!r} has no attribute {name!r}"
            ) from None


def __dir__():
    """List available plug-ins"""
    _import_plugins()
    return list( PLUGINS.keys() )


def _import_plugins():
    """Import all resources to register plug-ins"""
    for name in resources.contents(__name__):
        if name.endswith(".py"):
            import_module(f"{__name__}.{name[:-3]}")
            