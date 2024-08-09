"""
You can scape a special character by using \
For example:
\" -> scape double quote character
\' -> scape simple quote character
\\ -> scape backslash character
\n -> It is a line scape
"""
# \"
# \'
# \\
# \n -> line space

curso = "Ultimate\\Python -> \"Its great\""
curso2 = 'Ultimate\\Python -> \'Its great\''
curso3 = "Ultimate\nPython"

print(curso)  # Ultimate\Python -> "Its great"
print(curso2)  # Ultimate\Python -> 'Its great'
print(curso3)
