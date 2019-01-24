from icees import iceesclient

def module1(data):
    define_a_cohort = iceesclient.define_cohort(data)
    return define_a_cohort["return value"]["cohort_id"]

def module2_4_question1(input_cohort_id, maximum_p_value):
    AssociationToAllFeaturesObject = iceesclient.AssociationToAllFeatures()
    assoc_to_all_features = AssociationToAllFeaturesObject.run_association_to_all_features('TotalEDInpatientVisits','<', '2', str(maximum_p_value), input_cohort_id)
    features = []
    for assoc in assoc_to_all_features["return value"]:
        feature_b = assoc["feature_b"]
        feature_name_b = feature_b["feature_name"]
        feature_bins_b = list(map(lambda x : x["value"], feature_b["feature_qualifiers"]))
        chi_squared = assoc["chi_squared"]
        p_value = assoc["p_value"]
        counts0 = list(map(lambda x: x[0]["frequency"], assoc["feature_matrix"]))
        counts1 = list(map(lambda x: x[1]["frequency"], assoc["feature_matrix"]))
        features.append({
            "name": feature_name_b,
            "bins": feature_bins_b,
            "counts_by_bin_0": counts0,
            "counts_by_bin_1": counts1,
            "chi_squared": chi_squared,
            "p_value": p_value
        })

    return features

def module2_4_question2(input_cohort_id, maximum_p_value):
    AssociationToAllFeaturesObject = iceesclient.AssociationToAllFeatures()
    assoc_to_all_features = AssociationToAllFeaturesObject.run_association_to_all_features('EstResidentialDensity','<', '2', str(maximum_p_value), input_cohort_id)
    features = []
    for assoc in assoc_to_all_features["return value"]:
        feature_b = assoc["feature_b"]
        feature_name_b = feature_b["feature_name"]
        feature_bins_b = list(map(lambda x : x["value"], feature_b["feature_qualifiers"]))
        chi_squared = assoc["chi_squared"]
        p_value = assoc["p_value"]
        counts0 = list(map(lambda x: x[0]["frequency"], assoc["feature_matrix"]))
        counts1 = list(map(lambda x: x[1]["frequency"], assoc["feature_matrix"]))
        features.append({
            "name": feature_name_b,
            "bins": feature_bins_b,
            "counts_by_bin_0": counts0,
            "counts_by_bin_1": counts1,
            "chi_squared": chi_squared,
            "p_value": p_value
        })

    return features


