import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
from tensorflow.keras.models import model_from_json
import numpy as np
import shutil
import sklearn 
from sklearn import tree 

import os # inbuilt module
import random # inbuilt module
import webbrowser # inbuilt module

#=================================== Title ===============================
st.title("""
Fruit Recognizer
	""")

#================================= Title Image ===========================
#================================= About =================================
st.write("""
## 1.About
	""")
st.write("""
Hi all, Welcome to this project. It is a Fruit Recognizer App!!!
	""")
st.write("""
You have to upload your own test images to test it!!!
	""")


#============================ How To Use It ===============================
st.write("""
## 2. How To Use It
	""")
st.write("""
Well, it's pretty simple!!! 
- First of all, download image of a Apple or Orange!
- Next, just Browse that file or Drag & drop that file!
- Please make sure that, you are uploading a picture file!
- Press the **👉🏼 Predict** button to see the magic!!!

 **NOTE :** *If you upload other than an image file, then it will show an error massage when you will click the* **👉🏼 Predict** *button!!!*
	""")

#========================= What It Will Predict ===========================
st.write("""
## 3️.What It Will Predict
	""")
st.write("""
Well, it can predict wheather the image you have uploaded is the image of a Apple or a Orange!
	""")

#======================== Time To See The Magic ===========================
st.write("""
## 👁️‍🗨️ Time To See The Magic 🌀
	""")

#========================== File Uploader ===================================
img_file_buffer = st.file_uploader("Upload an image here 👇🏻")

try:
	image = Image.open(img_file_buffer)
	img_array = np.array(image)
	st.write("""
		Preview 👀 Of Given Image!
		""")
	if image is not None:
	    st.image(
	        image,
	        use_column_width=True
	    )
	st.write("""
		Now, you are just one step ahead of prediction.
		""")
	st.write("""
		**Just Click The '👉🏼 Predict' Button To See The Prediction Corresponding To This Image! 😄**
		""")
except:
	st.write("""
		### ❗ Any Picture hasn't selected yet!!!
		""")

#================================= Predict Button ============================
st.text("""""")
submit = st.button("👉🏼 Predict")

#==================================== Model ==================================
def processing(testing_image_path):
    IMG_SIZE = 50
    img = load_img(testing_image_path, 
            target_size=(IMG_SIZE, IMG_SIZE), color_mode="grayscale")
    img_array = img_to_array(img)
    img_array = img_array/255.0
    img_array = img_array.reshape((1, 50, 50, 1))   
    prediction =loaded_model.predict(img_array)    
    return prediction
#       feature = [[140,1], [130, 1], [150, 0], [170, 0]]
#       label = [0, 0, 1, 1] 
#       clf = tree.DecisionTreeClassifier()
#       clf = clf.fit(feature, labels)
#       # print ((clf.predict([[150, 0]))
#       prediction = clf.predict([[150, 0]])
#       return prediction

def generate_result(prediction):
	st.write("""
	## 🎯 RESULT 
		""")
# 	st.write("""
# 	## 🎯 RESULT 
# 		""")
# 	st.write(prediction)
	if prediction [0]<0.2:
	    st.write("""
	    	## Model predicts it as an image of a APPLE!!!
	    	""")
	else:
	    st.write("""
	    	## Model predicts it as an image of a ORANGE!!!
	    	""")

#=========================== Predict Button Clicked ==========================
if submit:
	try:
		# save image on that directory
		save_img("temp_dir/test_image.png", img_array)

		image_path = "temp_dir/test_image.png"
		# Predicting
		st.write("👁️ Predicting...")

		model_path_h5 = "model/model.h5"
		model_path_json = "model/model.json"
		json_file = open(model_path_json, 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		loaded_model = model_from_json(loaded_model_json)
		loaded_model.load_weights(model_path_h5)

		loaded_model.compile(loss='binary_crossentropy', metrics=['accuracy'],optimizer='adam')

		prediction = processing(image_path)

		generate_result(prediction)

	except:
		st.write("""
		### ❗ Oops... Something Is Going Wrong
			""")

#=============================== Copy Right ==============================
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.write("""
### ©️ Created By Nishanthi
	""")
