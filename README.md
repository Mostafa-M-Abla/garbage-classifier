# garbage-classifier
This project is a demonstration of the ability of machine learning to sort household garbage into 12 different categories and thus facilitate the recycling process.

# As a part of this project the following is done
-	I collected a data set of more than 15,000 images , saved in the “Data set folder” and has a “description” file.
-	I wrote a notebook to train the model on classifying the images, the notebook is saved as “model_training_notebook.ipynb” you can also open the notebook in Kaggle using the link https://www.kaggle.com/mostafaabla/garbage-classification-keras-transfer-learning you can also run and edit the notebook there. The notebook has detailed description of what is being done.
-	I wrote a web application that takes an image url and predicts to which class does this image belongs, you can access the web app here https://garbage-classifier.azurewebsites.net/

# Repository Contents
1.	“DataSet” Folder with description file
2.	“model_training_notebook.ipynb” where the model is trained
3.	“model.json” and “model_weights.h5” which are the trained model and the weights of the trained model respectively, they are used to perform the prediction.
4.	“static” folder contains some images for the web app.
5.	“template” folder has the html file for the web app
6.	“app.py” is the main file for the web app, and it also uses the “predict.py” file
7.	“Dockerfile” is the file from which I created the docker image that I deployed.
8.	Requirements.txt has a list of all the required packages to run the application.

# How to run
-	To test the web app, visit https://garbage-classifier.azurewebsites.net/
-	To run the model training notebook visit https://www.kaggle.com/mostafaabla/garbage-classification-keras-transfer-learning
-	If you want to run the web app on your PC then you need to install all the packages mention in the “requirements.txt” and then start the “app.py”
