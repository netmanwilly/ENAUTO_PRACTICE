import json
import MERAKI_Request

#Send GET request to sandbox to retrieve list of networks in organization

def getNetwork(meraki: object, org_id: str):
    RESPONSE = meraki.get(f'/organizations/{org_id}/networks')
    return RESPONSE




if __name__ == "__main__":
    MERAKI = MERAKI_Request.Meraki("https://api.meraki.com/api/v1", 'ccb3f4e44b2d75881d1471fcfa9a823149e69a9c', False)
    output = getNetwork(MERAKI, '549236')
    print(json.dumps(output, indent=2))

