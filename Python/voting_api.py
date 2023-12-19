from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
candidates = [
    {"id": 1, "name": "Mariano Iglesias", "votes": 0},
    {"id": 2, "name": "Pedro Rajoy", "votes": 0},
    {"id": 3, "name": "Santiago Sanchez", "votes": 0},
    {"id": 4, "name": "Pablo Abascal", "votes": 0},
]
votes_cast = set()  # To keep track of users who have voted

@app.route("/candidates", methods=["GET"])
def get_candidates():
    return jsonify(candidates), 200

@app.route("/candidates", methods=["POST"])
def add_candidate():
    new_candidate = request.get_json()
    candidates.append({
        "id": len(candidates) + 1,
        "name": new_candidate["name"],
        "votes": 0
    })
    return jsonify(candidates), 201

@app.route("/vote/<int:candidate_id>", methods=["POST"])
def cast_vote(candidate_id):
    user_id = request.get_json().get("user_id")
    if user_id in votes_cast:
        return jsonify({"error": "User has already voted"}), 400
    candidate = next((c for c in candidates if c["id"] == candidate_id), None)
    if candidate:
        candidate["votes"] += 1
        votes_cast.add(user_id)
        return jsonify(candidate), 201
    return jsonify({"error": "Candidate not found"}), 404

@app.route("/results", methods=["GET"])
def get_results():
    return jsonify(candidates), 200

@app.route("/candidates/<int:candidate_id>", methods=["PUT"])
def update_candidate(candidate_id):
    candidate = next((c for c in candidates if c["id"] == candidate_id), None)
    if candidate:
        updated_data = request.get_json()
        candidate["name"] = updated_data.get("name", candidate["name"])
        return jsonify(candidate), 200
    return jsonify({"error": "Candidate not found"}), 404

@app.route("/candidates/<int:candidate_id>", methods=["DELETE"])
def delete_candidate(candidate_id):
    global candidates  # to modify the global variable
    candidate = next((c for c in candidates if c["id"] == candidate_id), None)
    if candidate:
        candidates = [c for c in candidates if c["id"] != candidate_id]  # Reassigning filtered list
        return jsonify({"message": "Candidate deleted"}), 200
    return jsonify({"error": "Candidate not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)