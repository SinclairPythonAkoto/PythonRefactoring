from flask import Flask, render_template, request, redirect, url_for
from flask.views import View, MethodView

app = Flask(__name__)

# class view to direct user to enter their name
class Home(View):
    def dispatch_request(self):
        return render_template("homepage.html")

# method view to handle requests
class UserPage(MethodView):
    def get(self):
        return render_template("username.html")
    
    def post(self):
        user_name = request.form.get("userName")
        print(request.form)    # returns ImmutableMultiDict object with values from form
        return render_template("username.html", user_name=user_name)
        

app.add_url_rule(
    "/", view_func=Home.as_view(name="homepage")
)

app.add_url_rule(
    "/inputname", view_func=UserPage.as_view(name="inputname")
)

if __name__ == "__main__":
    app.run(debug=True)