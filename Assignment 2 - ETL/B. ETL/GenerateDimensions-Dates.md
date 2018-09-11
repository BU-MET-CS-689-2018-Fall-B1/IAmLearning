# Generate Dimensions - Dates

Open up the file DateGen.py and inspect.

## Initial Questions
Put these into your word processing document

*   What do the arguments to the `gendates` function mean?
*   What is the granularity of the date dimension (as we start)?
*   What is the format of the date "key"
*   What are the formats of the date hierarchies?

## Programming Steps

1. Add a (calendar) quarter value to the dimension hierarchy
2. Extend the dimension to include all hours of each day
3. Count up the number of date keys that you create
4. Use cs689_utils to log each dimension record you generate for the first hour of each first day of the month
5. After all the date values have been generated, report the number of rows generated using the cs689_utils log function
3. Save the modified python script
3. Demonstrate dimension generation with a 
dimension lengths of at least 400 days, passing over a leap day (in a leap year), capturing the output in a file
4.  Demonstrate generation of two more runs of at least 400 days, capturing outputs into two separate files

## Final Questions

*   How did you format your additional hierarchy levels and why?
*   Why did you change Python code the way you did?
