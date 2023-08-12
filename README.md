# Capstone
Welcome to our Capstone Project!  We are Team Take-off, a group of 3 University of Michigan Master of Applied Data Science students who came together to work on our final (aka Capstone) project for the program. This project represents our enthusiasm for using Data Science skills to understand (and predict) flight delays.  We hope you find this repo as interesting and fun as we did making it!

## Project Description

Have you ever been to an airport and waited and waited and waited for a flight?  If so, have you ever thought to yourself, 'I wish I could've known in advance about the delay'? Have you ever wondered how quickly that plane or airline was able to get back on schedule? If so, you're in the right place.  Our project dealt with these questions in the following way:
-  use several machine learning algorithms to learn a range of variables related to past flights, aircraft features and a tremendous amount of weather variables to predict whether a flight will be delayed or not
-  Use network analysis to study flight delay propagation with Susceptible-Infected-Recovered-Susceptible (SIRS) modeling. The aim was to see how delays infect subsequent flights and how quickly they are able to recover. 

We encourage you to read our Final Report to learn more about our motiviations, methods and findings.

Things to be aware of:
 - Our analysis is primarily centered around the Dallas / Fort Worth Airport.  This airport was chosen due to it's importance in the US aiport network or its high centrality to other nodes in the airport network.   

## External Data Resources/URLS
Data was extracted from the following locations:
 - Flight data from 2010-2023 extracted from [Bureau of Transportation Statistics Ontime Data](https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr)  
 - The Flight Data had tail numbers which we were able to use to extract details about the aircraft passing the tail numbers to [AeroBaseGroup](https://aerobasegroup.com/tail-number-lookup)
 - We also incorporated weather data through the NOAA's website using an api key.

## Project Notebooks and Resources

This repo contains the following folders:
- data_aquisition: out data came from the sources mentioned above.  Our processes for extracting the data and joining together can be found in these notebooks.
- data_preprocessing: contains folders that entail transforming our data into features for modeling
- modeling: this folder contains all of the models for this project and the associated notebooks to evaluate model performance.
- assets: this folder contains png files containing our visualizations, a copy of the NOAA manual with details about the weather variables we used.


## Quick Start
1. All file locations should be stored in the files.json file as key-value pairs where the values are the file locations. For ease of access, all models and final training tests sets are included in the models and data folder respectively and their relative locations are documented in the files.json file in this repo. You may need to update these locations based on your folder structure.

- Running the classification models:
  1. The best place to start is simply running the [Test_Models notebook](/models/Test_Models.ipynb).  This will load all of the package dependencies and the pretrained models and can be used to execute the visualizations/metrics seen in the notebook. 
  2. The Logistic Regression, Random Forest and Gradient Boosting Classifiers are packaged as separate pkl files and share a separate pipeline pkl object which should be used to transform the test data before prediction. Make sure that joblib package is imported
     ```
     import joblib
     lr = joblib.load(files['Models']['LR'])
     rf = joblib.load(files['Models']['RF'])
     gb = joblib.load(files['Models']['GB'])
     preprocessor = joblib.load(files['Models']['pipe'])
     ```
  3. The Neural Network has several dependencies and can be challenging to setup.  If running in Colab, make sure you're using a CPU runtime (to avoid any runtime issues) and that the NN_Model.py files is accessible to the model:
     ```
     import sys
     project_dir = files['Dirs']['Main']
     model_dir = files['Dirs']['Model']
     sys.path.append(model_dir)
     sys.path.append(project_dir + model_dir)

     # files from main and model directories available for import
     from NN_model import custom_f1, XTransform, create_model
     ``` 
