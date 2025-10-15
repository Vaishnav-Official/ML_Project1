# It's a common place for functionalities where entire function of the Project can be imported from 
# It is a common Python file in ML projects that contains utility/helper functions used across multiple modules.
# Purpose: A centralized file for reusable functions that don't belong to any specific component but are needed everywhere.
# Think of it as: Your project's toolbox 🧰

import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException


# Create a function to save path object
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)