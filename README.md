# Twitter-sentimental-analysis


 The project is based on Twitter sentimental analysis using Machine Learning .Find the relevant data from the sources like: Kaggle, UCI etc.
	Download the data set in .csv format from ⦁	www.kaggle.com
  
  #Steps followed to complete this project:
  * 	Download the data set in .csv format from ⦁	www.kaggle.com
	*   Import the data from the data set
  *   To authenticate and access the twitter we have used tweepy
  *   After authentiaction read the data from dataset and 
  *   Then pre process the data by sequence of characters that forms a search pattern such as Removal of Url,Smile -- :), : ), :-), (:, ( :, (-:, :'),Love -- <3, :*, 💙,username         removal,Convert more than 2 letter repetitions to 2 letter and so on..
  *   And Process data to get all the data of the tweets and,pass only tweets text to preprocess and finally returns only the processed tweets.
  *   Now divide the data sets into two parts:-
	Training data set
	Testing data set
  *   Now Implement these Machine Learning algorithms to check accuracy  -
	Multinomial Naive Bayes-Every
	Linear Classifier
	LinearSupportVectorClassifier
	Decision Tree Classifier
  * And used tkinter for gui
  *  At last show accuray of  all the models and tells the tweets are positive(good) or negative(bad).
  Compare all the models on basis of their accuracy and select the best working model for predictions.
