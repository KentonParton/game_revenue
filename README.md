# game_revenue

## Requirements
##### tensorflow==1.1.0
##### keras==2.1.5
##### pandas==0.22.0

## Files

### scale.py
Scales data from .csv file before training.

### train_model.py
Trains model using scaled data and creates Logs which can be used on Tensorboard and trained_model.h5.

### predict.py
Uses trained_model.h5 to predict potential revenue a game will earn based on proposed_new_product.csv

To view logs in Tensorboard, tensorboard --logdir=game_revenue/logs


