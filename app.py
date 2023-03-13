from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('Select * from jobs'))
  result_all = result.all()
  jobs = [u._asdict() for u in result_all]
  return jobs


@app.route("/")
def hellow_world():
  jobs = load_jobs_from_db
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
