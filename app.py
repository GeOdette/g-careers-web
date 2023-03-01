from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data analyst',
  'location': 'Nairobi, Kenya',
  'salary': '10k'
}, {
  'id': 2,
  'title': 'Data scientist',
  'location': 'Limuru, Kenya',
}, {
  'id': 3,
  'title': 'Front end',
  'location': 'Kisumu, Kenya',
  'salary': '100k'
}, {
  'id': 4,
  'title': 'Backend',
  'location': 'Nakuru, Kenya',
  'salary': '10000k'
}]


@app.route("/")
def hellow_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
