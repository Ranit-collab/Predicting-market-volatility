# A. Topic: 

Predicting Market Volatility and building short-term trading strategies using data from Reddit's WallStreetBets. 



# B. Short Description:

The aim of this project is to use data from posts made on the sub-reddit 'WallStreetBets' to make a prediction on stock prices and market volatility. Various features were extracted from these posts and a learning model was trained to predict if specific stocks rose or fell in the given timeframe.



# C. Content:
	1. Project Approach
	2. What does the DATA tell us?
	3. Our PREDICTION models
	4. PERFORMANCE evaluate
	5. CONCLUSION & NEXT STEP



# E. Data Collection:

As per project requirement, the data from the news portals or social media sites which has lot of stock enthusiast, Customers, Investors, Companies and so on is needed. So, the data from Reddit’s WallStreetBets can be used. For this project, two different datasets will be used.

a. SPX file which contains lot of ‘High’, ‘Low’, ‘Close’, ‘Open’, ‘Volume’, so we’ll trim it out as per the Kaggle file named SP500. Hence from this file we’ll get four columns:
##
	i. Open
	ii. Close
	iii. High
	iv. Low
	v. Volume
	vi. Date


![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/sent.png)


b. JSON file that contains the body of WSB post. Since, this file is very large we’ll take out only.
##
	i. Body
	ii. Date
	iii. Score
	
We’ll also create the target variable using open and close value. Where our condition willbe, if yesterday’s closing price is smaller than today’s closing price then our value will be 1 similiarly vice versa.


![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/csvdata.png)




# F. Data Cleaning:

First we’ll perform Sentiment Analysis in the body column that we had received fromJSON file. From where we’ll get the ‘Positive’, ‘Negative’ and 	‘Neutral’ value. Then we’ll merge this values with previously trimmed CSV files on the basis of Date. Hence, after which we’ll perform data cleaning involving following steps:
##
	i. Impute/Remove missing values or Null values (NaN)
	ii. Remove unnecessary and corrupted data.
	iii. Date/Text parsing if required.




# G. Create Target variable:

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/targetcountplot.png)

Creating a target variable where :

    i. Value is 1 if 'Today's closing price is greater than yesterday's closing price'
    ii. Value is 0 if 'Today's closing price is lesser than yesterday's closing price'
  
  
  

# H. Approach:

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/approach.png)



# I. Data Exploration:

After getting the data cleaned, exploration of data is necessary to understand the patterns in
data or to retrieve useful insights/relation.

*a. Exploratory Data Analytics (EDA):*

We can find the correlation among the dependent and independent features so that we can explore which feature is more important (Feature Selection Method) via different methods like:

1. Bi-varaite Barplot

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/Barplot.png)

## Summary of Barplot:
    i. Seems like if our sentiment analysis is negative, our target variable value appears to little.
    ii. Surprisingly, even if our sentiment analysis is positive,  our target variable value does not really 
    increase as we were expecting it to be.
    iii. But the target variable appears to more when the sentiment analysis is neutral.


2. Univariate  CountPlot

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/UniCountplot.png)

## Summary:
	As expected from above calculation our positive sentimental analysis is more in comparison to neutral and negative sentimental analysis.


3. Bivariate Countplot

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/BiCountplot.png)

## Summary

	1. Most of the positive sentiment analysis has target variable 1(Profit) but not 0 (Loss).
	2. All the neutral snetiment analysis has target varaible 1 i.e. has led to profit.
	3. Negative sentiment analysis equally has target variable 0 (Loss) and 1 (Profit).


4. Distribution plot

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/DistributionPlot.png)

## Summary

	1. All our variables are normally distributed.
	2. But there seems to be quite a outlier in the data. 
	3. Before exploring other plot. Let's deal with ourliers first.
	4. We're going to confirm outliers with Boxplot.



5. Boxplot 

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/BiLineplot.png)

## Summary of Box plot
    i. Seems like all other features are uniformly distributed other than 'Volume' and 'cont_pol'.
    ii. Volume and cont_pol has high number of outliers so lets fix that first.
        - Find the IQR (Interquartile Range)
        - Find the upper and lower limit
        - Find outliers
        - Treat outliers
            Since there are lot of outliers, if we'll trim/remove it all we'll have very less data so lets do 'Quantile based flooring and capping'.
              1. Replace all the outliers that are higher than upper limits with upper limit's value.
              2. Replace all the outliers that are higher than upper limits with upper limit's value.
        - Compare the plots after trimming   
        
        

5. Boxplot (After Treating Outliers)

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/Boxplot2.png)

## Summary:

    We've removed the outliers from 'Volume' and 'cont_pol' variable.
    It seems like our data is free from outliers. 
    Let's explore other plot.
    
    
6. Line Plot

   ![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/Unilineplot.png)
   

   ![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/volume.png)


## Summary:

	1. All the value of Open, Close, High and Close are increased as per the time.
	2. But Volume keeps on changing in between.




7. Bivariate Line Plot

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/BiLineplot.png)

# Summary
	Seems like Content polarity and close value are correlated to each other.

	1. As per the graph, close price is increasing as per the year.
	2. If the content polarity is higher, then there is higher chance of getting more closing price.



8. Heatmap

   ![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/Heatmap.png)
 
 ## Summary of Heatmap:

    i. Target variable is highly correlated to 'Volume', 'Closing price', 'Opening price', 'Comment length'  
    and 'Content Polarity' (Sentiment Analysis).
    ii. Suprisingly, Comment length is also highly correlated to 'Open', 'Close', 'High' and 'Low'.
    iii. Seems like the lenght of comment changed as per the year.
    iv. Volume is highly correlated with all other variables other than date( Year and Day).



b. Feature Engineering:

We can encode our categorical data if necessary using different classifiers/labels like
Label Encoder, Binary encoder and so on. We will also find the important features for our
model. Feature Engineering was done using ExtraTreesRegressor.

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/FeatureImp.png)


## Summary of Feature Engineering
	So, basically we can say, Our target variable is highly related to:

    i. Volume
    ii. Opening Price
    iii. Closing price
    iv. Comment Length
    v. Day the comment is posted
    vi. Content Polarity/ Sentiment analysis


# J. Model Building/Training:
Logistic Regression was selected for a model.

	!pip install logisticregression
	
	from sklearn.learn_model import LogisticRegression
	from sklearn.metrics import classification_report, accuracy_score
	
	log_reg = LogisticRegression
	log_reg.fit(x_train, y_train)

	y_pred = log_reg.predict(X_test)
	print(classification_report(y_test, y_pred))

	acc_score = accuracy_score(y_test,y_pred)
	acc_score_per = acc_score * 100
	print(‘The accuracy score is’, acc_score, ‘/’, acc_score_per, ‘%’.)



- Classification Report and Accuracy score of our model (Before Hyperparameter Tuning)

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/conmatrix.png)




# K. Performance Evaluation:
     
1. Confusion Matrix

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/COnfusionMatrix1.png)


## Summary
	True Negative: 69 (Predicted Loss as Loss)
	False Positive: 92 (Predicted Loss as Profit)
	False Negative: 14 (Predicted Profit as Loss)
	True Positive: 153  (Predicted Profit as Profit)



2. ROC-auc Curve
 
![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/RocCURVE1.png)

## Summary:
	The left corner of our model is quite near to top-left corner but not exactly so the roc curve of our model is average.
	In general AUC of 0.8-0.9 is considered good but above 0.9 is considered excellent.
	And also our accuracy score for model is not that good so let's try some Hyperparameter tuning.


# L. Hyperparmeter Tuning

There are various different methods for Hyperparameter Tuning But we don't have that great number of independent features so we'll choose GridSearchCV for hyperparameter tuning for our model. 

## Code:
	from sklearn.model_selection import GridSearchCV

	penalty=['l1', 'l2', 'elasticnet']
	solver=['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
	max_iter=[100,200,300,350]

	random_grid={'penalty':penalty,
             'solver':solver,
             'max_iter':max_iter,
             }

	log_reg_grid_search= GridSearchCV(estimator=log_reg, param_grid=random_grid, cv=20, n_jobs=-1, verbose=2)


1. Confusion Matrix(After Hyperparameter Tuning)

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/CONMATRIX2.png)

## Summary:
	True Negative: 148 (Predicted Loss as Loss)
	False Positive: 13 (Predicted Loss as Profit)
	False Negative: 7  (Predicted Profit as Loss)
	True Positive: 160  (Predicted Profit as Profit)



2. ROC-AUC Curve(After Hyperparameter Tuning)

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/ROC2.png)


## Summary:
	1. The AUC score is  0.98988358686354 / 98.988358686354 % (AUC value about 0.9 is considered outstanding). Hence 
	model has satisfying AUC score.
	2. From the curve also we can see, the line is so close to top-left corner. Hence, our model is really good.


3. Classification Report and Accuracy score of our model (After Hyperparameter Tuning)

   [alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/cM2.png)

## Summary:

	Accuracy score:
	Before Hyperparameter tuning: 0.6798780487804879 / 67.98780487804879 %.
	After Hyperparameter tunign: 0.9390243902439024 / 93.90243902439023 %.
	Hence, we can see how our accuracy has gradually changed after Hyperparameter tuning. 
	
										

# M. Model Deployment:
Tools:  Flask, HTML,CSS, Heroku 

![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/Deploy1.png)

	Input:
	Date, Sentiment Analysis, Open, Close, Higher Price, Lower Price, Content Length, Close


![alt text](https://github.com/bidhyapokharel/Predict-Market-Volatility/blob/master/Documentation-Report/deployresult.png)

	Output:
	Gives the predicted output from the trained model in the form of Profit/Loss.



# N. Model Conclusion:

  Conditions which have the following characteristics:
  a. Having HIGH opening price itself;
  b. High Volume;
  c. Positive Sentiment Analysis;
  d. Lengthy/Informative Detailed comments;
  are likely to lead us to profit.
  
  
  
# O. What can we do?

1.  Publish more Positive Contents ;
2. Promote more detailed and informative contents
3. Reduce/Remove the negative contents from Social Media asap if found. 



# P. Limitations and Next Step:

1. Only applied Logistic Regression:
   Apply and compare other tuned performance.


2.  Used only Reddit’s API:
    Collect API from as much as resources possible.
	
