# Retrain
Open a terminal then:

## Activate the virtualenv

```bash
WORKSPACE
```

## Go to `app/scripts/training` and run `retrain.py`

```bash
cd ~/app/scripts/training

$ python retrain.py \
--bottleneck_dir ../../train_data/bottlenecks \
--how_many_training_steps 1000 \
--model_dir ../../train_data/inception \
--output_graph ../../train_data/retrained_graph.pb \
--output_labels ../../train_data/retrained_labels.txt \
--image_dir ../../data \
--flip_left_right True \
--random_crop 25 \
--random_brightness 25
```

## Available options

### Input and output file flags.

#### --image_dir

Path to folders of labeled images.

**Default:** `''`

#### --output_graph

Where to save the trained graph.

**Default:** `'/tmp/output_graph.pb'`

#### --output_labels

Where to save the trained graph's labels.

**Default:** `'/tmp/output_labels.txt'`

#### --summaries_dir

Where to save summary logs for TensorBoard.

**Default:** `'/tmp/retrain_logs'`

### Details of the training configuration.

#### --how_many_training_steps

How many training steps to run before ending.

**Default:** `4000`

#### --learning_rate

How large a learning rate to use when training.

**Default:** `0.01`

#### --testing_percentage

What percentage of images to use as a test set.

**Default:** `10`

#### --validation_percentage

What percentage of images to use as a validation set.

**Default:** `10`

#### --eval_step_interval

How often to evaluate the training results.

**Default:** `10`

#### --train_batch_size

How many images to train on at a time.

**Default:** `100`

#### --test_batch_size

How many images to test on at a time. This test set is only used infrequently 
to verify the overall accuracy of the model.

**Default:** `500`

#### --validation_batch_size

How many images to use in an evaluation batch. This validation set is
used much more often than the test set, and is an early indicator of
how accurate the model is during training.

**Default:** `100`

###  File-system cache locations.


#### --model_dir

Path to classify_image_graph_def.pb, imagenet_synset_to_human_label_map.txt, 
and imagenet_2012_challenge_label_map_proto.pbtxt.

**Default:** `/tmp/imagenet`

#### --bottleneck_dir

Path to cache bottleneck layer values as files.

**Default:** `/tmp/bottleneck`

#### --final_tensor_name

The name of the output classification layer in the retrained graph.

**Default:** `final_result`


### Controls the distortions used during training.

#### --flip_left_right

Whether to randomly flip half of the training images horizontally.

**Default:** `False`

#### --random_crop

A percentage determining how much of a margin to randomly crop off the
training images.

**Default:** `0`

#### --random_scale

A percentage determining how much to randomly scale up the size of the
 training images by.

**Default:** `0`

#### --random_brightness

A percentage determining how much to randomly multiply the training
image input pixels up or down by.

**Default:** `0`

[![alt text](https://github.com/zirkis/LILO/blob/kevin/docs/images/left.png)](https://github.com/zirkis/LILO/blob/kevin/README.md)