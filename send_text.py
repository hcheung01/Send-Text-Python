from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACdeb1efd67b86298a6fcf22849e3c86dd"
# Your Auth Token from twilio.com/console
auth_token  = "16b668707f5781975b53ffd98fd9a2a5"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+14156880153",
    from_="+14159933577",
    body="I miss you N")

print(message.sid)
