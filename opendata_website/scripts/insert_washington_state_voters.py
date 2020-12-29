import sys
import json
from ..app import db

with open(sys.argv[1], 'r') as f:
    voters = json.loads(f.read())
for voter in voters:
        voter_rows = WashingtonStateVoter(state_voter_id = voter["state_voter_id"], fname = voter["fname"], mname = voter["mname"], lname = voter["lname"], name_suffix = voter["name_suffix"], birthdate = voter["birthdate"], gender = voter["gender"], reg_st_num = voter["reg_st_num"], reg_st_frac = voter["reg_st_frac"], reg_st_name = voter["reg_st_name"], reg_st_type = voter["reg_st_type"], reg_unit_type = voter["reg_unit_type"], reg_st_pre_direction = voter["reg_st_pre_direction"], reg_st_post_direction = voter["reg_st_post_direction"], reg_st_unit_num = voter["reg_st_unit_num"], reg_city = voter["reg_city"], reg_state = voter["reg_state"], reg_zip_code = voter["reg_zip_code"], county_code = voter["county_code"], precinct_code = voter["precinct_code"], precinct_part = voter["precinct_part"], legislative_district = voter["legislative_district"], congressional_district = voter["congressional_district"], mail = voter["mail"], mail_city = voter["mail_city"], mail_zip = voter["mail_zip"], mail_state = voter["mail_state"], mail_country = voter["mail_country"], registrationdate = voter["registrationdate"], absentee_type = voter["absentee_type"], last_voted = voter["last_voted"], status_code = voter["status_code"])
        db.session.commit()