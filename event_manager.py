from flask import Flask, render_template, request
from models  import Event, db
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)




@app.route('/')
def index():
    db.create_all()
    return render_template('index.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_time_str = request.form['start_time']
        print(start_time_str)
        end_time_str = request.form['end_time']
        
        try:
            start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            event = Event(title=title, description=description, start_time=start_time, end_time=end_time)
            
            db.session.add(event)
            db.session.commit()
            return 'Event created successfully!'
        except ValueError:
            return 'Invalid date format. Please use YYYY-MM-DD HH:MM.'
    else:
        return render_template('create_event.html')

@app.route('/view_events')
def view_events():
    "TODO"


@app.route('/delete_event', methods=['GET', 'POST'])
def delete_event():
    "TODO"

if __name__=="__main__":
    app.run(debug=True)