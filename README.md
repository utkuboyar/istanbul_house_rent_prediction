# Istanbul House Rent Prediction
![newplot](https://user-images.githubusercontent.com/95041952/215736778-2ee10353-65f0-4395-933a-b3c50559b6f7.png)


The aim of this project is to analyze the factors behind house rents in Istanbul and to predict the rents using regression techniques. The metric used is MAE.

## Data Colection
The data were scraped from hepsiemlak.com at the end of January 2023. The data used for analysis may not be representative of the current situtation anymore.

## Preprocessing
* The distribution of rents are quite skewed and it contains large outliers. These were dropped by setting a treshold on the target before the analysis.
* To deal with a possible problem of rare categories, columns konut_tipi, isinma_tipi, yapi_tipi, yapinin_durumu, yakit_tipi and kullanim_durumu were binned. The rule of binning was based both on domain knowledge and data-specific aspects of the features. The categories underwent hierarchical clustering based on their mean target values and the presumption was in favor of the ones that are close to each other to be in the same bin. Yet, the final decisions were made based on domain knowledge. 
* Feature site_icerisinde had a large cardinality and each of its subsets had small numbers of observations. It was thus transformed into a binary feature where the observations that initially contained information about this feature have now True and the rest of them -i.e. the None ones- have False.
* cephe column had a structure like [kuzey, güney, batı], [batı, güney], [], [doğu, kuzey]... (with four unique values) ant this was extended into four separete binary features. Then a new column called cephe_sayisi were added based on the lengths of the above lists. 
* bulundugu_kat was a cumbersome column, as it contained both a continuous and a categorical character. It was treated as a continuous feature and the categories that can be interpreted as continuous were transformed into numbers using domain knowledge. The remaining ones were still hard to bin in each other. Therefore, they were set to None and left to the merit of tree-based models.

## Models
* Initially, four regressors were trained: xgboost, lightgbm, random forest and support vector regressor. The one that performed best based on MAE was xgboost.
* Then an ensemble model were trained with stacking technique. 
...
