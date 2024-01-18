import MERAKI_Request
import json

def updateNetwork(meraki: object, URI):
    payload = '''
  {
    "id": "L_646829496481115495",
    "organizationId": "549236",
    "name": "NETMAN WILLYS NETWORK",
    "productTypes": [
      "appliance",
      "camera",
      "switch",
      "wireless"
    ],
    "timeZone": "America/Los_Angeles",
    "tags": [],
    "enrollmentString": null,
    "url": "https://n149.meraki.com/DNSMB4-wxxx4gmai/n/U995Sdvc/manage/usage/list",
    "notes": null,
    "isBoundToConfigTemplate": false
  }


'''
    return meraki.put(URI, payload)

def getNetwork(meraki: object, URI):
    return meraki.get(URI)


if __name__ == "__main__":
    meraki = MERAKI_Request.Meraki('https://n149.meraki.com/api/v1', 'ccb3f4e44b2d75881d1471fcfa9a823149e69a9c', False)
    print(json.dumps(updateNetwork(meraki, '/networks/L_646829496481115495')))
    print(json.dumps(getNetwork(meraki,'/networks/L_646829496481115495')))
