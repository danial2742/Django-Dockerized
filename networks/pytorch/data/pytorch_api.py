from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
	output_data = {
		"input_file": 'fasfa',
		"output_file": 'fasfa',
		"result": 'fasfa',
		"accuracy": 'fasfa',
		"runtime": 'fasfa',
	}

	return jsonify(output_data)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port="23000")