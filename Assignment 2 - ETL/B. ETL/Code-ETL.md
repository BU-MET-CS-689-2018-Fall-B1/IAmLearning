# Extract-Transform-Load

You will find a file `Energy Census and Economic Data US 2010-2014.csv` in the Google drive Datasets folder.  You will use this for your information.

This is an open-ended assignment.

Use this `Energy Census and Economic Data US 2010-2014.csv` file in a Python program to generate a locations dimension with a hierarchy for region and division.  Store this dimension table in the database under any schema.

Correlate this with the information in the table `us_national_statistics.person_economic_info` and store the person info into a new fact table with the following attributes:

* person count
* location_dimension key
* age
* marital status
* income
* wireless
* internet
* own_smartphone
* read_newspapers

We have a 'person count' attribute because you will aggregate the `person_economic_info` data with one entry for each 5 years of age.

The code should use cs689_utils to report progress every 30-50 rows via logging.

The code should include logic to drop the dimension output table if it exists, then create a new one.  Similarly with the fact table.

Count the number of entries made into the database.

Devise one query against the resulting tables that you think is interesting.

# Questions

* what does the resulting table tell us?
* what programming choices did you make and why?
* what does your query tell us?
