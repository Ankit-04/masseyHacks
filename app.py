from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import directions as map



def get_reply(message):
    
    message = message.lower()
    reply_text = ""

    if "route" and "from" in message:
        removal_list = ["route ","from "]
    
        for word in removal_list:
            message = message.replace(word, "")
        message = message.split()
        origin = message[0]
        destination = message [1]
        return map.get_directions(origin,destination)
    
    else:
        reply_text = "sorry please use enter you starting point and how long you want to route to be"

        return reply_text




app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    
    message_body = request.form['Body']
    resp = MessagingResponse()


    reply_text = get_reply(message_body)
    print(reply_text)
    
    resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    #Use for production
    app.run(debug=True)


