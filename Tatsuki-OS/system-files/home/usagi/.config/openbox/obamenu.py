#!/usr/bin/env python3

import os, shutil

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

f = open(os.path.expanduser('~')+'/.config/openbox/debian-menu.xml', 'r')
lines = len(f.readlines())
f.close()

shutil.copyfile(os.path.expanduser('~')+'/.config/openbox/debian-menu.xml', os.path.expanduser('~')+'/.config/openbox/obamenu.xml')
replace_line(os.path.expanduser('~')+'/.config/openbox/obamenu.xml', 1, '<openbox_pipe_menu>\n')
replace_line(os.path.expanduser('~')+'/.config/openbox/obamenu.xml', lines-1, '</openbox_pipe_menu>\n')

f = open(os.path.expanduser('~')+'/.config/openbox/obamenu.xml', 'r')
content = f.read()
print(content)
f.close()
