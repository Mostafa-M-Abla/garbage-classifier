import numpy as np
import pandas as pd
import time
import platform
import os
import tensorflow

from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image


# image size in pixels, when images are loaded this size will be used
IMAGE_WIDTH = 320    
IMAGE_HEIGHT = 320

# List of our 12 categories
categories_list = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'green-glass',
                      'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']
					  

def load_image(img_path):
    ''' Function to load an image and convert it to an array with the right shape '''
	
    print('img name = ',img_path)
    img = image.load_img(img_path, target_size = (IMAGE_WIDTH, IMAGE_HEIGHT)) # load the image from the directory
    img = image.img_to_array(img) 
    # add an additional dimension, (i.e. change the shape of each image from (320, 320, 3) to (1, 320, 320, 3)
	# so that the image size is compatible with our model
    img = np.expand_dims(img, axis = 0)    
	
    return img
	
def load_model(model_h5_path, model_json_path):
	''' Load the trained model from the h5 and the json files '''
		
	# load json and create model
	json_file = open(model_json_path, 'r')

	model_json = json_file.read()

	json_file.close()

	model = model_from_json(model_json)

	# load weights into new model
	model.load_weights(model_h5_path)

	return model
	

def predict(model, image_to_classify_name, model_h5_path, model_json_path):
	''' Predict to which category belongs the sleected image and return the top 3 categories with their probabilities'''

	# return the probabilities of all 12 categories
	pred = model.predict(load_image(image_to_classify_name))

	preds_df = pd.DataFrame({
		'categories': categories_list,
		'preds': pred[0]
	})
	
	# sort the categories with ascending values of the probabilities
	preds_df.sort_values(by=['preds'], inplace=True, ascending=False)

	# convert the probabilities to percentages
	category_1_name = preds_df.categories.iloc[0]
	category_1_prob = round((preds_df.preds.iloc[0]* 100), 1)  
	
	category_2_name = preds_df.categories.iloc[1]
	category_2_prob = round((preds_df.preds.iloc[1]* 100), 1)  
	
	category_3_name = preds_df.categories.iloc[2]
	category_3_prob = round((preds_df.preds.iloc[2]* 100), 1)  
	
	return category_1_name, category_1_prob, category_2_name, category_2_prob, category_3_name, category_3_prob 