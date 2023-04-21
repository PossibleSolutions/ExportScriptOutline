# ExportScriptOutline
Goes through a Python (.py) or a Jupyter Notebook (.ipynb) script and exports all the commented lines and markdown texts to a text file called "ScriptComments_summary.txt". It is generated into the same folder as the input script.

Use it to quickly generate a script outline/summary and to spectate if your script has sufficient descriptions about what it does. It should work as a standalone general description about what your script does, if not, consider further comments and markdown cells.

Example output
<br>\*\*\*Imports\*\*\* (markdown cells are indicated in this way)
<br>\*\*\*Inputs\*\*\*
<br>\*\*\*Processing\*\*\*
<br>#this part does x
<br>#here the part x is further aggregated to y by z...
<br>\*\*\*Outputs\*\*\*
<br>#heres some visualization and stats
<br>#change output path


Additional credits:
<br>-Syke
<br>-ChatGPT
