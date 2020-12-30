import requests
import json

cookies = {
    '_ga': 'GA1.2.27880359.1605390918',
    'WCMS_ASP.NET_SessionId': 'jcgubncpna5ilc3vikoi3cxo',
    'nmstat': '82e8cad4-3ac8-aede-f0fd-79be8dfbbc99',
    '_ce.s': 'v11.rlc~1607629079154',
    '_gid': 'GA1.2.1775611456.1609248748',
    'ASP.NET_SessionId': 'v4rq1miwc43xcngxlwly30jk',
    'TS01d0cb72': '017eac8407e47623700499eb665c28ac241c35149a53e3907fa12ee95c301bca71e2e633e36959a987a3bbea7444dea95ff20b3015f9b9a70d7ae5d9764b87bedeab29f6be',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ingress.kingcounty.gov/Public/JILS/default.aspx',
    'Accept-Language': 'en-US,en;q=0.9',
}

response = requests.get('https://ingress.kingcounty.gov/Public/JILS/Default.aspx/GetEveryoneInCustody', headers=headers, cookies=cookies)

people = json.loads(response.json()['d'])['People']
print(people[0])