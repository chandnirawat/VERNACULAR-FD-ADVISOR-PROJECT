def chatbot_reply(message):
    message = message.lower()

    if "fd" in message:
        return "FD is a safe investment where you earn fixed interest."
    elif "interest" in message:
        return "Interest depends on bank and duration."
    elif "risk" in message:
        return "Low risk = SBI, High return = Axis."
    else:
        return "I can help you with FD, interest, and banks."