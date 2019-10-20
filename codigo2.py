import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt
filenames=[]
labels=[]
class_names=[]
for i in range(47):
    nom='img'+str(i)+'.png'
    filenames.append(nom)
    labels.append(str(i))
    class_names.append(str(i))

nom=tf.constant(filenames)
eti=tf.constant(labels) 
dataset = tf.data.Dataset.from_tensor_slices((nom, eti))


def _parse_function(filename, label):
    image_string = tf.io.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    image = tf.cast(image_decoded, tf.float32)
    label=tf.strings.to_number(label, out_type=tf.int32)
    return image, label
    
dataset = dataset.map(_parse_function)
dataset = dataset.batch(47)

# step 4: create iterator and final input tensor
iterator = tf.compat.v1.data.make_one_shot_iterator(dataset)
enima, eneti = iterator.get_next()
pruiba, prutique = enima,eneti  
enima = enima / 1.0
pruiba = pruiba / 1.0




#print(enima.shape)
#plt.figure(figsize=(10,10))
#for i in range(25):
#    plt.subplot(5,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(enima[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[eneti[i]])
#plt.show()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(589, 963,3)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(47, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(enima, eneti, epochs=10)



    