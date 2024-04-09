# Vulnerability detection under poisoning attacks.
Lorena González-Manzano and Joaquin Garcia-Alfaro

(Universiad Carlos III de Madrid/ SAMOVAR, Télécom SudParis, Institut Polytechnique de Paris, Palaiseau, 91120, France)

This repository contains used data (namely computed code metrics and tokens) and complete results of the paper "Vulnerability detection under poisoning attacks. Lorena González-Manzano and Joaquin Garcia-Alfaro (submitted for evaluation)".

Files are the following (a reduced version is provided until aceptance):

-There are 3 .csv files (BaselineC_toGitHub/ BaselineCSHARP_toGitHub/ BaselinePHP_toGitHub) which contain baseline results of the use of VulCoT.

-"Summary_results_toGitHub.xlsx" contains all results concerning executed poisoning attacks.

-vulcot.sql contains tables with data used in the proposal related to SARD and Diversevul datasets - Until acceptance, some csv files with data of some of the tables are provided:
 
    -codesard/codediversevul: contain the code of each sample and its identifier.
    -sard/diversevul: contain the identifier of each sample, the state (bad or good depending on being vulnerable or not) and the linked CWE (some samples may contain more than one CWE).
    -metricssard/metricsdiversevul:contain the identifier of each sample, the programing language and code metrics, namely, entropy, number of 'for', 'if' and 'while', number of lines of code and CCN.
    -tokenssard/tokensdiversevul: contain the identifier of each sample, the programing language and the computed tokens separated by **** to simplify their later processing.
    -cwe: contains the existing CWE and their description.
