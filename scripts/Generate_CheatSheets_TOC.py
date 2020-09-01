#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python3 script to generate the summary markdown page that is used
by GitBook to generate the offline website.

The summary markdown page is named "TOC.md" and is generated in the
same location that the script in order to be moved later by the caller script.
"""
import os

# Define templates
cs_md_link_template = "* [%s](cheatsheets/%s)"

# Scan all CS files
cheatsheets = [f.name for f in os.scandir("../cheatsheets") if f.is_file()]
cheatsheets.sort()

# Scan all comment files
comments = [f.name for f in os.scandir("../comments") if f.is_file()]
comments.sort()

# Scan all customization files
customizations = [f.name for f in os.scandir("../customizations") if f.is_file()]
customizations.sort()

# Scan all pocs files
pocs = [f.name for f in os.scandir("../pocs") if f.is_file()]
pocs.sort()

# Scan all CS files
tools = [f.name for f in os.scandir("../tools") if f.is_file()]
tools.sort()

# Generate the summary file
with open("TOC.md", "w") as index_file:
    index_file.write("# Summary\n\n")
    index_file.write("### Cheatsheets\n\n")
    index_file.write(cs_md_link_template % ("Index Alphabetical", "Index.md"))
    index_file.write("\n")
    index_file.write(cs_md_link_template % ("Index ASVS", "IndexASVS.md"))
    index_file.write("\n")
    index_file.write(cs_md_link_template % ("Index Proactive Controls", "IndexProactiveControls.md"))
    index_file.write("\n")
    index_file.write(cs_md_link_template % ("Index Comments", "IndexProactiveControls.md"))
    index_file.write("\n")
    index_file.write(cs_md_link_template % ("Index Customizations", "IndexProactiveControls.md"))
    index_file.write("\n")
    index_file.write(cs_md_link_template % ("Index POCs", "IndexProactiveControls.md"))
    index_file.write("\n")
    for cheatsheet in cheatsheets:
        if cheatsheet != "Index.md" and cheatsheet != "IndexASVS.md" and cheatsheet != "IndexProactiveControls.md" and cheatsheet != "TOC.md":
            cs_name = cheatsheet.replace("_"," ").replace(".md", "").replace("Cheat Sheet", "")
            index_file.write(cs_md_link_template % (cs_name, cheatsheet))
            index_file.write("\n")
    index_file.write("\n")
    for comment in comments:
        if comment != "Index.md" and comment != "IndexASVS.md" and comment != "IndexProactiveControls.md" and comment != "TOC.md":
            cs_name = comment.replace("_"," ").replace(".md", "").replace("Cheat Sheet", "")
            index_file.write(cs_md_link_template % (cs_name, cheatsheet))
            index_file.write("\n")
    index_file.write("\n")
    for customization in customizations:
        if customization != "Index.md" and customization != "IndexASVS.md" and customization != "IndexProactiveControls.md" and customization != "TOC.md":
            cs_name = customization.replace("_"," ").replace(".md", "").replace("Cheat Sheet", "")
            index_file.write(cs_md_link_template % (cs_name, cheatsheet))
            index_file.write("\n")
    index_file.write("\n")
    for poc in pocs:
        if poc != "Index.md" and poc != "IndexASVS.md" and poc != "IndexProactiveControls.md" and poc != "TOC.md":
            cs_name = poc.replace("_"," ").replace(".md", "").replace("Cheat Sheet", "")
            index_file.write(cs_md_link_template % (cs_name, cheatsheet))
            index_file.write("\n")
    index_file.write("\n")
    for tool in tools:
        if tool != "Index.md" and tool != "IndexASVS.md" and tool != "IndexProactiveControls.md" and tool != "TOC.md":
            cs_name = tool.replace("_"," ").replace(".md", "").replace("Cheat Sheet", "")
            index_file.write(cs_md_link_template % (cs_name, cheatsheet))
            index_file.write("\n")

print("Summary markdown page generated.")