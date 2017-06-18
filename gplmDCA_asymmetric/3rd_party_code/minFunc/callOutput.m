<<<<<<< HEAD
function [stop] = callOutput(outputFcn,x,state,i,funEvals,f,t,gtd,g,d,opt,varargin)

optimValues.iteration = i;
optimValues.funccount = funEvals;
optimValues.fval = f;
optimValues.stepsize = t;
optimValues.directionalderivative = gtd;
optimValues.gradient = g;
optimValues.searchdirection = d;
optimValues.firstorderopt = opt;

=======
function [stop] = callOutput(outputFcn,x,state,i,funEvals,f,t,gtd,g,d,opt,varargin)

optimValues.iteration = i;
optimValues.funccount = funEvals;
optimValues.fval = f;
optimValues.stepsize = t;
optimValues.directionalderivative = gtd;
optimValues.gradient = g;
optimValues.searchdirection = d;
optimValues.firstorderopt = opt;

>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0
stop = outputFcn(x,optimValues,state,varargin{:});