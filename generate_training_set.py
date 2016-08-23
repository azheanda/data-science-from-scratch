import pymongo
import datetime

beginDate = datetime.date(2011, 3, 25).strftime("%Y-%m-%d")
endDate = datetime.date(2011, 4, 4).strftime("%Y-%m-%d")

def generate_training_set(beginDate, endDate):
	client = pymongo.MongoClient()
	db = client.hackernews_database
	titlesByDate = db.titlesByDate
	trainingSet = db.trainingSet

	for record in titlesByDate.find({"date" : {"$lte": endDate, "$gte": beginDate}}):
		for title in record.get("titles"):
			interesting_to_ethan = raw_input("Are you interested in this news: " + title.encode('utf-8') + "?(1/0, 1-yes, 0-no)")
			trainingSet.insert_one({"title": title, "is_interesting": interesting_to_ethan == '1'})

	print "All titles between {0} and {1} have been processed.".format(beginDate, endDate)


def generate_training_set_randomly():
	client = pymongo.MongoClient()
	db = client.hackernews_database
	titlesByDate = db.titlesByDate
	trainingSet = db.trainingSet

	titles_already_seen = get_training_titles()
	for record in titlesByDate.find():
		for title in record.get("titles"):
			if title not in titles_already_seen:
				interesting_to_ethan = raw_input(title.encode('utf-8') + ". Interested?(1/0, 1-yes, 0 or nothing-no)\n")
				trainingSet.insert_one({"title": title, "is_interesting": interesting_to_ethan == '1'})
	
	print "All titles have been processed."



def get_training_set():
	client = pymongo.MongoClient()
	db = client.hackernews_database
	t_set = []
	for record in db.trainingSet.find():
		t_set.append((record['title'], record['is_interesting']))
	return t_set

def get_training_titles():
	return [title for title, _ in get_training_set()]