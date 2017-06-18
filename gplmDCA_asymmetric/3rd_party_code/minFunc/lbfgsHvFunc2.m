<<<<<<< HEAD
function Hv = lbfgsHvFunc2(v,Hdiag,N,M)
=======
function Hv = lbfgsHvFunc2(v,Hdiag,N,M)
>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0
Hv = v/Hdiag - N*(M\(N'*v));