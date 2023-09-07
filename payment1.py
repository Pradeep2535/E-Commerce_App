import requests

def payment_link():
    url="https://test.cashfree.com/api/v1/order/create"
    payload={
        "appId" : "TEST100130263c1872d91b5b381916de62031001",
        "secretKey" : "TESTd6d22b1e806db0a28c11163efe327c430b620aa1",
        "orderId":"order_id_new_08959795479745363847548748857749712639178652545597850922514538",
        "orderAmount":"1",
        "orderCurrency":"INR",
        "orderNote":"Paying to seller",
        "customerName":"Dhakshitha",
        "customerEmail":"sec22ad096@sairamtap.edu.in",
        "customerPhone":"9710417608",
        "returnUrl":"https://cashfree.com"
        #"notifyUrl":


    }
    response = requests.request("POST",url,data=payload)
    if response.status_code==200:
        generated_url=response.json().get("paymentLink")
        if generated_url:
            return generated_url
        #else:
            return None
    #else:
        #print("Request to the payment gateway API failed with status code:", response.status_code)
     #   return None
url=str(payment_link())
print(url)

