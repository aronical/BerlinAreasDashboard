#only final data structures





#side effect free functions



#the use of higher-order functions



functions as parameters and return values




#use closures / anonymous functions

def add_gml_id_to_df(df, _ortsteile_id_map, ortsteil_key_in_df='Ortsteil'):
    df['id'] = df[ortsteil_key_in_df].apply(lambda ortsteil: _ortsteile_id_map[ortsteil])
