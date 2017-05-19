# hiragana_recognizer

## Usage
Installing the necessary libraries through requirement.txt
```
pip install -r requirement.txt
```
|Layer Name| Description|
|--|--|
|conv1| convolutino and rectified linear activation|
|pool1 | max pooling|
|norm1 | local response normalization|
|conv2 | convolution and rectified linear activation|
|norm2| local response normalization |
|pool2| max pooling|
|local3 | fully connected layer with rectified linear activation|
|local3 | fully connected layer with rectified linear activation|
|softmax_linear| linear transformation to produce logits|
