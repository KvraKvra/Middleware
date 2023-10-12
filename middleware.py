from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'mssql+pyodbc://<username>:<password>@<server>/<database>' with your SQL Server connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://<username>:<password>@<server>/<database>?driver=ODBC+Driver+17+for+SQL+Server'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))

@app.route('/api/data', methods=['POST'])
def add_data():
    try:
        data_content = request.json.get('content')

        new_data = Data(content=data_content)
        db.session.add(new_data)
        db.session.commit()

        return jsonify({'message': 'Data added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    try:
        data = Data.query.get(data_id)
        if data:
            db.session.delete(data)
            db.session.commit()
            return jsonify({'message': 'Data deleted successfully'}), 200
        else:
            return jsonify({'error': 'Data not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():  # Create an application context
        db.create_all()  # Create the database tables
    app.run(debug=True)