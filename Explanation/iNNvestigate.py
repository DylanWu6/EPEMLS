import innvestigate
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import custom_object_scope
from tensorflow.keras.models import load_model
import keras.backend as K
from keras.models import Model
def true_positive_metric(y, y_hat):
    y_hat_rounded = K.round(y_hat)
    if vec_output:
        ground_truth_labels = K.cast(K.argmax(y), dtype='float32')
        predicted_labels = K.cast(K.argmax(y_hat_rounded), dtype='float32')
    else:
        ground_truth_labels = K.cast(y, dtype='float32')
        predicted_labels = K.cast(y_hat_rounded, dtype='float32')
    ground_truth_equal_one = K.cast(K.equal(K.ones(K.shape(ground_truth_labels)), ground_truth_labels), dtype='float32')
    prediction_equal_one = K.cast(K.equal(K.ones(K.shape(predicted_labels)), predicted_labels), dtype='float32')
    # product of these two vectors is 1 if and only if both conditions are met. Sum the product to get the number of samples
    nominator_TPR = K.sum(ground_truth_equal_one * prediction_equal_one)
    denominator_TPR = K.sum(ground_truth_equal_one)
    return nominator_TPR / (denominator_TPR)#+K.epsilon())


def false_positive_metric(y, y_hat):
    y_hat_rounded = K.round(y_hat)
    if vec_output:
        ground_truth_labels = K.cast(K.argmax(y), dtype='float32')
        predicted_labels = K.cast(K.argmax(y_hat_rounded), dtype='float32')
    else:
        ground_truth_labels = K.cast(y, dtype='float32')
        predicted_labels = K.cast(y_hat_rounded, dtype='float32')
    ground_truth_equal_zero = K.cast(K.equal(K.zeros(K.shape(ground_truth_labels)), ground_truth_labels), dtype='float32')
    prediction_equal_one = K.cast(K.equal(K.ones(K.shape(predicted_labels)), predicted_labels), dtype='float32')
    # product of these two vectors is 1 if and only if both conditions are met. Sum the product to get the number of samples
    nominator_FPR = K.sum(ground_truth_equal_zero*prediction_equal_one)
    denominator_FPR = K.sum(ground_truth_equal_zero)
    return nominator_FPR / (denominator_FPR)#+K.epsilon())


with custom_object_scope({'true_positive_metric': true_positive_metric},{'false_positive_metric': false_positive_metric}):
    model = load_model('./model.053--ACC_0.9980--FP_0.0015--TP_0.9982.pb')


def model_wo_softmax(model):
    return Model(inputs=model.inputs, outputs=[layer.output for layer in model.layers[:-1]])


model = model_wo_softmax(model)


# 创建一个新模型，只包含第一个输出
model = Model(inputs=model.inputs, outputs=model.outputs[0])

# 从模型中删除softmax层
# model = innvestigate.utils.model_wo_softmax(model)

# 创建一个分析器，使用深度泰勒分解
analyzer = innvestigate.create_analyzer('gradient', model)

# 在此替换数据
npy_path = r".\test_data.npy"
x = np.load(npy_path, allow_pickle=True)
# 应用分析器
analysis = analyzer.analyze(x)

# 输出结果
print(analysis)
