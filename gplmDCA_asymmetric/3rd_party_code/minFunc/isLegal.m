<<<<<<< HEAD
function [legal] = isLegal(v)
=======
function [legal] = isLegal(v)
>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0
legal = sum(any(imag(v(:))))==0 & sum(isnan(v(:)))==0 & sum(isinf(v(:)))==0;