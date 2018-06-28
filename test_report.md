---
title: "Deduplication of contact information"
author: "Ignacio Arroyo Fernandez"
date: "June 28, 2018"
---

# Data exploration
The data I downloaded has a main file whose content is in CSV format. Each row
containing results and labeling provided by a baseline system based on string
distance metrics and manual annotation of each sample pair of clients. The first
field of the file is a kind of index of the associated sample. The next fields
are labeled according to the name of the distance metric and the
client information fields. These fields indicating distance metrics for each pair
of samples constitute a feature vector representing each sample pair. The last
field is the manual annotation of whether a sample pair corresponds to the same
client (1) or not (-1).

The dataset is imbalanced. That is, there are 18% of samples labeled as -1 (no
match), while the 82% remaining is labeled as 1 (matching). This condition implies
additional difficulties in the case of proposing a Machine Learning approach. In
addition, there are lots of missing values in the feature vectors.

# Modeling approach
For modeling this task I decided to use supervised learning. This is because it
is possible taking advantage of the manually labeled data. Also, it can be more
time-consuming trying to determine the importance of features in advance (an
unsupervised approach can also be effective in the case of doing feature
engineering before hand). In most cases a supervised learning algorithm can determine such importance by itself.

The supervised learning algorithm I used is a Support Vector Machine (SVM),
which performance in imbalanced datasets is good.

# Performance analysis

# Conclusions

# Potential improvements
Additional time is needed to perform a formal Exploratory Data Analysis, which can be helpful in determining the data distribution, as well as in assessing the actual impact the missing values have in modeling the learning problem.

The first potential improvement can be adding Fizzy String Matching measures to the feature vectors. Feature Selection methods are also recommended for machine learning approaches. In this case, we have a highly imbalanced dataset, and in addition we face highly imbalanced features, so Information-Theoretic feature selection methods are recommended to weigh the importance of features. Term Frequency - Inverse Document Frequency (TF-IDF) is a widely used, simple and effective method of this kind.
