import cs689_utils
import psycopg2
import pandas

stateQuery = 'select numeric_id, us_state_terr, abbreviation, is_state from us_national_statistics.states'

connDB = psycopg2.connect("dbname=postgres user=postgres host=localhost port=56321 password=bitnami")

dbCur = connDB.cursor()

dbCur.execute(stateQuery)

stateInfo = dbCur.fetchall()

# declare a dictionary
stateIsState = {}

for thisState in stateInfo:
    print (thisState[2])
    stateIsState[thisState[2]] = thisState[3]
    stateIsState[thisState[1]] = thisState[3]

datFrame = pandas.read_sql(stateQuery, connDB)

for statename in datFrame.us_state_terr:
    print (statename)

def is_it_a_state(stateabbrv):
    if stateIsState[stateabbrv] == "State":
        return ("yes, " + stateabbrv + " is a state")
    else:
        return ("no, " + stateabbrv + " is not a state")
