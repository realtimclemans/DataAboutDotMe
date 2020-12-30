# source ../dataaboutdotmekeys.sh;python3 -m opendata_website.scripts.insert_washington_state_voters /users/Tim/Desktop/code/wavoters/wavoters.json

import sys
import json
import re
from ..app import db
from ..app import WashingtonStateVoter

with open(sys.argv[1], 'r') as f:
    voters = json.loads(f.read())
for i in range(0, len(voters), 1000):    
    db.engine.execute(
        WashingtonStateVoter.__table__.insert(),
        [dict([('_'.join([x.lower() for x in re.findall('[A-Z]+[a-z0-9]*', key)]), voter[key]) for key in voter.keys()]) for voter in voters[i: i+1000]]
    )