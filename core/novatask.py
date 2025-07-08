import json
import numpy as np
import tensorflow as tf
from ml.feature_extraction import extract_features
from adapters.mongo_adapter import MongoAdapter

class NovaTask:
    def __init__(self, db_type, db_uri, model_path=None, mode='offline'):
        self.mode = mode

        if db_type == 'mongodb':
            self.db_adapter = MongoAdapter(db_uri)

        if self.mode == 'online' and model_path:
            self.model = tf.keras.models.load_model(model_path)

    def predict(self, payload):
        if self.mode != 'online':
            return 'allow'

        features = extract_features(payload)
        X = np.array([list(features.values())], dtype=np.float32)
        prediction = self.model.predict(X)
        label_idx = np.argmax(prediction, axis=1)[0]

        label_map_reverse = {0: 'allow', 1: 'block', 2: 'flag'}
        return label_map_reverse.get(label_idx, 'allow')

    def add(self, collection, data):
        return self.db_adapter.add(collection, data)

    def get(self, collection, query):
        return self.db_adapter.get(collection, query)

    def update(self, collection, query, update_data):
        return self.db_adapter.update(collection, query, update_data)

    def delete(self, collection, query):
        return self.db_adapter.delete(collection, query)