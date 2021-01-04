#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
from datetime import date

agencies = [{'name': 'City of Kirkland',
            'accepts_the_multi_item_daily_bot_pdr': True,
            'emails': ['PublicRecords@kirklandwa.gov']},
            {'name': 'NORCOM',
            'accepts_the_multi_item_daily_bot_pdr': True,
            'emails': ['records@norcom.org']},
            {'name': "King County Sheriff's Office",
            'accepts_the_multi_item_daily_bot_pdr': True,
            'emails': ['kimberly.petty@kingcounty.gov']},
            {'name': 'Kitsap 911',
            'accepts_the_multi_item_daily_bot_pdr': True,
            'emails': ['kitsap911_PDR@kitsap911.org']},
            {'name': 'Valley Communications Center',
            'accepts_the_multi_item_daily_bot_pdr': False,
            'emails': ['recordsrequest@valleycom.org']}]

for agency in agencies:
    if not agency['accepts_the_multi_item_daily_bot_pdr']:
        records_request = \
            """This is a public records request. You're getting this bot request and not the main one because your agency denied the main one for having multiple items. I request every retained electronic record/data created yesterday that is stored on a computer owned by the agency or its cloud vendors with its associated meta-data. The records/data is locatable because every file/database on a computer is findable with operating system and database query tools. For databases extract rows with yesterday's date in them. This is not a request for all of the agency's records. Just one day's worth of records.
        
I demand all records be electronically redacted. Absolutely do not print out or scan anything. Always redact Tim's social security number. It's on Muckrock no thanks to King County Prosecutor's Office.

Export listings to CSV files with redacted strings replaced by "*R*"

If no redaction required then release emails with meta-data using the MSG format. Redact emails in EML format. If an attachment has to be redacted then remove the binary code from the EML file and redact attachment via PDF or multimedia redactor. See https://superuser.com/questions/75581/how-to-save-a-mail-into-an-eml-file-with-outlook

No exemption log is wanted to reduce the effort involved in fulfilling the request. Do not add redaction exemption codes to save time.

Because I am a bot I can not use a portal such as GovQA and demand all responses be in text format not PDF/Word and that records be disclosed as zip files via email attachment or direct link to the zip file that doesn't require logging in (I have seen direct links that were generated with GovQA)"""
    else:
        records_request = \
            """This is a public records request. It is the same one that every PRA covered-entity in Washington State (see https://realtimclemans.com/my-epic-records-requests-bot-plan-and-proposal-for-over-hauling-washington-states-out-dated-public-records-act/) is receiving except those denying this request in its entirity. The request is generated by script by CollectorBot on behalf of https://dataabout.me and https://recordsbased.news. The data will not be used for commercial purposes. It will be posted on an open data portal for free to the public without ads with a notice that it is illegal to use dashcam and list of persons for commercial purposes.
 
This is one bot records request in a 24 hour period. Because I am a bot I can not use a portal such as GovQA and demand all responses be in text format not PDF/Word and that records be disclosed as zip files via email attachment or direct link to the zip file that doesn't require logging in (I have seen direct links that were generated with GovQA)


Export listings to CSV files with redacted strings replaced by "*R*"


I demand all records be electronically redacted. Absolutely do not print out or scan anything. Always redact Tim's social security number. It's on Muckrock no thanks to King County Prosecutor's Office.

If no redaction required then release emails with meta-data using the MSG format. Redact emails in EML format. If an attachment has to be redacted then remove the binary code from the EML file and redact attachment via PDF or multimedia redactor. See https://superuser.com/questions/75581/how-to-save-a-mail-into-an-eml-file-with-outlook

* Every already electronic with meta-data record received by or created by Toby Nixon after December 20, 2020. See https://recordsbased.news/dinosaur-toby-nixon-a-republican-kirkland-washington-council-member-president-of-the-the-washington-coalition-for-open-government-said-you-will-be-shut-down-mark-my-words-lets-prove-him-wron/
* For each year data is available for your Fire/EMS agency's CARES Utstein Survival Report, note DC FEMS published their's at https://fems.dc.gov/page/cardiac-arrest and Evrett published their 2018 report at https://everettwa.gov/DocumentCenter/View/20541/Everett-Fire-2018-CARES-Summary-and-Utstein-Survival-Report
* For yesterday for city attorney's office [if you're a city] or county prosecutor's office [if you're a county]: All cases charged yesterday with all already-electronic investigative records
* For yesterday the police/FIRE/EMS 911 text log, dispatch events, remarks, and individual unit dispatch tables exported to CSV with redacted strings replaced by "*R*"
* For yesterday all police reports, accident reports, citations from all departments including code enforcement and law enforcement
* The complete computer aided dispatch, records management system, SECTOR [State Patrol only, and all SECTOR data from all contributing agencies], 911 and radio audio recorder, 911 call data system, digital evidence management already existing SQL databases exported to CSV files with redacted strings reeplaced by "*R*"
* Active warrants list exported to CSV with redacted strings replaced by "*R*" and photos with identifier to tied to the textual data
* Complete adult jail bookings related database tables exported to CSV with redacted strings replaced by "*R*"
* All already-electronic investigative records involving Timothy Clemans or 11448 12th ave sw Burien WA, 98146 or 14431 58TH AVE S Tukwila WA
* All already-electronic investigative records for all swatting, DUIs, violent crimes, child abuse, and sexual crimes, police chases that occured on or after December 29, 2020
* Yesterday's already electronic misconduct investigative records for all departments
* The IAPro SQL database exported to CSV with redacted strings replaced by "*R*"
* All courts' SQL data exported CSV with redacted strings replaced by "*R*"
* Yesterday's public records requests, communications with meta-data about records requests, and released records
* For yesterday: SMS/text messages with meta-data of all executive staff and PIOs (see https://www.ecamm.com/mac/phoneview/ and https://www.nickshertzer.com/?p=1768) to CSV with redacted strings replaced by "*R*"
* All listings of employee data and associated listings exported to CSV with redacted strings replaced by "*R*" For each redacted person I request their last email, see "do not include work product created by the agency employee as part of his or her official duties." https://app.leg.wa.gov/RCW/default.aspx?cite=42.56.660
* Axon SQL database for all products your agency uses. There's a lot of data they aren't providing via the report downloads page like audit trail data
* All automatic license plate reader textual data exported to CSV with redacted strings replaced by "*R*"
* All police automatic vehicle location data 30 minutes after start of shift to 30 minutes before ending of shift and excluding the time responding to or at a dispatch event to 10 minutes after the event
* All internet history logs with full urls exported to CSV with redacted strings replaced by "*R*"
* All records indexes
* All already electronic policies and training documents
* All business license records in a SQL database exported to CSV with redacted strings replaced by "*R*"
* All ID badges from the ID badge database and all electronic photos with meta-data of all employees
* All SQL database tables with employee data exported to CSV with redacted strings replaced by "*R*"
* Yesterday's already electronic court documents
* Meta-data for every email exported to CSV with redacted strings replaced by "*R*"
* Yesterday's already electronic records for all building permit requests
* All real estate SQL data exported to CSV with redacted strings replaced by "*R*"
* Yesterday's emails with meta-data to and from PIOs
* The marriage records database exported to CSV with redacted strings replaced by "*R*"
* From State of Washington SOS: All voter registration SQL data exported to CSV with redacted strings replaced by "*R*"
* AXON evidence created log and AXON evidence sharing log exported to CSV with redacted strings replaced by "*R*"
* Every email with meta-data about CollectorBot or Collector Bot or Timothy Clemans or Tim Clemans or RecordsBased.news or DataAbout.me and NCIC/ACCESS data and audit trail for queries of Timothy Clemans DOB 7/19/1990.

No exemption log is wanted to reduce the effort involved in fulfilling the request. Do not add redaction exemption codes to save time.

"""
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    request = requests.post('https://api.mailgun.net/v3/%s/messages'
                            % os.getenv('API_EMAIL_DOMAIN_NAME'),
                            auth=('api', '%s'
                            % os.getenv('MAILGUN_API_KEY')), data={
        'from': 'CollectorBot <collectorbot@dataabout.me>',
        'to': agency['emails'] + ['collectorbot@dataabout.me'],
        'subject': 'For %s For %s Daily CollectorBot Records Request' 
            % (today, agency['name']),
        'text': 'For %s\n\nDear %s,\n%s' % (today, agency['name'], records_request),
        }).text
    print(request)
