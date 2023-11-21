from numpy import eye

from simulate_hte.create_settings import (create_database_settings, create_normal_dist_settings, create_model_settings,
                                          create_binomial_distribution_settings)
from simulate_hte.generate import generate_baseline_data

if __name__ == '__main__':
    settings = create_database_settings(n_observations=4,
                                        n_covariates=2,
                                        covariate_dist_settings=[create_normal_dist_settings(),
                                                                 create_binomial_distribution_settings(prob=0.2)])

    values = generate_baseline_data(database_settings=settings)

    model_settings = create_model_settings(constant=1,
                                           model_matrix=eye(4),
                                           transformation_settings=[],
                                           coefficients=[1, 1, 1, 1])
    print(values)