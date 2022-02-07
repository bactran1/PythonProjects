import tensorflow as tf

def isThereGPU():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))

isThereGPU()