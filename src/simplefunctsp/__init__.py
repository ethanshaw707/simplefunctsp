# read version from installed package
from importlib.metadata import version
__version__ = version("simplefunctsp")

print(f"Importing {__name__}")
print(f"Current Version {__version__}")
from .add_numbers import *
from .template_package import *