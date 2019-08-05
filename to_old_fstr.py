# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python [conda env:datalab]
#     language: python
#     name: conda-env-datalab-py
# ---

import re

# +
# filename = 'pydtk/pydtk/pydtk.py'
# out_filename = 'new_pydtk.py'
#filename = 'pydtk/pydtk/ptc/ptc.py'
#out_filename = 'new_ptc.py'

pattern_base = re.compile('^([^\'"]*)f[\'"]([^\'"]*)[\'"]([^\'"]*?)\n$')
pattern_string = re.compile('{.*?}')
pattern_prefix = re.compile('{(.*?)(?:\:[^:\]]*?)?}')
pattern_sufix = re.compile('{.*?(\:[^:\]]*?)?}')

# -

with open(filename) as infile:
    with open(out_filename, 'w') as outfile:
        for line in infile:
            if pattern_base.match(line):
                
                variables = []
                pre, main, post = pattern_base.match(line).groups()
                if post == '' or post[-1] != '\n':
                    post += '\n'
                for cell in pattern_string.findall(main):
                    variables.append(pattern_prefix.match(cell).group(1))
                    main = main.replace(cell, '{{{}}}'.format(pattern_sufix.match(cell).group(1) or ''))
                line = '{}\'{}\'.format({}){}'.format(pre, main, ', '.join(variables), post)
                
            outfile.write(line)
