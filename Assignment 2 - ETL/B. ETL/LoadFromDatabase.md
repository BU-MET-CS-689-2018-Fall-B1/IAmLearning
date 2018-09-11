# Load Data From Database

Make sure your PostgreSQL virtual machine and database are running.

## Initial test run

Run the script LoadFromDatabase.py

## Questions

*   What is the difference between stateInfo and datFrame?
*   Could we implement the `is_it_a_state` function more easily using datFrame?
*   What happens if we run `is_it_a_state` with something that is not a state abbreviation at all?

## Programming

*   Change is_it_a_state so that it will recognize either state name or state abbreviation
*   Change is_it_a_state so that it will report when it cannot find the state name or state abbreviation
*   Query the household_income table and look for any entries that are not listed as states; print out the state information, city, and zip code, and at the end report the total number of non-state entries
*   Run the program and save the output to the `Put your outputs here!` directory as usual

## Questions

*   How did you address not finding a state in the table?
*   Why did you choose the type of query that you did for the non-state household?
*   Why did you choose or not choose to use Pandas for the non-state household query?



