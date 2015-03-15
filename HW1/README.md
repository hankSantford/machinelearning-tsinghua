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

Example
-------
	
	$ python run.py data\ 1/ stopwords

	Generating feature files ..
	Starting training ..
	========== EPOCH 1 ==========
	Training sets: ['feature_s2', 'feature_s3', 'feature_s4', 'feature_s5']
	Test set: ['feature_s1']
	Precision: 0.869158878505
	Recall: 0.934673366834
	F1 score: 0.900726392252

	========== EPOCH 2 ==========
	Training sets: ['feature_s1', 'feature_s3', 'feature_s4', 'feature_s5']
	Test set: ['feature_s2']
	Precision: 0.926395939086
	Recall: 0.917085427136
	F1 score: 0.921717171717

	========== EPOCH 3 ==========
	Training sets: ['feature_s1', 'feature_s2', 'feature_s4', 'feature_s5']
	Test set: ['feature_s3']
	Precision: 0.948542024014
	Recall: 0.926298157454
	F1 score: 0.937288135593

	========== EPOCH 4 ==========
	Training sets: ['feature_s1', 'feature_s2', 'feature_s3', 'feature_s5']
	Test set: ['feature_s4']
	Precision: 0.957746478873
	Recall: 0.939698492462
	F1 score: 0.948636651871

	========== EPOCH 5 ==========
	Training sets: ['feature_s1', 'feature_s2', 'feature_s3', 'feature_s4']
	Test set: ['feature_s5']
	Precision: 0.966223132037
	Recall: 0.949698189135
	F1 score: 0.957889396246

	========== Average results ==========
	Precision: 0.933613290503
	Recall: 0.933490726604
	F1 score: 0.933251549536

Average results
---------------
	
	========== Average results ==========
	Precision: 0.933613290503
	Recall: 0.933490726604
	F1 score: 0.933251549536


