from flask import Flask
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Just Scores</title>
        <meta charset="UTF-8">
	<meta http-equiv="refresh" content="60">
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
            }

            h1 {
                font-size: 40px;
            }

            .game {
                border: 1px solid #ddd;
                padding: 20px;
                margin: 15px 0;
                border-radius: 8px;
            }

            .score {
                font-size: 24px;
                font-weight: bold;
            }

            .status {
                margin-top: 10px;
                color: #666;
            }
        </style>
    </head>

    <body>

    <h1>JUST SCORES</h1>
    <h2>College Football</h2>
    """

    for event in data["events"]:

        competition = event["competitions"][0]
        teams = competition["competitors"]

        team1 = teams[0]["team"]["displayName"]
        score1 = teams[0]["score"]

        team2 = teams[1]["team"]["displayName"]
        score2 = teams[1]["score"]

        status = event["status"]["type"]["description"]

        html += f"""
        <div class="game">
            <div class="score">{team1} {score1}</div>
            <div class="score">{team2} {score2}</div>
            <div class="status">{status}</div>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)
