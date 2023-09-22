from flask import Flask, request, render_template_string, redirect
import user_agent

URL_1 = "https://github.com/EricPanDev/SillyRepository/blob/main/bait.png"
URL_2 = "https://github.com/EricPanDev/SillyRepository/blob/main/real_image.png"

app = Flask(__name__)

# Define the user agent string for Discord's bot
discord_user_agent = "Discordbot"

# Variable to track the bot's access count
bot_access_count = 0

@app.route('/')
def serve_image_preview():
    global bot_access_count  # Declare bot_access_count as a global variable

    # Get the user agent from the request headers
    user_agent_string = request.headers.get('User-Agent', '')

    # Check if the user agent matches Discord's bot user agent
    if discord_user_agent in user_agent_string:
        print("disco bot")
        bot_access_count += 1  # Increment the bot's access count

        # Determine which image URL to use based on the bot's access count
        image_url = URL_1 if bot_access_count % 2 == 1 else URL_2

        # Generate an HTML response with an image preview
        html_response = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Image Preview</title>
        </head>
        <body>
            <h1>Image Preview</h1>
            <img src="{image_url}" alt="Image Preview">
        </body>
        </html>
        """

        return html_response

    else:
        # Redirect to the Rickroll URL for human users
        print("rickroll")
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
