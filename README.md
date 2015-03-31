##Goal:
    I want to make a command line application that generates pickup lines.
    
##Files that matter:
    - pickup-line-generator/main.py
    - pickup-line-generator/sql/test.db
    
    These are the only files that are needed for the pickup line generator are the
    two files mentioned above. All other files were either used for practice,
    creating the database, or for filling the database. 
    
##Why build this?
    My girlfriend is going away for the weekend and I would like to give
    her a gift before she goes. I think she will get a kick out of this!
    
##Dependencies
---
#####To recreate the project from the beginning then the project is needed:
    pdfminer: http://www.unixuser.org/~euske/python/pdfminer/index.html

#####If you just want to use the generator, then python 2.7 is the only dependency needed.

##Run Generator
---
###Directly run:
    python main.py
###Create an alias:
    alias pickupline="python path/to/project/main.py"
    
###Command line Interface:
    python main.py -h
    
    usage: pickupline [-h]
                  [-c | --add_pickupline ADD_PICKUPLINE | --add_comeback ADD_COMEBACK]

    A pickup line generator

    optional arguments:
      -h, --help            show this help message and exit
      -c, --comeback        Prints a comeback line to the screen.
      --add_pickupline ADD_PICKUPLINE
                               Allows you to add a pickup line to the database.
      --add_comeback ADD_COMEBACK
                               Allows you to add a comeback line to the database.

This project was built for my girlfriend (Jovanna Teran)
    
##Resources:
    Pickup lines source: http://www.howtocharmagirl.com/wp-content/uploads/2013/07/Pick-Up-Lines.pdf
    
##License:
    The MIT License (MIT)

    Copyright (c) <2015> <crazcalm>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
 