
import tensorflow as tf
import numpy as np
import pandas as pd
from keras import backend as K
from sklearn.base import BaseEstimator, TransformerMixin
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam, SGD
import keras.metrics
import keras.losses

class XTransform(BaseEstimator,TransformerMixin):
	
	def fit(self, X, y=None):
		return self
	
	def transform(self, X):
		X_tensor = tf.convert_to_tensor(X)
		return X_tensor


def custom_f1(y_true, y_pred):
	
	# Code from https://neptune.ai/blog/implementing-the-macro-f1-score-in-keras
	
	y_true = K.cast(y_true, 'float32')  
	y_pred = K.cast(y_pred, 'float32')
	
	def recall_m(y_true, y_pred,sample_weight=None):
		TP = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
		Positives = K.sum(K.round(K.clip(y_true, 0, 1)))
		recall = TP / (Positives+K.epsilon())
		return recall
		
	def precision_m(y_true, y_pred, my_weight=None):
		TP = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
		Pred_Positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
		precision = TP / (Pred_Positives+K.epsilon())
		return precision
	
	precision, recall = precision_m(y_true, y_pred), recall_m(y_true, y_pred)
	f1 = 2*((precision*recall)/(precision+recall+K.epsilon()))
	return f1
	
	
def create_model(dropout_rate=.01,learning_rate=.01, batch_size=512, output_bias=-4.19656855):
	if output_bias is not None:
		output_bias = tf.keras.initializers.Constant(output_bias)
	model= Sequential()
	model.add(Dense(neurons, input_shape=(neurons,), activation='relu'))
	# model.add(Dense(100, activation='relu'))
	# model.add(Dense(75, activation='relu'))
	# model.add(Dropout(dropout_rate))
	model.add(Dense(1, activation='sigmoid', bias_initializer=output_bias))
	optimizer = Adam(learning_rate=learning_rate)
	model.compile(
			  	# loss=keras.losses.BinaryFocalCrossentropy(alpha=.02, apply_class_balancing=True),
			  	loss='binary_crossentropy',
			  	optimizer=optimizer,
			  	metrics=metrics,
			  	weighted_metrics=metrics
				)
	return model
