import sys
import json
from ..app import db
from ..app import WashingtonStateVoter

with open(sys.argv[1], 'r') as f:
    voters = json.loads(f.read())
for voter in voters:
    voter = WashingtonStateVoter(state_voter_id = voter["StateVoterID"], fname = voter["FName"], mname = voter["MName"], lname = voter["LName"], name_suffix = voter["NameSuffix"], birthdate = voter["Birthdate"], gender = voter["Gender"], reg_st_num = voter["RegStNum"], reg_st_frac = voter["RegStFrac"], reg_st_name = voter["RegStName"], reg_st_type = voter["RegStType"], reg_unit_type = voter["RegUnitType"], reg_st_pre_direction = voter["RegStPreDirection"], reg_st_post_direction = voter["RegStPostDirection"], reg_st_unit_num = voter["RegStUnitNum"], reg_city = voter["RegCity"], reg_state = voter["RegState"], reg_zip_code = voter["RegZipCode"], county_code = voter["CountyCode"], precinct_code = voter["PrecinctCode"], precinct_part = voter["PrecinctPart"], legislative_district = voter["LegislativeDistrict"], congressional_district = voter["CongressionalDistrict"], mail1 = voter["Mail1"], mail2 = voter["Mail2"], mail3 = voter["Mail3"], mail4 = voter["Mail4"], mail_city = voter["MailCity"], mail_zip = voter["MailZip"], mail_state = voter["MailState"], mail_country = voter["MailCountry"], registrationdate = voter["Registrationdate"], absentee_type = voter["AbsenteeType"], last_voted = voter["LastVoted"], status_code = voter["StatusCode"])
    db.session.commit()