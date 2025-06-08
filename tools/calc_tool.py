# tools/calc_tool.py
from langchain_experimental.tools.python.tool import PythonREPLTool

def get_calc_tool():
    return PythonREPLTool(name="calculator", description="Useful for performing math or Python code.")

