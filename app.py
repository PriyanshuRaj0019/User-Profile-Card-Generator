import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from models import db
from models.profile import Profile

app = Flask(__name__)

app.config["SECRET_KEY"] = "profile_card_secret_key"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_DIR, "database", "profile.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    return render_template("index.html")

@app.route("/create-profile", methods=["POST"])
def create_profile():

    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    occupation = request.form.get("occupation", "").strip()
    location = request.form.get("location", "").strip()
    email = request.form.get("email", "").strip()
    image_url = request.form.get("image_url", "").strip()
    bio = request.form.get("bio", "").strip()

    # ----------------------------
    # Validation
    # ----------------------------

    if not all([
        name,
        age,
        occupation,
        location,
        email,
        image_url,
        bio
    ]):

        flash("Please fill all fields.", "error")

        return redirect(url_for("home"))

    existing_user = Profile.query.filter_by(
        email=email
    ).first()

    if existing_user:

        flash(
            "Email already exists.",
            "error"
        )

        return redirect(url_for("home"))

    profile = Profile(

        name=name,

        age=int(age),

        occupation=occupation,

        location=location,

        email=email,

        image_url=image_url,

        bio=bio

    )

    db.session.add(profile)

    db.session.commit()

    flash(
        "Profile created successfully!",
        "success"
    )

    return redirect(
        url_for(
            "view_profile",
            profile_id=profile.id
        )
    )

@app.route("/profile/<int:profile_id>")
def view_profile(profile_id):

    profile = Profile.query.get_or_404(profile_id)

    return render_template(
        "profile.html",
        profile=profile
    )


if __name__ == "__main__":
    app.run(debug=True)
