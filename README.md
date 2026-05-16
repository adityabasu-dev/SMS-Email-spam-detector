# SMS/Email Spam Detector

A machine learning web app that classifies messages as spam or not spam.
Built with BernoulliNB and deployed using Streamlit.


## Results

| Metric | Score |
|--------|-------|
| Accuracy | 98.3% |
| Precision | 99.1% |
| Recall | 88.0% |
| F1 Score | 93.0% |

> Dataset is imbalanced (87% ham / 13% spam).
> Precision prioritized over accuracy as primary metric.

## How it works
1. Input message is lowercased and tokenized
2. Stopwords and punctuation removed
3. Words reduced to root form using Porter Stemmer
4. Transformed using TF-IDF vectorizer (max_features=3000)
5. BernoulliNB model predicts spam or not spam

## Model Selection
Compared 3 Naive Bayes variants — GaussianNB, MultinomialNB, BernoulliNB.
BernoulliNB selected for best F1 score (0.93) on spam class.
Ensemble methods (voting, stacking) tested but showed no significant 
improvement over standalone BernoulliNB.

## Known Limitations
Trained on UCI SMS Spam Collection dataset (pre-2012).
May misclassify modern phishing patterns such as toll alerts,
delivery scams, and OTP fraud not present in training data.

## Dataset
UCI SMS Spam Collection — via Kaggle

## Stack
- Python
- scikit-learn
- NLTK
- Streamlit
- Pandas, NumPy