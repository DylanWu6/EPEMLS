import tensorflow as tf
from keras_preprocessing.sequence import pad_sequences
import innvestigate
import keras
import numpy as np

tf.compat.v1.disable_eager_execution()

# tf.compat.v1.experimental.output_all_intermediates(True)


loaded_model = keras.models.load_model("../NetworkTraining/VulDeePecker/models/model.006--ACC_0.9108.pb")
analyzer = innvestigate.create_analyzer("input_t_gradient", loaded_model)
array = np.load("../NetworkTraining/VulDeePecker/test_data.npy")
analysis = analyzer.analyze(array)
#     for i in range(1):
#         print(array[i])
#         print(analysis[i])
# #print(loaded_model.predict(array)[0])


#print(analysis[0])
# for i in range(20):
#     print(analysis[i])
# np.save("../NetworkTraining/VulDeePecker/after_whitebox/integrated_gradients.npy",analysis)

