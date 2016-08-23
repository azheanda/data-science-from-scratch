import pymongo
import datetime

def generate_training_set():
	client = pymongo.MongoClient()
	db = client.hackernews_database
	titlesByDate = db.titlesByDate
	trainingSet = db.trainingSet

	beginDate = datetime.date(2011, 3, 25).strftime("%Y-%m-%d")
	endDate = datetime.date(2011, 4, 4).strftime("%Y-%m-%d")

	for record in titlesByDate.find({"date" : {"$lte": endDate, "$gte": beginDate}}):
		for title in record.get("titles"):
			interesting_to_ethan = raw_input("Are you interested in this news: " + title.encode('utf-8') + "?(1/0, 1-yes, 0-no)")
			trainingSet.insert_one({"title": title, "is_interesting": interesting_to_ethan == '1'})

def get_training_set():
	client = pymongo.MongoClient()
	db = client.hackernews_database
	t_set = []
	for record in db.trainingSet.find():
		t_set.append((record['title'], record['is_interesting']))
	return t_set