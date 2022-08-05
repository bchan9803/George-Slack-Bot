# Library
import os

# For date/time
from datetime import datetime

# For Slack Bolt
from pyexpat.errors import messages

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient()

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Env variables´
from dotenv import load_dotenv
load_dotenv()


# Main
botToken = os.environ.get("SLACK_BOT_TOKEN")
appToken = os.environ.get("SLACK_APP_TOKEN")

app = App(token=botToken)

owner_user_id = "U03QHATV9M0" # user ID for DM


# App function
@app.event("member_joined_channel")
def welcome_msg(event, say):
    user = event["user"]
    say(f"*Hi <@{user}>!*")

    app.client.chat_postMessage(
        channel=user,
        text = f"Hi <@{user}>! 😁\n\nWelcome to the channel!\n\nI am George, America's favorite beaver, who also happens to be the facilitator of this channel. 🇺🇸❤️\n\n\nHere is a helpful guide for some of the functions included in this text channel:\n\n1) `;help` - Use this command followed by your question, so that the channel owner can quickly come to assist you. ✋\n2) `;time` - This command will trigger the current date and time. ⏰ \n3) `;happy bday` - Use this command to send someone in the chat a nice b-day GIF! 🎁 🥳\n4) `;beaver` - A easter egg that sends a GIF of \"George the Beaver\" from Duck Dynasty. 🦆 \n6) `;happy` - Posts a happy face GIF to express your happiness! 😊 \n7) `;thumbs up` - Agree with someone? Use the Phil Robertson iconic \"thumbs up\" GIF to display your agreement. 👍 \n8) `;homie` - Feel the need to display your inner Uncle Si? Use this command to display his iconic quote, \"Homie don't play that\". 🦆🙅‍♂️ \n\n\nForgot the commands? Use the `;guide` command to display the command list. \n\n\nPlease use the `;help` command if you have any questions! \n\n\n - George the Beaver"
    )


@app.message(";guide") # Guide which shows EVERY accessible command
def guide(message, say):
    say(f"Here is a helpful guide for some of the functions included in this text channel: \n\n\n1) `;help` - Use this command followed by your question, so that the channel owner can quickly come to assist you. ✋\n2) `;time` - This command will trigger the current date and time. ⏰ \n3) `;happy bday` - Use this command to send someone in the chat a nice b-day GIF! 🎁 🥳\n4) `;beaver` - A easter egg that sends a GIF of \"George the Beaver\" from Duck Dynasty. 🦆 \n6) `;happy` - Posts a happy face GIF to express your happiness! 😊 \n7) `;thumbs up` - Agree with someone? Use the Phil Robertson iconic \"thumbs up\" GIF to display your agreement. 👍 \n8) `;homie` - Feel the need to display your inner Uncle Si? Use this command to display his iconic quote, \"Homie don't play that\". 🦆🙅‍♂️ \n\n\nForgot the commands? Use the `;guide` command to display the command list. \n\n\nPlease use the `;help` command if you have any questions! \n\n\n - George the Beaver")
    #


@app.message(";help")  # Help finder
def help_finder(message, say, client):
    user = message["user"]
    copied_msg = message["text"]
    say(text = f"*<@{user}>, help is on the way!*")

    # Current time of when the message was sent
    currTime = datetime.now()
    currTime = currTime.strftime("%m/%d/%Y | %H:%M:%S")

    app.client.chat_postMessage(
        channel=owner_user_id,
        text = f"------------------------------------------------------------------------------------------------ \n❓❓*ASSISTANCE NEEDED*❓❓ \n\n\n<@{user}> is in need of assistance!  \n\n*Original Message:*\n\n{copied_msg} \n\n*Date and Time:* \n{currTime} \n------------------------------------------------------------------------------------------------"
    )


@app.message("copy")  # Cheater detector ("copy")
def cheater_detector(message, client):
    user = message["user"]
    copied_msg = message["text"]

    # Current time of when the message was sent
    currTime = datetime.now()
    currTime = currTime.strftime("%m/%d/%Y | %H:%M:%S")

    app.client.chat_postMessage( 
        channel=owner_user_id,
        text = f"------------------------------------------------------------------------------------------------ \n⚠️⚠️ *CHEATER DETECTED* ⚠️⚠️ \n\n\n*Original Message:* \n{copied_msg} \n\n*Alleged Cheater:* \n<@{user}> \n\n*Date and Time:* \n{currTime} \n------------------------------------------------------------------------------------------------"
    )
    
    # ONLY TO BE USED FOR PRESENTATION
    app.client.chat_postMessage(
        main_channel_id = "C03QANGL43Y",
        channel=main_channel_id,
        text = f"⚠️⚠️ *CHEATER DETECTED* ⚠️⚠️"
    )


@app.message(";time") # Current time command
def curr_Time(message, say):
    # Current time of when the message was sent
    currTime = datetime.now()
    currTime = currTime.strftime("%m/%d/%Y | %H:%M:%S")

    say(f"Here is the date and time: \n\n{currTime}.")


@app.message(";happy bday")  # Happy bday GIF
def happy_bday(message, say):
    say(
        f"https://georgebottest-zoc9376.slack.com/files/U03QHATV9M0/F03T95AGD24/happy-bday.gif"
    )    


@app.message(";beaver")  # George the Beaver GIF
def beaver(message, say):
    say(
        f"https://georgebottest-zoc9376.slack.com/files/U03QHATV9M0/F03RNK7U718/george-the-beaver.gif"
    )


@app.message(";happy") # Happy face GIF
def happy_face(message, say):
    say(
        f"https://georgebottest-zoc9376.slack.com/files/U03QHATV9M0/F03SKB6HZ4K/happy.gif"
    )


@app.message(";thumbs up") # Phil Robertson (Duck Dynasty) GIF
def thumbs_up(message, say):
    say(
        f"https://georgebottest-zoc9376.slack.com/files/U03QHATV9M0/F03SMU86SH2/phil-thumbs-up.gif"
    )


@app.message(";homie") # Uncle Si Robertson (Duck Dynasty) "Homie don't play that" GIF
def homie_egg(message, say):
    say(
        f"https://georgebottest-zoc9376.slack.com/files/U03QHATV9M0/F03SCSZP4NS/si-homie.gif"
    )



# App starter
if __name__ == "__main__":
    handler = SocketModeHandler(app, appToken)
    handler.start()
