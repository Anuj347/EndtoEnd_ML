#any functinalities that we are writing in a common way which will be used in entire application
# for example read a dataset from a database I can create MongoClient overhere
#save model in the cloud

import os
import sys

import numpy as np
import pandas as pd
import dill #helps in creating a pickel file

from src.exception import CustomException

def save_object(file_path, obj):

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
