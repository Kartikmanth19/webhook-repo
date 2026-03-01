from flask import Blueprint, request, jsonify
from models import events_collection
from datetime import datetime

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def github_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json

    timestamp = datetime.utcnow()

    if event_type == "push":
        author = payload["pusher"]["name"]
        to_branch = payload["ref"].split("/")[-1]

        # Prevent duplicatas
        existing = events_collection.find_one({
            "type": "PUSH",
            "author": author,
            "to_branch": to_branch,
            "timestamp": {"$gte": timestamp}
        })

        if not existing:
            events_collection.insert_one({
                "type": "PUSH",
                "author": author,
                "to_branch": to_branch,
                "timestamp": timestamp
            })

    elif event_type == "pull_request":
        action = payload["action"]
        pr = payload["pull_request"]

        author = pr["user"]["login"]
        from_branch = pr["head"]["ref"]
        to_branch = pr["base"]["ref"]

        if action == "closed" and pr["merged"]:
            event_type_db = "MERGE"
        else:
            event_type_db = "PULL_REQUEST"

        events_collection.insert_one({
            "type": event_type_db,
            "author": author,
            "from_branch": from_branch,
            "to_branch": to_branch,
            "timestamp": timestamp
        })

    return jsonify({"message": "Stored"}), 200


@webhook_bp.route("/events", methods=["GET"])
def get_events():
    # fetch last 60 sec events
    time_window = datetime.utcnow().timestamp() - 60

    events = list(events_collection.find().sort("timestamp", -1).limit(20))

    formatted_events = []

    for event in events:
        event["_id"] = str(event["_id"])
        event["timestamp"] = event["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")
        formatted_events.append(event)

    return jsonify(formatted_events)    