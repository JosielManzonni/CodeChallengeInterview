import __future__
def first_challenge(message):
    '''Complexity in-time and space are O(n) where n is the size of original word,
    if we consider that '&32' count as 3 in len, so to be precisilly in-time O(n) and space is O(3*n*k)
    where k is the quantity of space in the original word
    '''
    return message.replace(' ','&32')

def second_challenge(correct_word, wrong_word ):
    '''As the description do not tell if is case-sensitive and others things.
    I will consider the follow premisses to solve this problem:

    1st premisse - I will consider as case-sensitive
    2st premisse - If word size is odd, I will get only integer part, that means if:
        'house' and 'uhseo' are the inputs, the 2/3 of word will be considere as 2.
    3st premisse - if word has less than 3 letter ignore and return False

    Time Complexity:
    - best case: O( 2*n/3 + 1 + 2 ) as 2*n/3 is the condition to decide if is partial-permutation, the +1 means 
    stop, becasue 2*n/3 + 1 is the condition to stop verification and the +2 is the first two if that will be runned, so we can 
    use it as O( 2*n/3 + 1 ).
    worst case: O(n) as we will ned compare all letter
    Space Complexity O(2*n) as n size of word

    '''
    correctWordSize = len(correct_word)
    wrongWordSize = len(wrong_word)
    countMiss = 0
    MINIMUM_SIZE  = 3

    #avoid unnecessary comperation
    #we can put together these first two if's but to be a clean code style I will let like that
    if correctWordSize != wrongWordSize or correctWordSize < MINIMUM_SIZE:
        return False
    if correct_word[0] != wrong_word[0]: #if first letter changed place return False
        return False

    for idx in range(1, correctWordSize):
        if correct_word[idx] != wrong_word[idx]:
            countMiss += 1
        if countMiss > (correctWordSize//3)*2:
            return False #this will avoid compare all string
    return True # if was not trigged inside that means the missspelling is less than 2/3 of word size

def third_challenge(first_word, second_word):
    '''To solve it we can use levenshtein-distance approach, using dynamic programming.

    in-time Complexity O(n*m) where n is size of first word and m size of second word.

    Normally, Levenstein-distance take Space Complexity O((n+1)*(m+1)) where n is size of first word and m size of second word
    but we can improve it and only store twice the size of first word giving us O(2*n) we can do that due we only need the current and previous 
    line, so as O(2*n) is O(n).

    Space Complexity O(n) where n is size of first word and m size of second word

    ->>>  if we have been informed the minimum size of string we could use Jaccard Approach that is computationally better than Levenshtein.
    '''
    sizeX = len(first_word)+1
    sizeY = len(second_word)+1
    
    firstComputation = [x for x in range(sizeX)]
    secondComputation = [0 for x in range(sizeX)]
    secondComputation[0] = 1
    
    for y in range(1, sizeY):
        print(firstComputation)
        for x in range(1, sizeX):
            if first_word[x-1] == second_word[y-1]:
                secondComputation[x] = firstComputation[x-1]
            else:
                minimum = min(firstComputation[x-1], firstComputation[x], secondComputation[x-1]) + 1
                secondComputation[x] = minimum
        firstComputation = secondComputation.copy()
        secondComputation[0] = secondComputation[0]+1
    return True if secondComputation[sizeX] <=1 else False  #the last value calculated is the minimum number of operations


#  def fourth_challenge() must be in android

def fifth_challenge(email_list):
    '''As it was requested only remove duplicated we can use hasmap to store the visited email thread item then when we forward to next
    we ask to hashmap: 'have I seen this before' if yes then remove.

    As wasn't explained the struct of email thread node we will assume that:
    - email item (message) is a object that contain at least the follow field: email_id
    - other fields can exist such as sender, datetime, etc...

    so email_list = [ {email_id: , sender:}, ...., {email_id: , sender:}  ] 

    In-Time Complexity  O(n)
    Space Complexity  O(n-m) where n is the size of email list and m is quantity of duplicate items are in list.

    --> other solution should be using 'set' from python3, but the solution below it is not dependent of programming language
    '''

    hashMap = {}
    idx = 0
    while idx < (len(email_list)):
        try:
            if(hashMap[email_list[idx]['email_id']]):
                del email_list[idx]
                continue
        except:
            hashMap.update( {email_list[idx]['email_id']: email_list[idx]['email_id']} )
        idx +=1
    return email_list

# def sixth_challenge(): must be in android