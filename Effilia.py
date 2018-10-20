#!/bin/~python

#!/usr/bin/python

print """
Hello and welcome to esemds web hunter.
            ------------------------------
            --$$---$$--$$-----$$--$$$$$$--
            --$$---$$--$$$---$$$-----$$---
            --$$$$$$$--$$-$-$-$$----$$----
            --$$---$$--$$--$--$$---$$-----
            --$$---$$--$$-----$$--$$$$$$--
            ------------------------------
                                        V1.01.1
4 more type "-h" [help file].
"""

def bash():
    while True:
        in_info = str(raw_input(">>> "))
        key = in_info.upper()
        if key == "-H":
            print"""
            the help file 4 esemds web hunter.
            use these commands to find what U want.
            1. -a alpha trace kit.
            2. -c cosmos web king
            3. -f ferri trackback info gathering tool.
            4. -w the wang crack system.
            5. 00 to stop hunting.
            """
        elif key == "-A":
            alpha()
        elif key == "-C":
            print "\t    -c"
        elif key == "-F":
            print "\t    -f"
        elif key == "-W":
            print "\t    -w"
        elif key == "00":
            print "\t    U R Going out."
            break
        elif key =="":
            continue
        else :
            print "\t    ("+ key.lower()+") is not a valid command."

def alpha():
    print """
            This tool is a Trace kit.
            inter a target in [ip > command] format to do, 4 help type '-h'.
    """
    while True:
        in_alpha = str(raw_input("-> "))
        key_alpha = in_alpha.upper()
        
        if key_alpha == "-H":
            print """
            The help file 4 alpha Trace tool.
            1. -s to scan a target.
            2. -0 to back to main menu.
            """
        elif key_alpha == "-S":
            print "\t    The -s tool."
        elif key_alpha == "-0":
            print "\t    U R in main menu."
            bash()
            break
        elif key_alpha == "":
            continue
        else :
            print "\t    ("+ key_alpha.lower()+") is not a valid command."


bash()        
