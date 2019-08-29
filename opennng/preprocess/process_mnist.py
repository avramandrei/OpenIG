import numpy as np
import os


def process_data(load_path, save_path):
    raw_train = np.load(os.path.join(load_path, "train.npy"))
    raw_eval = np.load(os.path.join(load_path, "eval.npy"))

    train = raw_train / 255
    eval = raw_eval / 255

    if len(train.shape) == 3:
        train = np.expand_dims(train, axis=3)
    if len(eval.shape) == 3:
        eval = np.expand_dims(eval, axis=3)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    np.save(os.path.join(save_path, "train.npy"), np.float32(train))
    np.save(os.path.join(save_path, "eval.npy"), np.float32(eval))


if __name__ == "__main__":
    mnist_raw_data_path = os.path.join("..", "..", "data", "mnist", "raw")
    mnist_processed_data_path = os.path.join("..", "..", "data", "mnist", "processed")

    process_data(mnist_raw_data_path, mnist_processed_data_path)
