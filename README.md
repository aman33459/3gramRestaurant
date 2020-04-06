# 3gramRestaurant

Probability of a sentence to occur in the given restaurant corpus('transcript.txt') using trigram model.
Trigram model with laplacian add one smoothing-P(w1,n) = P(w1) P(w2|w1) P(w3|w1,2) ... P(wn|w1,n-1). 
where P(wi|wi-1,wi-2) = cn(wi-1,wi-2,wi)/cn(wi-1,wi-2).
