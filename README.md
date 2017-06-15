[![Build Status](https://travis-ci.org/KrzysztofSakowski/bioinf.svg?branch=master)](https://travis-ci.org/KrzysztofSakowski/bioinf/)

# Academy project for bioinformatics course
## Subject: gplmDCA
### Description:
Implementacja algorytmu gplmDCA. Dostępny kod wzorcowy w matlabie.
Artykuł opisujący metodę: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4191875/
Program w matlabie: http://gplmdca.aurell.org/


# Notes:
* https://docs.scipy.org/doc/scipy/reference/optimize.minimize-bfgs.html
* Typical call for matlab function : gplmDCA_asymmetric('fasta.fas','output.out',0.01,0.01,0.001,0.1,2,2)
* https://www.mathworks.com/help/matlab/matlab_external/table-of-mex-file-source-code-files.html - mexref
* http://cens.ioc.ee/local/man/matlab/techdoc/apiref/ - mexref

Issues:
* Possible error in calc_inverse_weights.c ? Wrong size taken.
* Differences between our and matlab implementation in calc_inverse_weights of +/- 1 in values, the sum is the same though