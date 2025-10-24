import sys
import os
import importlib.machinery
import importlib.util

base_dir = os.path.dirname(os.path.abspath(__file__))
exact_dir = os.path.join(base_dir, "ExactInvariants")

# Add both base and module folder to sys.path
sys.path.insert(0, base_dir)
sys.path.insert(0, exact_dir)

# Load main.pyc manually (as if it were a source file)
pyc_main = os.path.join(exact_dir, "main.pyc")
loader = importlib.machinery.SourcelessFileLoader("main", pyc_main)
spec = importlib.util.spec_from_loader("main", loader)
main_mod = importlib.util.module_from_spec(spec)
loader.exec_module(main_mod)
