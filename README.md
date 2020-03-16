# Creating earliest possible date from input
**Python script that**

* reads input.txt file

    * text file contain three numbers between 0 and 2999
    * numbers represent year, month and day in random order
    * number representing year may be truncated to two digits and in case the first one is 0, to just one digit
    * numbers may be zero padding
    * number are separated by "/"
    * there are no extra spaces around "/"

* outputs the earliest possible date between 2000-01-01 and 2999-12-31 created from given numbers
* if there is no possible date, returns input string with "is illegal" annotation

**Run**

To run this program:
* download date.py file
* create text file containing numbers in accordance with above-mentioned instructions
* in your terminal run `python date.py input.txt`, where `input.txt` is the name of your text file
