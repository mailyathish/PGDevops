"""
Generate PDF reports from data included in several Pandas DataFrames
From pbpython.com
"""
from __future__ import print_function
import pandas as pd
import numpy as np
import argparse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def create_pivot(df, infile, index_list=["Manager", "Rep", "Product"], value_list=["Price", "Quantity"]):
    """
    Create a pivot table from a raw DataFrame and return it as a DataFrame
    """
    table = pd.pivot_table(df, index=index_list, values=value_list,
                           aggfunc=[np.sum, np.mean], fill_value=0)
    return table

    