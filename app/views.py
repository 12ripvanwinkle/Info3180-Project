"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, send_from_directory, request, jsonify, send_file, session, Flask
import os
from .models import User, Profile, Favourite 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, current_user, login_required
from flask_jwt_extended import create_access_token

###
# Routing for your application.
###

# Ensure your app is configured with the upload folder

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# for this I used form-data and not raw->json in postman
@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/assets/<path:filename>')
def assests(filename):
     return send_from_directory(os.path.join(app.static_folder, "assets"), filename)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    upload_dir = app.config['UPLOAD_FOLDER']
    print("🔍 CONFIGURED UPLOAD_FOLDER =", upload_dir)

    # Print out the parent directories to see where things actually are:
    def list_dir(path):
        try:
            return os.listdir(path)
        except Exception as e:
            return f"<error: {e}>"

    project_src = os.getcwd()
    app_dir     =  os.path.join(project_src, 'app')
    static_dir  = os.path.join(app_dir, 'static')

    print("📂 project/src contents:", list_dir(project_src))
    print("📂 app/ contents:",      list_dir(app_dir))
    print("📂 app/static contents:", list_dir(static_dir))
    print("📂 app/static/uploads contents:", list_dir(upload_dir))

    return send_from_directory(os.path.join(app.static_folder, "uploads"), filename)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

@app.route('/api/register', methods=['POST'])
def register_user():
    # Get user form fields
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    email = request.form.get('email')
    photo = request.files.get('photo')

    # Check all required fields
    if not all([username, password, name, email, photo]):
        return jsonify({'error': 'All fields are required.'}), 400

    # Check for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 409
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists.'}), 409

    # Save photo
    photo = request.files.get('photo')
    if photo.filename == '' or not allowed_file(photo.filename):
        return jsonify({'error': 'Invalid or missing photo file.'}), 400

    filename = secure_filename(photo.filename)
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    photo.save(photo_path)


    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create user
    new_user = User(
        username=username,
        password=hashed_password,
        name=name,
        email=email,
        photo=filename
    )

    # Commit to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.', 'id': new_user.id}), 201

# For this i used raw->json in postman
@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username','').strip()
        password = data.get('password','').strip()

        # Verify if both fields were filled
        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400
        
        # Look up user in the database
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            # Successful login
            login_user(user)
            return jsonify({
                'message': 'Login successful',
                'token': access_token,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'name': user.name,
                    'photo': user.photo
                }
            }), 200
        else:
            # Failed login
            return jsonify({'error': 'Invalid credentials'}), 401
        
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

# For this nothing really needed to inserted in postman, just send a post request to the endpoint
@app.route('/api/auth/logout', methods=['POST'])
@login_required
def handle_logout():
    logout_user()  # ← This now correctly refers to flask_login.logout_user
    return jsonify({'message': 'Logged out successfully'}), 200

# For this i used raw->json in postman
@app.route('/api/profiles', methods=['POST'])
@login_required
def create_profile():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['description', 'parish', 'biography', 'sex', 'race', 'birth_year', 'height',
                           'fav_cuisine', 'fav_colour', 'fav_school_subject',
                           'political', 'religious', 'family_oriented']
        
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}'}), 400
        
        # Check how many profiles this user already has
        profile_count = Profile.query.filter_by(user_id_fk=current_user.id).count()
        if profile_count >= 3:
            return jsonify({'error': 'You can only create up to 3 profiles.'}), 400
        
        # Create profile
        profile = Profile(
            user_id_fk=current_user.id,
            description=data['description'],
            parish=data['parish'],
            biography=data['biography'],
            sex=data['sex'],
            race=data['race'],
            birth_year=int(data['birth_year']),
            height= data['height'],
            fav_cuisine=data['fav_cuisine'],
            fav_colour=data['fav_colour'],
            fav_school_subject=data['fav_school_subject'],
            political=bool(data['political']),
            religious=bool(data['religious']),
            family_oriented=bool(data['family_oriented'])
        )

        db.session.add(profile)
        db.session.commit()

        return jsonify({
            'message': 'Profile created successfully',
            'profile': {
                'id': profile.id,
                'user_id': profile.user_id_fk,
                'description': profile.description,
                'parish': profile.parish,
                'biography': profile.biography,
                'sex': profile.sex,
                'race': profile.race,
                'birth_year': profile.birth_year,
                'height': profile.height,
                'fav_cuisine': profile.fav_cuisine,
                'fav_colour': profile.fav_colour,
                'fav_school_subject': profile.fav_school_subject,
                'political': profile.political,
                'religious': profile.religious,
                'family_oriented': profile.family_oriented
            }
        }), 201

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    try:
        profiles = Profile.query.all()
        results = []

        for profile in profiles:
            user = User.query.get(profile.user_id_fk)
            results.append({
                'id': profile.id,
                'user_id': profile.user_id_fk,
                'user_name': user.name,
                'user_photo': user.photo,
                'description': profile.description,
                'parish': profile.parish,
                'biography': profile.biography,
                'sex': profile.sex,
                'race': profile.race,
                'birth_year': profile.birth_year,
                'height': profile.height,
                'fav_cuisine': profile.fav_cuisine,
                'fav_colour': profile.fav_colour,
                'fav_school_subject': profile.fav_school_subject,
                'political': profile.political,
                'religious': profile.religious,
                'family_oriented': profile.family_oriented
            })
        return jsonify({'profiles': results}), 200
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# same as the route above but for a specific profile
# for this just add this line in postman http://127.0.0.1:5000/api/profiles/1
@app.route('/api/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    try:
        profile = Profile.query.get(profile_id)

        if not profile:
            return jsonify({'error': 'Profile not found'}), 404
        user = User.query.get(profile.user_id_fk)
        profile_data = {
            'id': profile.id,
            'user_id': profile.user_id_fk,
            'user_name': user.name,                     
            'user_photo': user.photo,
            'description': profile.description,
            'parish': profile.parish,
            'biography': profile.biography,
            'sex': profile.sex,
            'race': profile.race,
            'birth_year': profile.birth_year,
            'height': profile.height,
            'fav_cuisine': profile.fav_cuisine,
            'fav_colour': profile.fav_colour,
            'fav_school_subject': profile.fav_school_subject,
            'political': profile.political,
            'religious': profile.religious,
            'family_oriented': profile.family_oriented
        }

        return jsonify(profile_data), 200

    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

@app.route("/api/profiles/<int:user_id>/favourite", methods=["POST"])
@login_required
def add_favourite(user_id):
    try:
        user_id_fk = current_user.id
        favourite_user_id_fk = user_id
        favourite = Favourite(user_id_fk=user_id_fk, fav_user_id_fk=favourite_user_id_fk)
        db.session.add(favourite)
        db.session.commit()
        return jsonify({'message': 'Favourite added successfully'}), 201

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500    
    
@app.route("/api/profiles/matches/<int:profile_id>", methods=["GET"])
def get_profile_matches(profile_id):
    try:
        profile = Profile.query.get(profile_id)
        if profile is None:
            return jsonify({'error': 'Profile not found'}), 404
        
        profile_name = profile.user.name
        profile_birth_year = profile.birth_year
        profile_sex = profile.sex
        profile_race = profile.race

        profiles =  Profile.query.join(User).filter(
            (User.name == profile_name ) if profile_name else True,
            (Profile.birth_year == profile_birth_year) if profile_birth_year else True,
            (Profile.sex == profile_sex ) if profile_sex else True,
            (Profile.race ==profile_race) if profile_race else True
        ).all()

        found_profiles = []
        for match in profiles:
            found_profiles.append({
                'id': match.id,
                'user_id': match.user_id_fk,
                'description': match.description,
                'parish': match.parish,
                'biography': match.biography,
                'sex': match.sex,
                'race': match.race,
                'birth_year': match.birth_year,
                'height': match.height,
                'fav_cuisine': match.fav_cuisine,
                'fav_colour': match.fav_colour,
                'fav_school_subject': match.fav_school_subject,
                'political': match.political,
                'religious': match.religious,
                'family_oriented': match.family_oriented
            })
        return jsonify(found_profiles), 200
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    


@app.route("/api/search", methods=["GET"])
def search():
    name = request.args.get('name')
    birth_year = request.args.get('birth_year')
    sex = request.args.get('sex')
    race = request.args.get('race')

    if not name and not birth_year and not sex and not race:
        return jsonify({'error': 'No search parameters provided'}), 400

    filters = []

    if name:
        filters.append(User.name == name)
    if birth_year:
        filters.append(Profile.birth_year == birth_year)
    if sex:
        filters.append(Profile.sex == sex)
    if race:
        filters.append(Profile.race == race)

    query = Profile.query.join(User).filter(*filters).all()

    found_profiles = []
    for profile in query:
        user = User.query.get(profile.user_id_fk)
        found_profiles.append({
            'id': profile.id,
            'user_id': profile.user_id_fk,
            'user_name': user.name,                     
            'user_photo': user.photo,
            'description': profile.description,
            'parish': profile.parish,
            'biography': profile.biography,
            'sex': profile.sex,
            'race': profile.race,
            'birth_year': profile.birth_year,
            'height': profile.height,
            'fav_cuisine': profile.fav_cuisine,
            'fav_colour': profile.fav_colour,
            'fav_school_subject': profile.fav_school_subject,
            'political': profile.political,
            'religious': profile.religious,
            'family_oriented': profile.family_oriented
        })
    return jsonify(found_profiles), 200

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'photo': user.photo
        }

        return jsonify(user_data), 200

    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500


@app.route("/api/users/<int:user_id>/favourites", methods=["GET"])
def get_user_favourites(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        favourites = Favourite.query.filter_by(user_id_fk=user_id).all()
        favourites_user_data = []
        for favourite in favourites:
            fav_user = User.query.get(favourite.fav_user_id_fk)
            favourites_user_data.append({
                'id': fav_user.id,
                'name': fav_user.name,
                'email': fav_user.email,
                'password': fav_user.password,
                'photo': fav_user.photo
            })

        return jsonify(favourites_user_data), 200
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500
    
@app.route("/api/users/favourites/<int:N>", methods=["GET"])
def most_favourite_users(N):
    try:
        users = db.session.query(User).\
        join(Favourite, User.id == Favourite.fav_user_id_fk).\
        group_by(User.id).\
        order_by(db.func.count(Favourite.id).desc()).\
        limit(N).\
        all()
        users_data = []
        for user in users:
            users_data.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password,
                'photo': user.photo,
            })

        return jsonify(users_data), 200
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500



###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response