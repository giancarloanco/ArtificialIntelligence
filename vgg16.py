from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.utils.vis_utils import plot_model
from keras.applications.vgg16 import VGG16
# load the model
model = vgg16()
# arqui visual
plot_model(model, to_file='vgg16.png')
# arqui
print(model.summary())
# load an image from file
image = load_img('parrot.jpg', target_size=(224, 224))
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
# predict the probability across all output classes
yhat = model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(yhat, top=8)[0]
# retrieve the most likely result, e.g. highest probability
# label = label[0][0]
# print the classification
# print('%s (%.2f%%)' % (label[1], label[2] * 100))
print(label)
