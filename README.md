# Istanbul House Rent Prediction
![newplot](https://user-images.githubusercontent.com/95041952/215736778-2ee10353-65f0-4395-933a-b3c50559b6f7.png)


The aim of this project is to analyze the factors behind house rents in Istanbul and to predict the rents using regression techniques. The metric used is MAE.

## Data Colection
The data were scraped from hepsiemlak.com at the end of January 2023. The data used for analysis may not be representative of the current situation  anymore.

## Preprocessing
* The distribution of rents is quite skewed and it contains large outliers. These were dropped by setting a threshold on the target before the analysis.
* To deal with a possible problem of rare categories and high cardinality, columns konut_tipi, isinma_tipi, yapi_tipi, yapinin_durumu, yakit_tipi and kullanim_durumu were binned. The rule of binning was based both on domain knowledge and data-specific aspects of the features. The categories underwent hierarchical clustering based on their mean target values and the presumption was in favor of the ones that were close to each other to be in the same bin. Yet, the final decisions were made based on domain knowledge. 
* Feature site_icerisinde had a large cardinality and each of its subsets had small numbers of observations. It was thus transformed into a binary feature where the observations that initially contained information about this feature are now True and the rest of them -i.e. the None ones- are False.
* cephe column had a structure like [kuzey, güney, batı], [batı, güney], [], [doğu, kuzey]... (with four unique values) and this was extended into four separate binary features. Then a new column called cephe_sayisi were added based on the lengths of the above lists. 
* bulundugu_kat contained both continuous and categorical characters. It was treated as a continuous feature and the categories that can be interpreted as continuous were transformed into numbers using domain knowledge. The remaining ones were still hard to bin in each other. Therefore, they were set to None and left to the merit of tree-based models.

## Models
Initially, four regressors were trained: xgboost, lightgbm, random forest and support vector regressor. The one that performed best based on MAE was xgboost. Then an ensemble model was trained with the stacking technique. The entire process was done with 5-fold cross validation: 
* The dataset was initially splitted into train and test sets. 
* The train set was further splitted into five folds for the cv procedure.
* For each of the five folds in the train set, the base models were trained on the rest of the four folds and they made predictions on the validation set in hand. After the cv procedure, they were fitted on the whole train data and then predicted the test set. 
* Then, the final model was trained on the train set with the predictions of the base models. It was then validated on the test set.
* The ensemble model enhanced the overall performance slightly. 

