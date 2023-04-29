import random
from flask import jsonify, request as flask_req
from giphy_client.rest import ApiException

from ChatGIFPT import create_app
from ChatGIFPT.gif_generator import search_gifs
from ChatGIFPT.text_analyzer import analyze_text

app = create_app()


@app.route("/search-gif", methods=["POST"])
def handle_search_gif():
    print(flask_req.form)
    query_text = flask_req.form["text"]
    if len(query_text) > 500:
        return jsonify({"response_type": "in_channel", "text": "Query is too long"})
    if len(query_text) > 50:
        query_text = analyze_text(query_text)
    try:
        gifs = [r.to_dict() for r in search_gifs(query_text, 1)]
        gif_url = random.choice(gifs).get("images", {}).get("original", {}).get("webp")
        if gif_url is None:
            return jsonify(
                {
                    "response_type": "in_channel",
                    "text": "No gif available for the given query",
                }
            )
    except ApiException as e:
        return jsonify(
            {
                "response_type": "in_channel",
                "text": f"Failed to search gif due to Query Too Long",
            }
        )
    except Exception as e:
        return jsonify(
            {
                "response_type": "in_channel",
                "text": f"Failed to search gif due to {str(e)}",
            }
        )
    return jsonify(
        {
            "response_type": "in_channel",
            "text": "Here's the image you requested:",
            "attachments": [{"fallback": "Image", "image_url": gif_url}],
        }
    )


def main(request):
    if request.method == "POST":
        if request.path == "/search-gif":
            return handle_search_gif()
        else:
            return jsonify({"error": "Invalid API endpoint"})
    else:
        return jsonify({"error": f"Unsupported HTTP type {request.type} endpoint"})
