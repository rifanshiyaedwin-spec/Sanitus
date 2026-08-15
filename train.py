"""
train.py - Deep Learning CNN Model Training Pipeline
Uses Transfer Learning with MobileNetV2 on PlantVillage Dataset.
Exports trained model to models/plant_disease_model.h5.
"""

import os
import json
import matplotlib.pyplot as plt
import numpy as np

def build_and_train_model(dataset_dir="dataset", models_dir="models", epochs=15, batch_size=32):
    """
    Train a MobileNetV2 Transfer Learning classifier for plant disease identification.
    """
    try:
        import tensorflow as tf
        from tensorflow.keras import layers, models
        from tensorflow.keras.applications import MobileNetV2
        from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
    except ImportError:
        print("[Error] TensorFlow is required to run train.py. Install with: pip install tensorflow")
        return

    os.makedirs(models_dir, exist_ok=True)
    
    if not os.path.exists(dataset_dir) or len(os.listdir(dataset_dir)) == 0:
        print(f"[Error] Dataset directory '{dataset_dir}' is empty or missing.")
        print("Please place the PlantVillage dataset folders inside 'dataset/' before training.")
        return

    img_height, img_width = 224, 224
    image_size = (img_height, img_width)

    print("[INFO] Loading dataset from:", dataset_dir)
    train_ds = tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=image_size,
        batch_size=batch_size
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=image_size,
        batch_size=batch_size
    )

    class_names = train_ds.class_names
    num_classes = len(class_names)
    print(f"[INFO] Found {num_classes} classes across dataset.")

    # Save class indices json
    class_indices = {i: name for i, name in enumerate(class_names)}
    class_json_path = os.path.join(models_dir, "class_indices.json")
    with open(class_json_path, "w") as f:
        json.dump(class_indices, f, indent=2)
    print(f"[INFO] Saved class indices to {class_json_path}")

    # Optimize data pipeline caching
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # Data Augmentation Pipeline
    data_augmentation = models.Sequential([
        layers.RandomFlip("horizontal_and_vertical"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
        layers.RandomContrast(0.1)
    ], name="data_augmentation")

    # Base Transfer Learning Model (MobileNetV2)
    base_model = MobileNetV2(
        input_shape=(img_height, img_width, 3),
        include_top=False,
        weights="imagenet"
    )
    base_model.trainable = False  # Freeze base feature extractor

    # Construct Complete Architecture
    inputs = tf.keras.Input(shape=(img_height, img_width, 3))
    x = data_augmentation(inputs)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
    x = base_model(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    model = tf.keras.Model(inputs, outputs, name="PlantaSanitus_MobileNetV2")

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    model.summary()

    # Callbacks
    model_save_path = os.path.join(models_dir, "plant_disease_model.h5")
    callbacks = [
        ModelCheckpoint(model_save_path, save_best_only=True, monitor="val_accuracy", mode="max", verbose=1),
        EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2, verbose=1)
    ]

    print("[INFO] Starting Deep Learning model training...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs,
        callbacks=callbacks
    )

    print(f"[SUCCESS] Model training complete! Saved to {model_save_path}")

    # Plot Accuracy & Loss Curves
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend(loc='lower right')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.legend(loc='upper right')

    plot_path = os.path.join(models_dir, "training_metrics.png")
    plt.savefig(plot_path)
    print(f"[INFO] Saved training metrics plot to {plot_path}")

if __name__ == "__main__":
    build_and_train_model()
