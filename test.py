# It will import all the modules stored in AllImport module
from AllImport import *
# Use hashtag and classify in % how many sentiments are +ve and -ve based on fetched tweets
from tkinter import *
import time


class TwitterClient():
	def __init__(self, twitter_user=None):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()
		self.twitter_client = API(self.auth)
		self.twitter_user = twitter_user

	def get_twitter_client_api(self):
		return self.twitter_client

	def get_user_timeline_tweets(self, num_tweets):
		tweets = []
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
			tweets.append(tweet)
		return tweets

	def get_friend_list(self, num_friends):
		friend_list = []
		for friend in Cursor(self.twitter_client, id=self.twitter_user).items(num_friends):
			friend_list.append(friend)
		return friend_list

	def get_home_timeline_tweets(self, num_tweets):
		home_timeline_tweets = []
		for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
			home_timeline_tweets.append(tweet)
		return home_timeline_tweets


# To authenticate and access the twitter
class TwitterAuthenticator():

	def authenticate_twitter_app(self):
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		return auth


# get all the data of the tweets and,pass only tweets text to preprocess and finally returns only the processed tweets
def process(data):
	temp = []
	for text in data['sentence']:
		text = pp.pre_processing(text)
		temp.append(text)
	data['sentence'] = temp
	return data['sentence']


def execute():
	try:
		user = Entry1.get()
		num_tweets = w.get()
		twitter_client = TwitterClient()
		api = twitter_client.get_twitter_client_api()
		tweets = api.user_timeline(screen_name=user, count=num_tweets)
		tweets_text = []
		for tweet in tweets:
			tweets_text.append(pp.pre_processing(tweet.text))
		datafile = pd.read_csv('Train.csv', sep=',', encoding="utf-8")
		x = process(datafile)
		y = datafile['label']
		x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
		vector = CountVectorizer()
		vector.fit(x_train)
		x_train_vft = vector.transform(x_train)
		x_test_vft = vector.transform(x_test)

		count = 1
		for tweet in tweets_text:
			tweet_text = str(count)+":- "+tweet
			msg_list.insert(END,tweet_text)
			# print(count, tweet)
			count += 1
			tweet = [tweet]
			vec = vector.transform(tweet)

		# Multinomial Naive Bayes-Every feature is independent,probability is cal and highest one will be o/p,fastest
			temp = mnb.MultinomialNBAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
			msg_list.insert(END,"Multinomial Naive Bayes")
			msg_list.insert(END,temp)
			
			
			# Linear Classifier
			temp = lc.LinearClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
			msg_list.insert(END,"Linear Classifier")
			msg_list.insert(END,temp)
			
			# LinearSupportVectorClassifier-LinearSeparationOfDataHappensOptimalLineIsDrawn using margins b/w both data
			temp = lsvc.LinearSupportVectorClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
			msg_list.insert(END,"LinearSupportVectorClassifier")
			msg_list.insert(END,temp)
			
			# Decision Tree Classifier
			temp = dtc.DecisionTreeClassifierAlgo(x_train_vft, y_train, x_test_vft, y_test, vec)
			msg_list.insert(END,"Decision Tree Classifier")
			msg_list.insert(END,temp)


	except Exception as e:
		# Print the error
		print(e)

		# When reach the rate limit
		def on_limit(self, track):
			# Print rate limiting error
			print("Rate limited, continuing")
			# Continue mining tweets
			return True
		# When timed out

		def on_timeout(self):
			# Print timeout message
			print(sys.stderr, 'Timeout')
			# Wait 10 seconds
			time.sleep(10)
			# Return nothing
			return

if __name__ == "__main__":
	mainwindow = Tk()
	mainwindow.title("Twitter Sentimental Analysis Engine")
	Label(mainwindow, text="TWITTER SENTIMENTAL ANALYSIS ENGINE", bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)
	photo = PhotoImage(file="Twitterlogo.png")
	Label(mainwindow, image=photo, bg="black", fg="white").pack(side=TOP, fill=X)
	
	messages_frame = Frame(mainwindow)
	scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.
	# Following will contain the messages.
	msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
	scrollbar.pack(side=RIGHT, fill=Y,padx=2,pady=2)
	msg_list.pack(side=LEFT, fill=BOTH,padx=2,pady=2)
	msg_list.pack(padx=2,pady=2)
	messages_frame.pack()

	Label(mainwindow, text="USERNAME", bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)
	Entry1 = Entry(mainwindow)
	Entry1.pack(side=TOP, padx=2, pady=2)
	Label(mainwindow, text="NUMBER OF TWEETS", bg="black", fg="white").pack(side=TOP, fill=X, padx=2, pady=2)
	w = Scale(mainwindow, from_=1, to=10, orient=HORIZONTAL)
	w.pack(side=TOP, fill=X, padx=2, pady=2)
	But1 = Button(mainwindow, text="RUN", command=execute)
	But1.pack(side=TOP, fill=X, padx=2, pady=2)
	mainwindow.mainloop()