Attention is all you need paper introduces a different method of NLP, it encompases architecture of the model known as transformer in this paper. This paper gives a comparison to existing models of cnn, gans and rans. This paper also describes the dataset and the training procedure of the model and its performance.

The model intakes some string as input, encodes it, then starts with its attention mechanism, with a weighted nodes provide an attention value to all the encoded words in the string input, this will create a matrix of size nxn where n is the word length of the string. But since half of the matrix values are same indicating a symetric matrix. so n*n/2.

now this is processed x number of times with variating weight values between different attention head. the result of each heads is put together using do product.
Attention(Q, K, V ) = softmax(QKT√dk)V

the values Q: query,K key and V value are like dictinary in python, and softmax means here, that for all the values in the results of attention, softmax will adjust max to 1 and minimum to 0.
thus resulting in a grid which indicates which of the words showcase attention to which word from each attention head.

at the end the decoder will decode the final vectors back into readable words.
Looking at the who structure from above gives us an understanding that the encoder can provide a vectorized and attention calculated list of numbers to us, whereas the decorder block decodes this list of numbers into something understadable.
one of the few examples of how its useful is, for translating human languages, like we have one dataset of english to german or x to y pattern of language conversion. This can be used to train the model and gain weights for model, so that when we wish to translate between x and y, those previous weights are usefull.

multi headed attention, this is a technique in this paper, where it allocates the same encoded matrix to multiple differently weighted nodes. I still lack the understanding of these nodes but, overview there are not much different from cnn nodes or general perceptrons

attention mechanism help model improve performance, means it knows which words refer what in-context to the input.
multi headed mech boosts the speed of training by processing each head in parallel
The magical number of 6 for the number of encoders and decoders (which can be also be called multi heads, smarter than ravan with 10 heads, but less confused than vishnu with millions) coinciding len('google') == 6. and it beats google nueral machine translations.
