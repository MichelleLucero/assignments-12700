

def madlib(s):
    nouns = ['dog', 'hole','park']
    verbs = ['walked','ran','jumped']
    adj = ['gray']
    story = s
    numnouns = story.count('NOUN')
    numverbs = story.count('VERB')
    numadj = story.count('ADJ')

    for i in range(numnouns):
        story.replace('NOUN',nouns[i])
        print('g')
        
    for i in range(numverbs):
        story.replace('VERB',verbs[i])

    for i in range(numadj):
        story.replace('ADJ',adj[i])

    return story
s = "You VERB out to the NOUN. You VERB a NOUN. Then you VERB into a ADJ NOUN."

print(madlib(s))