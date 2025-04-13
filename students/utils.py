import requests

def capture_fingerprint() :
    secugen_url = "https://localhost:8443/SGIFPCapture"
    headers = {"Connection":"keep-alive", "Origin":"https://localhost"}
    response = requests.post(secugen_url, headers=headers, verify=False)
    return response

def verify_fingerprint(current_fingerprint, captured_fingerprint):
    secugen_url = "https://localhost:8443//SGIMatchScore"
    headers = {"Connection":"keep-alive", "Origin":"https://localhost"}
    response = requests.post(secugen_url, headers=headers, verify=False, data={"template1": current_fingerprint, "template2": captured_fingerprint})
    data = response.json()
    if not data.get('ErrorCode'):
        print(data)
        return data.get('MatchingScore') > 149
    print(data)
    return False