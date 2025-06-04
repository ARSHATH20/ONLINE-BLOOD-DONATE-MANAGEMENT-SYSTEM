from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_donor, add_request, get_inventory, get_requests

app = Flask(__name__)

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        address = request.form['address']
        add_donor(name, blood_group, contact, address)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/request', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        contact = request.form['contact']
        add_request(name, blood_group, contact)
        return redirect(url_for('index'))
    return render_template('request.html')

@app.route('/inventory')
def inventory():
    inventory = get_inventory()
    requests = get_requests()
    return render_template('inventory.html', inventory=inventory, requests=requests)

if __name__ == '__main__':
    app.run(debug=True)