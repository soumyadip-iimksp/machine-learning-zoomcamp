#### To create releases
[link](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

#### Download the model from github
```
wget https://github.com/CrookedNoob/machine-learning-zoomcamp/releases/download/v6.0.2/xception_v6.h5 -O xception_v6_ep_07_ac_0.868.h5
```

```
saved_model_cli show --dir clothing-model --all
```
```
MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['__saved_model_init_op']:
  The given SavedModel SignatureDef contains the following input(s):
  The given SavedModel SignatureDef contains the following output(s):
    outputs['__saved_model_init_op'] tensor_info:
        dtype: DT_INVALID
        shape: unknown_rank
        name: NoOp
  Method name is:

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['input_28'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 299, 299, 3)
        name: serving_default_input_28:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['dense_18'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 10)
        name: StatefulPartitionedCall:0
  Method name is: tensorflow/serving/predict
2022-12-30 18:07:33.317999: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Concrete Functions:
  Function Name: '__call__'
    Option #1
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
    Option #2
      Callable with:
        Argument #1
          input_28: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_28')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
    Option #3
      Callable with:
        Argument #1
          input_28: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_28')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
    Option #4
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None

  Function Name: '_default_save_signature'
    Option #1
      Callable with:
        Argument #1
          input_28: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_28')

  Function Name: 'call_and_return_all_conditional_losses'
    Option #1
      Callable with:
        Argument #1
          input_28: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_28')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
    Option #2
      Callable with:
        Argument #1
          input_28: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='input_28')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
    Option #3
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: False
        Argument #3
          DType: NoneType
          Value: None
    Option #4
      Callable with:
        Argument #1
          inputs: TensorSpec(shape=(None, 299, 299, 3), dtype=tf.float32, name='inputs')
        Argument #2
          DType: bool
          Value: True
        Argument #3
          DType: NoneType
          Value: None
          ```


Run model in a pre-built docker image tensorflow/serving:2.7.0
```
 winpty docker run -it --rm  -p 8500:8500  \
--mount type=bind,source=$(pwd)/clothing-model,target=/models/clothing-model/1 \
-e MODEL_NAME="clothing-model" \
-t tensorflow/serving:2.7.0
```

Install GRPCIO and TF-Serving libraries
```
pip install grpcio==1.42.0 tensorflow-serving-api==2.7.0
```