import os
import pkgutil
import importlib
from .base_spell import BasePriestSpells

# Get the directory name of the current package
pkg_dir = os.path.dirname(__file__)

# Import each module in our current directory
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    importlib.import_module('.' + name, __package__)

# Since each priest spells class is a subclass of BasePriestSpells, I can
# build a dictionary of all classes, in all modules, in this package
priest_spells = {cls.__name__: cls for cls in BasePriestSpells.__subclasses__()}
