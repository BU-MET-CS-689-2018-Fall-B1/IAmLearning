# Generate Dimensions - People

In the class datasets, you will find a file named 'titanic.csv'.  Make sure you have this available on your computer.  We will load it using `pandas`.

## Start

Open `LoadTitanic.py` and put the titanic file name into the variable.  Use a full path if needed.

Run the script and make sure it prints out the names of everyone on the Titanic.

## Questions

*   What is `pd`?
*   How can you find the names of the columns?
*   How can you find the number of rows?

## Programming

Generate a dimension for all the people on the Titanic.

Include the following attributes:

*   passenger name
*   passenger gender
*   passenger age if available
*   Rank

For "Rank", create a three-level hierarchy combining the "Pclass" and "Fare" attributes.  The Pclass is at the top, then the Fare divided by 3, then the Fare itself.

Put out a log message every 20 rows using cs689_utils.

At the end of the run, report the number of entries.

## Verification
Run the script and save its output to a file in the "Put your outputs here!" folder.

## Questions

*   Why did you program this the way you did?
*   How did you structure your "person key" and why?
