



def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score            

if __name__ == "__main__":
    # matchingWords("This is Good", "Python is Good")  

    sentences = ["Python is a good", "This is Snake", "Khand is a good boy", "Subscribe to code2hell"]

    query = input("Please enter the query string\n")
    scores = [matchingWords(query, sentence) for sentence in sentences] 
    
    # print(scores) 
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse = True)]
    
    print(f"{len(sortedSentScore)} result found!\n")
    
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a sorted {score}")