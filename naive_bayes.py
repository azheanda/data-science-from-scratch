from collections import defaultdict
import re

def count_words(training_set):
	"""training_set contains pairs (title, interesting_to_ethan)"""
	word_counts = defaultdict(lambda: [0, 0])
	for title, interesting_to_ethan in training_set:
		for word in tokenize(title):
			word_counts[word][1 if interesting_to_ethan else 0] += 1
	return word_counts

def tokenize(message):
	message = message.lower()
	all_words = re.findall('[a-z0-9]+', message)
	return set(all_words)


def word_probabilities(word_counts, total_interesting_messages, total_non_interesting_messages, k=1):
	"""calculating triplets (word, P(word|interesing_to_ethan), P(word|~interesting_to_ethan))"""
	return [ word,
	  (interesting + k) / (total_interesting_messages + 2*k),    #don't forget k
	  (non_interesting + k) / (total_non_interesting_messages + 2*k),
	  for word, (interesting, non_interesting) in word_counts.iteritems()]

def interesting_probablity(word_probs, message):
	message_words = tokenize(message)
	log_prob_if_interesting = log_prob_if_not_interesting = 0.0

	for word, prob_if_interesting, prob_if_not_interesting in word_probs:
		if word in message_words:
			log_prob_if_interesting += math.log(prob_if_interesting)
			log_prob_if_not_interesting += math.log(prob_if_not_interesting)
		else 
			log_prob_if_interesting += math.log(1-prob_if_interesting)
			log_prob_if_not_interesting += math.log(1-prob_if_not_interesting)

	prob_if_interesting = math.exp(log_prob_if_interesting)
	prob_if_not_interesting = math.exp(log_prob_if_not_interesting)
	return prob_if_interesting/(prob_if_interesting + prob_if_not_interesting) #assuming prob of interesting and prob of non-interesting is the same

class NaiveBayesClassifier:
	def _init_(self, k = 1):
		self.k = k
		self.word_probs = []

	def train(self, training_set):
		num_interesting = len([])
