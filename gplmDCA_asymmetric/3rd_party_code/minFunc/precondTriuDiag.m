<<<<<<< HEAD
function [y] = precondUpper(r,U,D)
=======
function [y] = precondUpper(r,U,D)
>>>>>>> 91d58b237e9ec315677292bfa60cc0df39bbc6d0
y = U \ (D .* (U' \ r));