from flask import Flask, request, render_template, redirect
import urllib
import os
import time
import predict
import tensorflow.keras.applications.xception as xception
import pandas as pd
import platform
import tensorflow

app = Flask(__name__)

#Paths where our pre-trained classification model is saved.
model_h5_path = 'model_weights.h5'
model_json_path = 'model.json'

# Load the pre-trained model
model = predict.load_model(model_h5_path, model_json_path)

# Each time the user selects an image to classify we first delete the old saved images
def deleteOldImages():
	
	for filename in os.listdir('static'):
		if filename.startswith('image_to_predict'):  # not to remove other images
			os.remove('static/' + filename)
			
	return

	
@app.route('/', methods = ['GET', 'POST'])
def rootpage():

	# Each time the user selects an image to classify we first delete the old saved images, before saving the new one.
	deleteOldImages()
	
	# url of the target image to classify
	url = ''
	
	# Before the user selects an image to classify, place a blank image just as a placeholder.
	image_to_classify_name = 'static/white_background.jpg'
	
	# The image showing the 12 possible garbage categories
	pred_visualisation_name = 'static/garbage_categories/default.jpg'
	
	# The three top predictions and their respective probabilities
	category_1_name = ''
	category_1_prob = ''
	category_2_name = ''
	category_2_prob = ''
	category_3_name = ''
	category_3_prob = ''
	
	# this statement is true if the user gave an input and pressed the classify button
	if request.method == 'POST' and 'url-input' in request.form:
		
		# Read the url given by the user
		url = request.form.get('url-input')
		request_time = time.time()
		image_to_classify_name =  "static/image_to_predict" +str(request_time)+ ".jpg"
		
		# Save the image selected by the user and predict the top 3 categories
		try:
			urllib.request.urlretrieve(url, image_to_classify_name)		
			category_1_name, category_1_prob, category_2_name, category_2_prob, category_3_name, category_3_prob = \
				predict.predict(model, image_to_classify_name, model_h5_path, model_json_path)
			
			# After we predict that the image belongs to a certain category, we show an image of that category selected
			pred_visualisation_name = 'static/garbage_categories/' +  category_1_name + '.jpg'
			
			# If the user entered an invalid url display an error message
		except ValueError:
			image_to_classify_name = 'static/Warning.jpg'

	return render_template("index.html", image_to_classify_name = image_to_classify_name, pred_visualisation_name = pred_visualisation_name,
							category_1_name = category_1_name, category_1_prob = category_1_prob,
							category_2_name = category_2_name, category_2_prob = category_2_prob,
							category_3_name = category_3_name, category_3_prob = category_3_prob)

							
app.run(host='0.0.0.0', port=5000)