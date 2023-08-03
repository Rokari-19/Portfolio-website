from flask import Flask, render_template, url_for, jsonify 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
JOBS = [
    {
        'id':1, 
        'title':'Backend developer',
        'location':'Abuja, Nigeria',
        'salary':'n1000000',
        'member': 'Ajiri "rokari" iyelobu',
        'github': 'https://github.com/rokarioss'
    }, 
    {
        'id':2, 
        'title':'Data Scientist',
        'location':'Abuja, Nigeria',
        'salary':'n1000000',
        'member': 'anosike ugochukwu'
    },
    {
        'id':3, 
        'title':'Front End Engineer',
        'location':'Uke, Nigeria',
        'salary':'n1000000',
        'member': 'Daniel "kng-koder" fori',
        'github': 'https://github.com/DFori'

    },
    {
        'id':4, 
        'title':'Fullstack Developer',
        'location':'remote',
        'salary':'$200000',
        'member': 'Aigbona Benjamin "bencool"',
        'github':'https://github.com/aigbonabenjamin'
    }
    
]
@app.route('/')

def index():
    return render_template('landing.html',
     jobs= JOBS,
     company_name= 'Code-crusaders'
     )


@app.route('/jobs')
def list_jobs():



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)