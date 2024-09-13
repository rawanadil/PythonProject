# Consider you have a tuple with common types of machine learning models:
# ML_ models = ("RNN", "SVM", "RE", "LSTM", "RE" "RNN", "CNN")
# in the last step, you should print the common types of deep learning models as follow:
# Common types of deep learning models:
# CNN
# FNN
# LSTM
# RNN
# What procedures must be performed on the tuple (written in blue) to get the last step (written in green)?

ML_models = ("RNN", "SVM", "RF", "LSTM", "RF", "RNN", "CNN")
ML_models2 = set(ML_models)
ML_models2.add("FNN")
ML_models2.remove("RF")
ML_models2.remove("SVM")
print("Common types of deep learning models:")
for i in ML_models2:
    print(i)