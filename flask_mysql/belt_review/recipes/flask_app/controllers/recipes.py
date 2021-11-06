from werkzeug import datastructures
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard_page():
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    data = {
            "id": session['user_id']
        }
    user = User.get_user_with_recipes(data)
    return render_template('dashboard.html', user=user)

@app.route('/recipes/new')
def new_recipe_page():
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    return render_template('add_recipe.html', user_id=session['user_id'])

@app.route('/recipes/new/save', methods=['POST'])
def save_recipe():
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    data = {
        "users_id": session['user_id'],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"]
    }
    recipe_id = Recipe.create(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    data = {
        "id": id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe_page(id):
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    data = {
        "id": id
    }
    recipe = Recipe.get_by_id(data)[0]
    print(recipe)
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/recipes/edit/<int:id>/save', methods=['POST'])
def save_edit(id):
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    data = {
        "id": id,
        "users_id": session['user_id'],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under_30": request.form["under_30"]
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def recipe_details_page(id):
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }

    user = User.get_user_by_id(user_data)[0]
    recipe = Recipe.get_by_id(data)[0]
    return render_template('recipe.html', recipe=recipe, user=user)

@app.route('/recipes/all')
def all_recipes_page():
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    all_recipes = Recipe.get_all()
    recipes = []
    for recipe in all_recipes:
        recipe = Recipe(recipe)
        recipe.get_likes()
        recipes.append(recipe)
    print(recipes)

    return render_template('all_recipes.html', recipes=recipes)

@app.route('/recipes/<int:id>/like')
def like_recipe(id):
    # check for login
    if 'user_id' not in session:
        return redirect('user/logout')

    recipe = Recipe.get_by_id(data={"id": id})
    data = {
        "users_id": session['user_id'],
        "recipes_id": id
    }
    Recipe.add_like(data)
    return redirect('/recipes/all')