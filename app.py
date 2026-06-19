from flask import Flask, request, jsonify
from queue import Queue
from threading import Thread
import time

app = Flask(__name__)

# Event Queue
event_bus = Queue()

# Processed events
events_processed = []


# ---------- Event Consumer ----------
def event_listener():

    while True:

        event = event_bus.get()

        print(
            f"Processing event: {event}"
        )

        time.sleep(2)

        events_processed.append(
            event
        )

        event_bus.task_done()


# Start listener
Thread(
    target=event_listener,
    daemon=True
).start()


# ---------- Publish Event ----------
@app.route(
    "/publish",
    methods=["POST"]
)
def publish():

    data = request.get_json()

    event_bus.put(
        data
    )

    return jsonify({
        "message":
        "Event published"
    })


# ---------- Queue Size ----------
@app.route("/events")
def events():

    return jsonify({
        "events_waiting":
        event_bus.qsize()
    })


# ---------- Processed Events ----------
@app.route("/processed")
def processed():

    return jsonify(
        events_processed
    )


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status":
        "healthy"
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )
