from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts=[]
@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    new_contact = {
        "name": request.form['name'],
        "phone": request.form['phone'],
        "email": request.form['email'],
        "address": request.form['address']
    }
    contacts.append(new_contact)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return render_template('search.html', contacts=results, query=query)

@app.route('/update_contact/<string:name>', methods=['GET', 'POST'])
def update_contact(name):
    contact = next((c for c in contacts if c['name'] == name), None)
    if request.method == 'POST':
        contact["phone"] = request.form['phone']
        contact["email"] = request.form['email']
        contact["address"] = request.form['address']
        return redirect(url_for('index'))
    return render_template('update_contact.html', contact=contact)

@app.route('/delete_contact/<string:name>')
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
