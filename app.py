from flask import Flask, render_template, Jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data analyst',
    'location': 'lagos, Nigeria',
    'salary': 'N.500,000'
  },
  {
    'id': 2,
    'title': 'web developer',
    'location': 'Abuja, Nigeria',
    'salary': 'N.800,000'
  },
 {
  'id': 3,
    'title': 'programmer',
    'location': 'lagos, Nigeria',
    'salary': 'N.400,000'
 },
 {
   'id': 4,
    'title': 'backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$1,000,000'
 } 
]

@app.route("/")
def hello_techboys():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name='techboys')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
