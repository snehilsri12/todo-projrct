from flask import Flask, render_template, request, jsonify
import uuid, hashlib

app = Flask(_name_)

# Dummy storage list
items = []

@app.route('/')
def home():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    data = request.form

    # Generate ID, UUID, Hash
    item_id = len(items) + 1
    item_uuid = str(uuid.uuid4())
    item_hash = hashlib.sha256(data.get("itemName").encode()).hexdigest()

    item = {
        "itemID": item_id,
        "itemUUID": item_uuid,
        "itemHash": item_hash,
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }

    items.append(item)
    return jsonify({"message": "Item added successfully", "items": items})

if _name_ == '_main_':
    app.run(debug=True)
