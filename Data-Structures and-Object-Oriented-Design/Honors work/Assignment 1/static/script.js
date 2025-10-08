async function add(direction) {
  const value = document.getElementById('inputValue').value.trim();
  if (!value) {
    alert('Enter a value first!');
    return;
  }

  const response = await fetch('/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ value, direction })
  });

  const data = await response.json();
  updateDeque(data.items);
  document.getElementById('inputValue').value = '';
}

async function removeItem(direction) {
  const response = await fetch('/remove', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ direction })
  });

  const data = await response.json();
  if (data.removed === null) {
    alert('Deque is empty!');
  } else {
    alert(`Removed: ${data.removed}`);
    updateDeque(data.items);
  }
}

function updateDeque(items) {
  const container = document.getElementById('dequeContainer');
  container.innerHTML = ''; // clear
  items.forEach(item => {
    const div = document.createElement('div');
    div.className = 'deque-item';
    div.textContent = item;
    container.appendChild(div);
  });
}