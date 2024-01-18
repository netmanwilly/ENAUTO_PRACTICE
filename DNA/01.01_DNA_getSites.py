import json
import DNA_Request
from pprint import pprint

#CODE SAMPLE TO GET SITES USING SELF MADE SDK

#GET SITES CONFIGURED ON DNA OBJECT
def getSites(DNA: object):
    output = DNA.get('/dna/intent/api/v1/site')

    return output


#GET SITE HEALTH FOR ALL SITES
def getSiteHealth(DNA: object):
    output = DNA.get('/dna/intent/api/v1/site-health')
    return output


if __name__ == '__main__':
    BASE_URI = "https://sandboxdnac2.cisco.com"
    USER = "devnetuser"
    PASS = "Cisco123!"
    
    DNA = DNA_Request.DNA_Request(BASE_URI, USER, PASS, False)
#    pprint(getSites(DNA), indent=2)
    pprint(getSiteHealth(DNA), indent=2)
    