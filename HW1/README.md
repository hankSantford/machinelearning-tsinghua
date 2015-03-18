HW1
===

__Name:__ 梁俊雄 Richard Luong
__Student-ID:__ 2014403075

How to run
----------

1. Unzip `HW1.zip`
2. Run following command

```$ python run.py <data set> <stopwords file>```

Replace `<data set>` and `<stopwords file>` with paths to the data set and a list of stopwords respectively.

How the features are extracted
------------------------------

The features are extracted for each non-stopword word in a tokenized document. The value of the feature is based on [TD-IDF](http://en.wikipedia.org/wiki/Tf%E2%80%93idf) with the specific form as follows:

	value = log(word frequency + 1) * log(#documents / # documents where word occurs) 

Example
-------
	
	$ python run.py data\ 1/ stopwords

	Generating feature files ..
	Starting training ..
	========== EPOCH 1 ==========
	Training sets: ['features_s2', 'features_s3', 'features_s4', 'features_s5']
	Test set: ['features_s1']
	Precision: 0.9375
	Recall: 0.904522613065
	F1 score: 0.920716112532

	========== EPOCH 2 ==========
	Training sets: ['features_s1', 'features_s3', 'features_s4', 'features_s5']
	Test set: ['features_s2']
	Precision: 0.950248756219
	Recall: 0.959798994975
	F1 score: 0.955

	========== EPOCH 3 ==========
	Training sets: ['features_s1', 'features_s2', 'features_s4', 'features_s5']
	Test set: ['features_s3']
	Precision: 0.973684210526
	Recall: 0.929648241206
	F1 score: 0.951156812339

	========== EPOCH 4 ==========
	Training sets: ['features_s1', 'features_s2', 'features_s3', 'features_s5']
	Test set: ['features_s4']
	Precision: 0.959595959596
	Recall: 0.954773869347
	F1 score: 0.95717884131

	========== EPOCH 5 ==========
	Training sets: ['features_s1', 'features_s2', 'features_s3', 'features_s4']
	Test set: ['features_s5']
	Precision: 0.965
	Recall: 0.974747474747
	F1 score: 0.969849246231

	========== Average results ==========
	Precision: 0.957205785268
	Recall: 0.944698238668
	F1 score: 0.950780202482

Average results
---------------
	
	========== Average results ==========
	Precision: 0.957205785268
	Recall: 0.944698238668
	F1 score: 0.950780202482


