from flask import Flask, request, redirect
import user_agent
URL_1 = "https://github.com/EricPanDev/SillyRepository/blob/main/bait.png?raw=true"
URL_2 = "https://github.com/EricPanDev/SillyRepository/blob/main/real_image.png?raw=true"

app = Flask(__name__)

# Define the user agent string for Discord's bot
discord_user_agent = "Discordbot"

# Variable to track the bot's access count
bot_access_count = 0

@app.route('/')
def redirect_bot():
    global bot_access_count  # Declare bot_access_count as a global variable

    # Get the user agent from the request headers
    user_agent_string = request.headers.get('User-Agent', '')

    # Check if the user agent matches Discord's bot user agent
    if user_agent.is_bot(user_agent_string, discord_user_agent):
        bot_access_count += 1  # Increment the bot's access count

        # Redirect to https://google.com on the first visit, and https://bing.com on the second visit
        if bot_access_count % 2 == 1:
            return redirect(URL_1, code=302)
        else:
            return redirect(URL_2, code=302)

    else:
        # Redirect to the Rickroll URL for human users
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
