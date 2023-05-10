import pywhatkit


def send():

    # read data from data file
    # write phone number and whatsapp message in data.txt file
    with open('data.txt', 'r') as f:
        data = f.readlines()
    number = data[0]
    msg = data[1]
    pywhatkit.sendwhatmsg_instantly(number, msg)


# call the driver function
send()
