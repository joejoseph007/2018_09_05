import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model     

from keras.models import model_from_json


def Deep_neural_net(Z1,Z2,t='T',sample=[]):
	if t=='T':
		#print(np.max(Z2))
		np.savetxt('Normalisation',[np.max(Z2)])
		Z1=Z1/np.max(Z1)
		Z2=Z2/np.max(Z2)
			
		model = tf.keras.models.Sequential([tf.keras.layers.Flatten()])
		model.add(tf.keras.layers.Dense(512,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(512,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(512,kernel_initializer='uniform',activation=tf.nn.relu))
		model.add(tf.keras.layers.Dense(512,kernel_initializer='uniform',activation=tf.nn.relu))
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

		model.fit(Z1, Z2, epochs=100)
		#model.save('Neural_Network.h5')
		
		
		model_json = model.to_json()
		with open("Neural_Netork_model.json", "w") as json_file:
			json_file.write(model_json)

			# serialize weights to HDF5
		model.save_weights("Neural_Netork_model.h5")


	if t=='P': 
		Normalisation=np.loadtxt('Normalisation')
		#print(Normalisation)
		sample=sample/np.max(sample)
		
		json_file = open('Neural_Netork_model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		model = model_from_json(loaded_model_json)

		# load weights into new model
		model.load_weights("Neural_Netork_model.h5")
		#print("Loaded model from disk")
		
		#model=load_model('Neural_Netork_model.hdf5')
		
		prediction=model.predict(sample)
		return prediction*Normalisation



#Something to test the ANN
'''

Z1=np.random.rand(60,10,2)
Z2=np.zeros((60,1))

for i in range(len(Z2)):
    Z2[i]=0
    for j in range(len(Z1[i])):
        Z2[i]+=((Z1[i][j][0]**2+Z1[i][j][1]**2)**0.5)/10


Deep_neural_net(Z1,Z2,'T')


Z1=np.random.rand(20,10,2)
Z2=np.zeros((20,1))

for i in range(len(Z2)):
    Z2[i]=0
    for j in range(len(Z1[i])):
        Z2[i]+=((Z1[i][j][0]**2+Z1[i][j][1]**2)**0.5)/10


predictions=Deep_neural_net(Z1,Z2,'P',Z1)


plt.plot(Z2)
plt.plot(predictions)
plt.show()
'''