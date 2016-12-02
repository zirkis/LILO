# Retrain

```bash
$ python retrain.py \
--bottleneck_dir=../train_data/bottlenecks \
--how_many_training_steps 1000 \
--model_dir=../train_data/inception \
--output_graph=../train_data/retrained_graph.pb \
--output_labels=../train_data/retrained_labels.txt \
--image_dir ../data \
--flip_left_right True \
--random_crop 25 \
--random_brightness 25
```

[![alt text](https://github.com/zirkis/LILO/blob/kevin/docs/images/left.png)](https://github.com/zirkis/LILO/blob/kevin/README.md)