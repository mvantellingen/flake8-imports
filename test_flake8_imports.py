
from flake8_imports import ImportsPlugin

def test_integration():
    ImportsPlugin.parse_options(None)
    obj = ImportsPlugin(None, 'flake8_imports.py')
    obj.run()
