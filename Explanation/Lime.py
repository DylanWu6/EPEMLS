import numpy as np
import pickle as pkl
import argparse
import time
import sys
import os
from sklearn.linear_model import Ridge
from tqdm import tqdm
from scipy.spatial.distance import cosine
from scipy.sparse import issparse, save_npz, vstack

from scipy.sparse import load_npz

def linreg_relevances_to_vector_space(relevances, data, save_path, is_sparse):
    if is_sparse:
        if not issparse(data):
            data = data.tocsr()
        assert len(relevances) == data.shape[0], 'Number of relevances should match the number of data samples.'
        relevance_matrix = vstack(relevances)
        save_npz(save_path, relevance_matrix)
        print('Relevance matrix saved to {}.'.format(save_path))
    else:
        assert len(relevances) == len(data), 'Number of relevances should match the number of data samples.'
        relevance_dict = {i: rel for i, rel in enumerate(relevances)}
        with open(save_path, 'wb') as f:
            pkl.dump(relevance_dict, f)
        print('Relevance dictionary saved to {}.'.format(save_path))

# returns l^2 weight for two points
def get_weight(x,y,sigma=1.0):
    dist = cosine(x,y)
    return np.exp(-dist/sigma)


# calculates lime weights for each feature
# perturbations is a 2d numpy array where the first row corresponds to the original sample
# labels is a 1d numpy array containing the labels for the perturbations and the original sample is supposed to be
# given label 1 by the classifier always. (this way, positive relevances will always speak _for_ the original
# classification of the classifier)
def get_lime_weights(perturbations, labels, random_state):
    assert perturbations.shape[0] == labels.shape[0]
    model_regressor = Ridge(alpha=1, fit_intercept=True, random_state=random_state)
    weights = np.array([get_weight(perturbations[0], y) for y in perturbations])
    model_regressor.fit(perturbations, labels, sample_weight=weights)
    return model_regressor.coef_


# calculates lime weights for several perturbations and labels
# perturbations is a list where each list entry is a 2d numpy array suitable for get_lime_weights
# labels is a 2d numpy array with shape (no_samples, no_perturbations)
def explain_samples(perturbations, labels, random_state=None):
    relevances = []
    start_time = time.time()
    for p, l in tqdm(zip(perturbations, labels), total=len(perturbations)):
        w = get_lime_weights(p, l, random_state)
        relevances.append(w)
    end_time = time.time()
    print('Calculation of {} relevances took on {} seconds ({} seconds per sample).'.format(len(perturbations),
                                                                                           end_time-start_time,
                                                                                            (end_time-start_time)/
                                                                                            len(perturbations),
                                                                                           ))
    return relevances

def mimicus_recover(save_path):
    recovered = []
    array = np.load("../NetworkTraining/Mimicus/result/zero_index2.npy", allow_pickle=True)
    with open(save_path, 'rb') as f:
        data = pkl.load(f)
        x = 0
        for i in array:
            for j in i:
                item = [0] * 135
                y = 0
                for k in j:
                    item[k] = data[x][y]
                    y = y + 1
                recovered.append(item)
            x = x + 1


def main_lime(perturbation_path, label_path, save_path, data_path):
    perturbations = pkl.load(open(perturbation_path, 'rb'))
    labels = np.load(label_path)
    if data_path:
        is_sparse = data_path.split('.')[-1] == 'npz'
        if data_path.split('.')[-1] == 'npy':
            data = np.load(data_path)
        elif data_path.split('.')[-1] == 'pkl':
            data = pkl.load(open(data_path, 'rb'))
        elif args.data_path.split('.')[-1] == 'npz':
            data = load_npz(data_path)
        else:
            print('Data format was not understood. Data could not be loaded.')
            sys.exit(1)
    rels = explain_samples(perturbations, labels)
    if args.data_path:
        linreg_relevances_to_vector_space(rels, data, save_path, is_sparse)
    else:
        pkl.dump(rels, open(save_path+'relevances_lime.pkl', 'wb'))

    mimicus_recover(save_path = save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of the LIME algorithm.')
    parser.add_argument('perturbation_path', type=str,
                        help='Path to list (.pkl) of perturbations for data of shape (no_perturbations, no_features).')
    parser.add_argument('label_path', type=str,
                        help='Path to array containing labels of perturbations of shape (no_samples, no_perturbations).'
                             'Labels are assumed to be binary (0/1).')
    parser.add_argument('save_path', type=str, help='Folder to save results.')
    parser.add_argument('--data_path', type=str, help='Path to data. Can be .npy, .npz, .pkl (sparse,numpy,list)')
    args = parser.parse_args()
    perturbations = pkl.load(open(args.perturbation_path, 'rb'))
    labels = np.load(args.label_path)
    if args.data_path:
        is_sparse = args.data_path.split('.')[-1] == 'npz'
        if args.data_path.split('.')[-1] == 'npy':
            data = np.load(args.data_path)
        elif args.data_path.split('.')[-1] == 'pkl':
            data = pkl.load(open(args.data_path, 'rb'))
        elif args.data_path.split('.')[-1] == 'npz':
            data = load_npz(args.data_path)
        else:
            print('Data format was not understood. Data could not be loaded.')
            sys.exit(1)
    rels = explain_samples(perturbations, labels)
    if args.data_path:
        linreg_relevances_to_vector_space(rels, data, args.save_path, is_sparse)
    else:
        pkl.dump(rels, open(args.save_path+'relevances_lime.pkl', 'wb'))

    mimicus_recover(save_path = args.save_path)