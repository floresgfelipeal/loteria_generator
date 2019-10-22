# loteria_generator
Generator of Mexican Loteria Boards in PDF format.

You can create PDF files ready for printing of randomly generated boards for 
playing Mexican Loteria.

Requirements
------------

You need Python 3 to run this application.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, macOS and Windows, packages are available at

  http://www.python.org/getit/

Usage
-----------

    $ pip install -r requirements.txt
    $ python3 generator.py [-p | -l] [number_of_pages] [file_path] [title]

	Example:	
	
	$ python3 generator.py -p 15 loteria.pdf 'Mi Loteria' 
	
	Arguments:
	-h, --help       Shows a help message.
	-p, --portrait   It will create files in portrait orientation with one
	                 board per page.
	-l, --landscape  It will create files in landscape orientation with two
	                 boards per page.
	number_of_pages  Number of pages that the file will have. Min. 1. Max. 500
    	
					 
Built With
-----------
	
	