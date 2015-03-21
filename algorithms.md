# TEXT

## setup

1. read in faustroll book
2. create `froll_dict` dictionary from text
3. remove stopwords and numbers from `froll_dict`

## text algorithm

1. get query term
2. execute three functions:  

  2a. syzygy algorithm  
    1. get list of synonyms
    2. for each synonym do the following:  
      a. find hyponyms; if a hyponym occurs in `froll_dict` then add to the output list  
      b. find hypernyms; if a hypernym occurs in `froll_dict` then add to the output list  
      c. find holonyms; if a holonym occurs in `froll_dict` then add to the output list  
    3. return list of syzygy words

  2b. antinomy algorithm
    1. get list of synonyms
    2. for each synonym do the following:  
      a. find antonyms; if a antonym occurs in `froll_dict` then add to the output list
    3. return list of antinomy words

  2c. clinamen algorithm
    1. find list of words within `froll_dict` that have a `dameraulevenshtein distance` of 1 or 2 (meaning, there are 1 or 2 spelling errors)  
    2. return list of clinamen words

3. get sentences for all three output lists

  3a. if the word appears in faustroll then find the nearest 5 words before and after the word  
  3b. return list of sentences

4. render results as html


---

# IMAGES

## setup

- microsoft translate API key
- flickr API key
- (bing image search API key) - not used atm

## image algorithm

1. get query word
2. get one syzygy word using syzygy algorithm 2a above
3. translation party  
  3a. translate english to french  
  3b. translate french to japanese  
  3c. translate japanese to english  
4. get images  
  4a. search flickr for 10 matches to english translation  
  4b. get metadata for each  
  4c. add title, thumb, link to output list
5. return output list
6. render results as html

---

# VIDEOS

## setup

- microsoft translate API key
- youtube API stuff
- (bing video search API key) - not used atm

## video algorithm

1. get query word
2. get one syzygy word using syzygy algorithm
3. translation party
  3a. translate english to french
  3b. translate french to japanese
  3c. translate japanese to english
4. get videos
  4a. search YouTube for 10 matches to english translation  
  4b. get metadata for each
  4c. add title, thumb, link to output list
5. return output list
6. render as html
