from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class ListNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList4:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        if self._head is None:
            return None
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head is None:
            return None
        if self._head is self._tail:
            return self.removefirst()
        currentnode = self._head
        while currentnode.link is not self._tail:
            currentnode = currentnode.link
        item = self._tail.data
        self._tail = currentnode
        self._tail.link = None
        self._length -= 1
        return item

    def __len__(self):
        return self._length

    def to_list(self):
        """Helper method to convert linked list into a Python list"""
        items = []
        current = self._head
        while current:
            items.append(current.data)
            current = current.link
        return items


# --- Flask setup ---
deque = LinkedList4()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    value = data.get('value')
    direction = data.get('direction')

    if direction == 'front':
        deque.addfirst(value)
    else:
        deque.addlast(value)

    return jsonify({'items': deque.to_list()})

@app.route('/remove', methods=['POST'])
def remove():
    data = request.json
    direction = data.get('direction')

    removed = deque.removefirst() if direction == 'front' else deque.removelast()
    return jsonify({'removed': removed, 'items': deque.to_list()})

if __name__ == '__main__':
    app.run(debug=True)
