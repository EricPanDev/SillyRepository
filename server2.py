import io
from flask import Flask, request, send_file, redirect
import requests

URL_1 = "https://github.com/EricPanDev/SillyRepository/blob/main/bait.png?raw=true"
URL_2 = "https://github.com/EricPanDev/SillyRepository/blob/main/real_image.png?raw=true"

app = Flask(__name__)

# Dictionary to store downloaded images
downloaded_images = {}


bot_access_count = 0
def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_image(path):
    global bot_access_count
    user_agent_string = request.headers.get('User-Agent', '')

    if 1==1:
        # Check if the image is already downloaded, otherwise download it
        if URL_1 not in downloaded_images:
            downloaded_images[URL_1] = download_image(URL_1)

        if URL_2 not in downloaded_images:
            downloaded_images[URL_2] = download_image(URL_2)

        bot_access_count += 1

        # Serve the appropriate image based on the bot's access count
        if bot_access_count % 2 == 1:
            return send_file(io.BytesIO(downloaded_images[URL_2]), mimetype='image/png')
        else:
            return send_file(io.BytesIO(downloaded_images[URL_1]), mimetype='image/png')
    else:
        # Redirect to the Rickroll URL for human users
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
