import os
from twilio.rest import Client

account_sid = "AC05dd38f1795b184957244034bb648cfe"
auth_token = "0d0c5d838f1724ba6b50f16152480718"

client = Client(account_sid, auth_token)

call = client.calls.create(
    url = "https://handler.twilio.com/twiml/EH870d3ec69eb6e82e0cde221bdae46157",
    to = "+34 678 87 36 89",
    from_ = "+18474613533"
    )

