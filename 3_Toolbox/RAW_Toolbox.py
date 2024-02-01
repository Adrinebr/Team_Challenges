
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from scipy.stats import pearsonr


###  DESCRIBE_DF 

def describe_df(df):
    """
     La función realiza un análisis de las columnas de un dataframe.

    Argumento:
    el dataframe (df) que hay que analizar.

    Retorna:
    tipo: un dataframe con la información detallada siguiente sobre cada columna del dataframe :
       - el tipo de la columna,
       - el tanto por ciento de valores nulos o missings,
       - los valores únicos y
       - el porcentaje de cardinalidad.
       
    """
    # Inicializar listas para la información correspondiente
    column_names = []
    data_types = []
    null_percentages = []
    unique_values = []
    cardinality_percentages = []

    # Iterar sobre cada columna del dataframe
    for column in df.columns:
        
        # Nombre de la columna
        column_names.append(column)

        # Tipo de dato de la columna
        data_types.append(df[column].dtype)

        # Porcentaje de valores nulos
        null_percentage = (df[column].isnull().sum() / len(df)) * 100
        null_percentages.append(null_percentage)

        # Valores únicos
        unique_value = df[column].nunique()
        unique_values.append(unique_value)

        # Porcentaje de cardinalidad
        cardinality_percentage = (unique_value / len(df)) * 100
        cardinality_percentages.append(cardinality_percentage)
        
        
    # Crear un nuevo dataframe 
    result_df = pd.DataFrame({
        'COL_N': column_names,
        'DATA_TYPE': data_types,
        'MISSINGS(%)': null_percentages,
        'UNIQUE_VALUES': unique_values,
        'CARDIN(%)': cardinality_percentages
    })

    return result_df

###  TIPIFICA_VARIABLES 

def tipifica_variables(df, umbral_categoria, umbral_continua):
    """
    La función sugiere el tipo de cada variable presente en un dataframe.

    Argumentos:
    df: El dataframe a analizar.
    umbral_categoria (int): Umbral para considerar una variable como categórica.
    umbral_continua (float): Umbral para considerar una variable numérica como continua.

    Retorna:
    tipo : un dataframe con dos columnas, "nombre_variable" y "tipo_sugerido".
    """
    
    # Inicializar listas para la información correspondiente
    variable_names = []
    sugg_types = []

# Iterar sobre cada columna del dataframe
    for column in df.columns:
        
    # Nombre de la columna
        variable_names.append(column)

        # Cardinalidad de la columna
        cardinality = df[column].nunique()

        # Tipo sugerido según las pautas siguientes:  
        """
    - Si la cardinalidad es 2, asignara "Binaria"
    - Si la cardinalidad es menor que umbral_categoria asignara "Categórica"
    - Si la cardinalidad es mayor o igual que umbral_categoria, entonces entra en juego el tercer argumento:
        - Si además el porcentaje de cardinalidad es superior o igual a umbral_continua, asigna "Numerica Continua"
        - En caso contrario, asigna "Numerica Discreta"
        """
        if cardinality == 2:
                suggested_type = "Binaria"
        elif cardinality < umbral_categoria:
            suggested_type = "Categórica"
        else:
            cardinality_percentage = (cardinality / len(df)) * 100
            if cardinality_percentage >= umbral_continua:
                suggested_type = "Numerica Continua"
            else:
                suggested_type = "Numerica Discreta"

    # Añadir el tipo sugerido a la lista
        sugg_types.append(suggested_type)

    # Crear un nuevo dataframe con la información recopilada
    result_df = pd.DataFrame({
    'nombre_variable': variable_names,
    'tipo_sugerido': sugg_types
})
    return result_df

### GET_FEATURES_NUM_REGRESSION

def get_features_num_regression(df, target_col, umbral_corr, pvalue=None):
    """
    La funcion devuelve una lista con las columnas numéricas del dataframe cuya correlación con la columna designada
    por "target_col" sea superior en valor absoluto al valor dado por "umbral_corr".
    Además si la variable "pvalue" es distinta de None, sólo devolvera las columnas numéricas cuya correlación supere el valor indicado 
    y además supere el test de hipótesis con significación mayor o igual a 1-pvalue.

    Argumentos:
    df: El dataframe inicial con las variables.
    target_col (str): Nombre de la columna que será el target del modelo de regresión.
    umbral_corr (float): Umbral de correlación (valor absoluto) para considerar una variable como relevante, comparandola con "target_col".
    pvalue (float): Umbral de significación útil para el test de hipótesis. Por defecto es None.

    Retorna:
    list: una lista con las columnas numéricas cuya correlación con la variable "target_col" supere el valor indicado "umbral_col"
    y además supere el test de hipótesis con significación mayor o igual a 1-pvalue.
    """
    if target_col not in df.columns:
        print(f"Error: La columna '{target_col}' no existe en el dataframe.")
        return None

    if target_col not in df.select_dtypes(include=[np.number]).columns:
        print(f"Error: La columna '{target_col}' no es numérica en el dataframe.")
        return None

    # Utilizar la función tipifica_variables para obtener el tipo sugerido de target_col
    tipo_sugerido = tipifica_variables(df[[target_col]], 5, 10.0)['tipo_sugerido'][0]

    # Verificar si target_col es una variable numérica continua
    if tipo_sugerido != "Numerica Continua":
        print(f"Error: La columna '{target_col}' no es una variable numérica continua.")
        return None

    if not (0 <= umbral_corr <= 1):
        print("Error: El umbral de correlación debe estar entre 0 y 1.")
        return None

    if pvalue is not None and not (0 <= pvalue <= 1):
        print("Error: El valor de pvalue debe estar entre 0 y 1.")
        return None

    # Obtener la correlación entre la variable target y las demás variables numéricas seleccionadas gracias a .select_dtypes(include=[np.number])
    correlations = df.select_dtypes(include=[np.number]).corr()[target_col]

    # Filtrar las columnas con correlación superior al umbral -> features
    features = correlations[abs(correlations) > umbral_corr].index.tolist()
    # se usa la funccion abs() porque hemos visto que una correlacion fuerte negativa también vale!

    # Filtrar por p-value si es el caso
    if pvalue is not None:
        quedarse_con_features = []
        for feature in features:
            # Calcular la correlación y el p-value
            correlation, p_value_test = pearsonr(df[feature], df[target_col])
            # Verificar si el p-value es menor o igual al umbral especificado
            if p_value_test <= (1 - pvalue):
                quedarse_con_features.append(feature)
        return quedarse_con_features
        

    return features

### PLOT_FEATURES_NUM_REGRESSION

def plot_features_num_regression(df, target_col="", columns=[], umbral_corr=0, pvalue=None):
    """
     Pinta pairplots y devuelve las columnas relevantes según correlación y test de hipótesis - es decir las features que ha identificado get_features_num_regression.
     Argumentos:
     df: El dataframe inicial con las variables.
     target_col (str): Nombre de la columna que será el target del modelo de regresión.
     columns (list): lista de features, o de variables numericas
     umbral_corr (float): Umbral de correlación (valor absoluto) para considerar una variable como relevante, comparandola con "target_col".
     pvalue (float): Umbral de significación útil para el test de hipótesis. Por defecto es None.

     Retorna:
     Si la lista columns no está vacía, la función pintará una pairplot del dataframe considerando la columna designada por "target_col" y las features.
    
    """
     # Comprobaciones de los valores de entrada
    if target_col not in df.columns:
        print(f"Error: La columna '{target_col}' no existe en el dataframe.")
        return None

    if target_col not in df.select_dtypes(include=[np.number]).columns:
        print(f"Error: La columna '{target_col}' no es numérica en el dataframe.")
        return None

    # Utilizar la función tipifica_variables para obtener el tipo sugerido de target_col
    tipo_sugerido = tipifica_variables(df[[target_col]], 5, 10.0)['tipo_sugerido'][0]

    # Verificar si target_col es una variable numérica continua
    if tipo_sugerido != "Numerica Continua":
        print(f"Error: La columna '{target_col}' no es una variable numérica continua.")
        return None

    if not (0 <= umbral_corr <= 1):
        print("Error: El umbral de correlación debe estar entre 0 y 1.")
        return None

    if pvalue is not None and not (0 <= pvalue <= 1):
        print("Error: El valor de pvalue debe estar entre 0 y 1.")
        return None

# Obtener las columnas relevantes usando la función get_features_num_regression
    relevant_columns = get_features_num_regression(df, target_col, umbral_corr, pvalue)

    # Verificar si hubo algún error en get_features_num_regression
    if relevant_columns is None:
        return None

    # Si relevant_columns no es None, asignar sus valores a columns
    if relevant_columns:
        columns = relevant_columns

    # Si la lista de columnas está vacía, asignar todas las variables numéricas del dataframe
    if not columns:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()

    # Pintar pairplot
    sns.pairplot(df[columns + [target_col]])
    plt.show()
    
    return columns