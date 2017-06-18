#include <math.h>
#include "mex.h"

/*
Copyright 2012 - by Magnus Ekeberg (magnus.ekeberg@gmail.com)
All rights reserved

Permission is granted for anyone to copy, use, or modify this
software for any uncommercial purposes, provided this copyright 
notice is retained, and note is made of any changes that have 
been made. This software is distributed without any warranty, 
express or implied. In no event shall the author or contributors be 
liable for any damage arising out of the use of this software.

The publication of research using this software, modified or not, must include an 
appropriate citation to:
M. Ekeberg, C. Lövkvist, Y. Lan, M. Weigt, E. Aurell, Improved contact
prediction in proteins: Using pseudolikelihoods to infer Potts models, Phys. Rev. E 87, 012707 (2013) 
*/

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
	/* variables */

	int i, j, n, nInstances, nNodes, *y;
	double id, *m,*threshold;
    
	/* input */

	y = (int*)mxGetPr(prhs[0]);
	threshold = mxGetPr(prhs[1]);
    
	/* compute sizes */
<<<<<<< HEAD
	nInstances = mxGetDimensions(prhs[0])[1];
	nNodes = mxGetDimensions(prhs[0])[0];
=======
	nInstances = mxGetDimensions(prhs[0])[0];
	nNodes = mxGetDimensions(prhs[0])[1];
>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0

	/*output*/
	plhs[0] = mxCreateDoubleMatrix(nInstances, 1, mxREAL);
	m = mxGetPr(plhs[0]);

	for(i=0;i < nInstances;i++) {
		m[i]+=1;
		for(j=i+1;j < nInstances;j++) {
			id=0;
			for(n=0;n < nNodes;n++) {
				if(y[i+n*nInstances]==y[j+n*nInstances]) {
					id+=1;
				}	
			}
			if(id>=((1-threshold[0])*nNodes)) {
				m[i]+=1;
				m[j]+=1;
			}	
		}	
<<<<<<< HEAD
    	}
    
=======
    	}	
>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0
}
