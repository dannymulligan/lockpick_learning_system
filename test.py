#!/usr/bin/env python3

import SVG_locks
import csv
import sys

supported_diagrams = ["plastic_cut_sheet_a", "plastic_cut_sheet_b", "paper_cut_sheet", "lock_diagrams", "logo_sheets"]

input_filename = "example_locks.csv"
with open("example_locks.csv") as file:
    reader = csv.reader(file)
    csv_lines = [(n+1,row) for (n,row) in enumerate(reader)]

pages = dict()
#sys.exit()
for line in csv_lines:
    (line_number, (diagram_type, output_filename, page_size, name, lock_configuration, show_key)) = line
    if diagram_type not in supported_diagrams:
        continue

    if ((diagram_type == "plastic_cut_sheet_a") or (diagram_type == "plastic_cut_sheet_b")) and \
       (page_size != "12x12"):
        print("Error: {}, line {} - {} output files only support \"12x12\" page size".format(input_filename, line_number, diagram_type))
        sys.exit(0)

    if output_filename in pages:
        if pages[output_filename][0]["page_size"] != page_size:
            print("Error: {}, line {} - all content in an output files must use the same page size".format(input_filename, line_number))
            print("    \"{}\" and \"{}\".".format(pages[output_filename][0]["page_size"], page_size))
            sys.exit(0)

        if (pages[output_filename][0]["diagram_type"] == "lock_diagrams") and (len(pages[output_filename]) > 8):
            print("Error: {}, line {} - lock_diagram output files cannot have more than 9 lock diagrams per output page".format(input_filename, line_number))
            sys.exit(0)

        if (diagram_type == "plastic_cut_sheet_a") or \
           (diagram_type == "plastic_cut_sheet_b") or \
           (diagram_type == "paper_cut_sheet"):
            print("Error: {}, line {} - {} output files cannot have more than one diagram per output page".format(input_filename, line_number, diagram_type))
            sys.exit(0)

        pages[output_filename].append({"diagram_type": diagram_type, "page_size": page_size, "name": name, "lock_configuration":lock_configuration, "show_key": show_key })
    else:
        pages[output_filename] = [{"diagram_type": diagram_type, "page_size": page_size, "name": name, "lock_configuration":lock_configuration, "show_key": show_key }]


for output_filename in pages:
    page = pages[output_filename]
    pagesize = page[0]["page_size"]
    diagram_type = page[0]["diagram_type"]
    print("Writing {} to output file {}".format(diagram_type, output_filename))

    if  diagram_type  == "plastic_cut_sheet_a":
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(SVG_locks.plastic_cut_sheet(pagesize="12x12", kind=diagram_type, page_title=output_filename, indent=1))
            SVG_file.write(SVG_locks.SVG_root(kind="end"))

    elif diagram_type == "plastic_cut_sheet_b":
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(SVG_locks.plastic_cut_sheet(pagesize="12x12", kind=diagram_type, page_title=output_filename, indent=1))
            SVG_file.write(SVG_locks.SVG_root(kind="end"))

    elif diagram_type == "paper_cut_sheet":
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(SVG_locks.paper_sheet([], kind="cut", page_title=output_filename, alignment=True, pagesize=pagesize, indent=1))
            SVG_file.write(SVG_locks.SVG_root(kind="end"))

    elif diagram_type == "lock_diagrams":
        configs = []
        for config in page:
            configs.append( (config["lock_configuration"], config["show_key"] == "yes", config["name"]) )
        with open(output_filename, "w") as SVG_file:
            SVG_file.write(SVG_locks.SVG_root(kind="start", pagesize=pagesize))
            SVG_file.write(SVG_locks.paper_sheet(configs, kind=diagram_type, page_title=output_filename, alignment=False, pagesize=pagesize, indent=1))
            SVG_file.write(SVG_locks.SVG_root(kind="end"))

    elif page["diagram_type"] == "logo_sheets":
        print("Error: {}, line {} - logo_sheets not implemented".format(input_filename, line_number))
        sys.exit(0)
