<<<<<<< HEAD
function [y] = precondUpper(r,U)
=======
function [y] = precondUpper(r,U)
>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0
y = U \ (U' \ r);