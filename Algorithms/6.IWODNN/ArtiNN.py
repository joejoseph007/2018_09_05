import tensorflow as tf
import keras
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model     
from keras.models import model_from_json
import random
def Deep_neural_net(Z1,Z2,t='T',sample=[]):
	if t=='T':
		print('Training Neural Network')
		np.savetxt('Normalisation',[np.max(Z2)])
		Z1=Z1/np.max(Z1)#-np.min(Z1)
		Z2=Z2/np.max(Z2)#-np.min(Z2)
			
		model = tf.keras.models.Sequential([tf.keras.layers.Flatten()])
		model.add(tf.keras.layers.Dense(1024,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(1024,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(1024,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(1024,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(1,activation=tf.nn.sigmoid))

		'''
		model.compile(optimizer='adamax',
					loss='binary_crossentropy',
					metrics=['mae'])

		'''
		model.compile(optimizer='adamax',
					loss='mse',
					metrics=['mae'])
		#'''

		model.fit(Z1, Z2, epochs=200)#,verbose=0)
		#model.save('Neural_Network.h5')
		
		model_json = model.to_json()
		with open("Neural_Netork_model.json", "w") as json_file:
			json_file.write(model_json)

			# serialize weights to HDF5
		model.save_weights("Neural_Netork_model.h5")


	if t=='P': 
		Normalisation=np.loadtxt('Normalisation')
		print(Normalisation)
		sample=sample/np.max(sample)#-np.min(sample)
		
		json_file = open('Neural_Netork_model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		model = model_from_json(loaded_model_json)

		# load weights into new model
		model.load_weights("Neural_Netork_model.h5")
		#print("Loaded model from disk")
		
		#model=load_model('Neural_Netork_model.hdf5')
		
		prediction=model.predict(sample)
		
		return prediction*Normalisation#+np.min(prediction)



#Something to test the ANN
#'''
def func(Z1):
	Z2=np.zeros((len(Z1),1))
	for i in range(len(Z2)):
		Z2[i]=0
		#for j in range(len(Z1[i])):
		j=0
		Z2[i]+=(Z1[i][j][0]**2 + Z1[i][j][1]**2)/4000-np.cos(Z1[i][j][0]/2**(0.5))*np.cos(Z1[i][j][1]/2**(0.5))+1
			#Z2[i]=-20*np.exp(-0.2*np.sqrt(0.5*(Z1[i][j][0]**2+Z1[i][j][1]**2)))-np.exp(0.5*(np.cos(2*np.pi*Z1[i][j][0])+np.cos(2*np.pi*Z1[i][j][1])))+np.e+20
			#Z2[i]=Z1[i][j][0]**2
	
	#for i in range(len(Z2)):
	#	Z2[i]=0
	#	for j in range(len(Z1[i])):
	#		Z2[i]+=((Z1[i][j][0]**2+Z1[i][j][1]**2)**0.5)
	
	return Z2

Z1=np.random.rand(100,10,10)*random.choice([-1,1])*500
#Z2=np.zeros((600,1))
Z2=func(Z1)

Deep_neural_net(Z1,Z2,'T')


Z1=np.random.rand(20,10,10)*random.choice([-1,1])*500
#Z2=np.zeros((20,1))
Z2=func(Z1)

predictions=Deep_neural_net(Z1,Z2,'P',Z1)


plt.plot(Z2)
plt.plot(predictions)
plt.show()
#'''