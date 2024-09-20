from flask import Flask, request, render_template, jsonify
import openpyxl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])


def upload_file():
    file = request.files['file']
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    # Assuming the Excel sheet has these fields in the first row
    data = {
        'firstname': sheet['A2'].value,
        'surname': sheet['B2'].value,
        'age': sheet['C2'].value
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
