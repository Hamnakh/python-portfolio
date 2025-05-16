from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')

mail = Mail(app)

# Sample projects data
PROJECTS = [
    {
        'title': 'Resume',
        'description': 'A full-stack editable resume.',
        'image': 'resume1.jpg',
        'github': 'https://github.com/Hamnakh/Milestone-5',
        'demo': 'https://milestone-5-gray-delta.vercel.app/'
    },
    {
        'title': 'Blog App',
        'description': 'A real-time task management application with team collaboration features.',
        'image': 'blog2.jpg',
        'github': 'https://github.com/yourusername/project2',
        'demo': 'https://web-b-three.vercel.app/'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            msg = Message('New Portfolio Contact',
                        sender=email,
                        recipients=[os.getenv('EMAIL_USER')])
            msg.body = f"""
            From: {name}
            Email: {email}
            Message: {message}
            """
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred. Please try again later.', 'error')
            
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 