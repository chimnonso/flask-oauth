import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


from flask import Flask, redirect, url_for,render_template
from flask_dance.contrib.google import make_google_blueprint, google


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

google_bp = make_google_blueprint(client_id='276049735207-kg431dbhs7cn9d0iiq71076tg2c87b23.apps.googleusercontent.com', client_secret='uzSbPYgJYTdoGyvWqZYyJBbe', offline=True, scope=['profile', 'email'])
app.register_blueprint(google_bp, url_prefix='/login')


# @app.route('/')
# def index():
#    return render_template('home.html')


# @app.route('/welcome')
# def welcome():
#     resp = google.get("/oauth2/v1/userinfo")
#     assert resp.ok, resp.text
#     email = resp.json()["email"]
#     return render_template('welcome.html', email=email)


# @app.route('/login/google')
# def login():
#     if not google.authorized:
#        return render_template(url_for('google.login'))
#     resp = google.get("/oauth2/v1/userinfo")
#     assert resp.ok, resp.text
#     email = resp.json()["email"]
    
#     return redirect(url_for('welcome'))


@app.route('/')
def index():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return f"You are {email} on Google"
    

if __name__ == "__main__":
    app.run()