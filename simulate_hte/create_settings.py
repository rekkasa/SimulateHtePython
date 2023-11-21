from numpy import eye


def create_database_settings(n_observations,
                             n_covariates,
                             covariate_dist_settings,
                             post_processing=None):
    return {"n_observations": n_observations,
            "n_covariates": n_covariates,
            "covariate_dist_settings": covariate_dist_settings,
            "post_processing": post_processing
            }


def create_normal_dist_settings(mean=0, covariance=1):
    return {
        "type": "normal",
        "mean": mean,
        "covariance": covariance
    }

def create_binomial_distribution_settings(prob, size=1):
    return {"type": "binomial",
            "size": size,
            "prob": prob}


def create_model_settings(type="logistic",
                          model_matrix=eye(0),
                          coefficients=None,
                          constant=None,
                          transformation_settings=None):
    if coefficients is None:
        print("Missing coefficients or model matrix\n Assuming model with only constant")
        model_matrix = eye(0)
        coefficients = None
        transformation_settings = []
    return dict(type=type,
                constant=constant,
                modelMatrix=model_matrix,
                transformation_settings=transformation_settings,
                coefficients=coefficients)


if __name__ == '__main__':
    settings = create_database_settings(n_observations=10,
                                        n_covariates=1,
                                        covariate_dist_settings=[create_normal_dist_settings()])
