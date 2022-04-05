# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

from importlib import reload
reload(demographic_data_analyzer);


# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()