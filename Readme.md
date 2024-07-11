# On the resilience of traditional AI algorithms towards poisoning attacks.
Lorena González-Manzano and Joaquin Garcia-Alfaro

(Universidad Carlos III de Madrid/ SAMOVAR, Télécom SudParis, Institut Polytechnique de Paris, Palaiseau, 91120, France)

This repository contains used data (namely computed code metrics and tokens) and complete results of the paper "On the resilience of traditional AI algorithms towards poisoning attacks. Lorena González-Manzano and Joaquin Garcia-Alfaro (submitted for evaluation)".

The metrics provided in results are the following:

    • Accuracy (acc): is a measure of the correct predictions of the model and it is the most common metric.
    
    • Precision (pre): provides the number of positive predictions well made. It is specially relevant in this proposal because a higher value minimizes FP.
    
    • Recall (rec): provides the number of positives well predicted by the model.
    
    • F1 measure (F1): refers to the harmonic mean of precision and recall, looking for the maximization of both vales in the best case.
    
    • Confusion matrix: in involves the amount of false positives (FP), negatives (FN), true positives (TP) and negatives (TN). In this case, as bad samples are labelled with 0 and good ones with 1 (recall Section VII-A), FP are the most relevant because it means that a vulnerability is missed, while FN affect usability.
    
    • Matthews Correlation Coefficient (MCC): is a measure of the quality of binary classification and produces a high score (+1 to −1) only if the prediction obtained good results in all of the four confusion matrix categories.
    
Files are the following (a reduced version is provided until acceptance):

-There are 3 .csv files (BaselineC_toGitHub/ BaselineCSHARP_toGitHub/ BaselinePHP_toGitHub) which contain baseline results of the use of VulCoT.

-"Summary_results_toGitHub.xlsx" contains all results concerning executed poisoning attacks.

-A .py file containing the general working process of AI algorithms, where MLP algorithm is used as an example.

-vulcot.sql contains tables with data used in the proposal related to SARD and Diversevul datasets - until acceptance, some csv files with data of some of the tables are provided:
 
    -codesard/codediversevul: contain the code of each sample and its identifier.
    -sard/diversevul: contain the identifier of each sample, the state (bad or good depending on being vulnerable or not) and the linked CWE (some samples may contain more than one CWE).
    -metricssard/metricsdiversevul:contain the identifier of each sample, the programing language and code metrics, namely, entropy, number of 'for', 'if' and 'while', number of lines of code and CCN.
    -tokenssard/tokensdiversevul: contain the identifier of each sample, the programing language and the computed tokens separated by **** to simplify their later processing.
    -cwe: contains the existing CWE and their description.
