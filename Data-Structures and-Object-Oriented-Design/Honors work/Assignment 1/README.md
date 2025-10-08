# Queue Visualizer (Flask + JavaScript)

This project is a simple Queue Visualizer built with Python (Flask) on the backend and JavaScript on the frontend.  
It shows how enqueue and dequeue operations work in real time — with smooth animations and an interactive interface.  
.

---

## What It Does

- Lets users add (enqueue) and remove (dequeue) items from a queue.
- Each action updates both the backend data and the frontend animation instantly.
- Uses a linked list implementation for the queue logic on the backend.
- Visual animations are powered by JavaScript and CSS transitions on the frontend.

---

## 🧩 Tech Stack

| Part | Technology |
|------|-------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Data Structure | Linked List Queue |

---

## 📁 Folder Structure

```
queue-visualizer/
│
├── app.py              # Flask backend (runs the server + defines routes)
├── linkedlist4.py      # LinkedList4 class for queue logic
│
├── templates/
│   └── index.html      # Frontend layout
│
├── static/
│   ├── style.css       # Styling and animation design
│   └── script.js       # Handles animation + communicates with Flask
│
└── README.md
```

---

## 🧠 How It Works

### Backend (Flask)
The backend stores the actual queue using a linked list.  
Each time you enqueue or dequeue, Flask updates the structure and sends the new queue back to the frontend.

Example:
```python
@app.route("/enqueue", methods=["POST"])
def enqueue():
    data = request.json["item"]
    queue.addlast(data)
    return jsonify({"status": "success"})
```

### Frontend (JavaScript)
The frontend uses fetch() to communicate with Flask.  
When the user performs an action, it sends a request to Flask, updates the queue, and triggers a smooth animation.

Example:
```js
function enqueue(item) {
  fetch("/enqueue", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ item })
  }).then(() => animateEnqueue(item));
}
```

---

## 💻 How to Run It

### 1. Clone the project
```bash
git clone https://github.com/your-username/queue-visualizer.git
cd queue-visualizer
```

### 2. Install dependencies
```bash
pip install flask
```

### 3. Run the server
```bash
python app.py
```

### 4. Open it in your browser
Go to 👉 http://127.0.0.1:5000/

---

## 🎨 Example Animation Flow

1. You click “Enqueue” →  
   Flask adds the item to the queue → JavaScript animates a new block sliding in.

2. You click “Dequeue” →  
   Flask removes the first item → JavaScript animates it moving out and disappearing.

The queue on screen always matches the one in Python.
