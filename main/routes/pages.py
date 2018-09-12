from flask import render_template, Blueprint, request

blueprint = Blueprint('pages', __name__)


################
#### routes ####
################


@blueprint.route('/')
def home():
    return render_template('pages/home.html')


@blueprint.route('/analysis')
def analysis():
    return render_template('pages/analysis.html')

@blueprint.route('/prediction')
def prediction():
    return render_template('pages/prediction.html')


@blueprint.route('/visualisation')
def visualisation():
    return render_template('pages/visualisation.html')
