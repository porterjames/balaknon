from flask import jsonify
from flask_login import login_required

from app import app
from app.models.geo import Country, Language


@app.route('/country/autocomplete')
@login_required
def autocomplete_country():
    """autocomplete for country names"""
    country_names = [c.name for c in Country.query.order_by(Country.name.asc())]
    return jsonify(country_names=country_names)


@app.route('/language/autocomplete')
@login_required
def autocomplete_language():
    """autocomplete for languages"""
    language_names = [l.name for l in Language.query.order_by(Language.name.asc())]
    return jsonify(language_names=language_names)
