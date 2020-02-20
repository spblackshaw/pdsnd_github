# Bikeshare Project

### Date created
2/7/2020

### Description
This repository houses an interactive Python program for viewing statistics from a bikeshare company for 3 US cities. Users are able to run the program and view statistics on different segments of the bikeshare company subscribers/customers for a particular city. They can then view the actual raw bikeshare data for the city selected. 

**How does it work?**
* Users will need Python installed; the project was written with [Python 3.7.4](https://www.python.org/downloads/release/python-374/)
* Running the executable Python script [bikeshare.py](docs/bikeshare.py) will lead the user through the interactive program with prompts.
* The [local_function.py](docs/local_functions.py) file houses additional functions necessary for running the main [bikeshare.py](docs/bikeshare.py) script.
    * The data files have been added to the .gitignore file so they aren't uploaded to the project.



### Files used
* bikeshare.py
* local_functions.py
* chicago.csv
* new_york_city.csv
* washington.csv

### Credits
**These sources were used for reference during development of the program:**
* http://effbot.org/zone/stupid-exceptions-keyboardinterrupt.htm
* https://stackoverflow.com/questions/53037698
* https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python
* https://stackoverflow.com/questions/19112735/how-to-print-a-list-of-tuples-with-no-brackets-in-python
* https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python
* https://stackoverflow.com/questions/17995024/how-to-assign-a-name-to-the-a-size-column
* https://stackoverflow.com/questions/53163469/how-to-rename-column-after-pandas-groupby-size
* https://smallbusiness.chron.com/making-raw-input-lowercase-python-31840.html
* https://stackoverflow.com/questions/35277075
* https://stackoverflow.com/questions/35277075/python-pandas-counting-the-occurrences-of-a-specific-value
* https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
* https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
* https://stackoverflow.com/questions/9943504/right-to-left-string-replace-in-python 	
* https://www.geeksforgeeks.org/precision-handling-python/
* https://stackoverflow.com/questions/51519178/pandas-dataframe-hist-doesnt-work
* https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
* Use of iloc instead of loc in local_functions.view_data() after project reviewer recommendation.
* Handled possibility of missing additional columns in datasets using test of column's existence on project reviewer's recommendation.
    * Original was hard-coded to account for current status of particular dataset .
