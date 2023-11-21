from numpy import random
from pandas import DataFrame


def generate_baseline_data(database_settings):
    dataset = DataFrame()
    column_names = [f'x{num}' for num in range(1, len(database_settings["covariate_dist_settings"]) + 1)]
    for i, settings in enumerate(database_settings["covariate_dist_settings"]):
        if settings["type"] == "normal":
            dataset[column_names[i]] = random.normal(loc=settings["mean"],
                                             scale=settings["covariance"],
                                             size=database_settings["n_observations"])
        elif settings["type"] == "binomial":
            dataset[column_names[i]] = random.binomial(n = settings["size"],
                                                       p = settings["prob"],
                                                       size = database_settings["n_observations"])
    return dataset
