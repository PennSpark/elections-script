from collections import defaultdict

# TODO: import from csv here
votes = [[]] # list of pref lists

'''
    calculates golf scores for a given input of votes
    returns top candidate(s) with lowest score
'''
def calc_golf_scores(votes):
    candidates = defaultdict(int) # key: candidate name, value: score
    # sum scores
    for vote in votes:
        rank = 1
        for person in vote:
            candidates[person] += rank
            rank += 1

    # grab & return top candidate(s), inclusive of ties
    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1])
    top_candidate_score = sorted_candidates[0][1]
    top_candidates = list()
    for candidate in sorted_candidates:
        if candidate[1] <= top_candidate_score:
            top_candidates.append(candidate[0])
        else:
            return top_candidates
    
    return top_candidates

'''
    calc_top_candidates takes in a list of votes and returns an ordered list of 
    (candidate name, which round they got selected).

    selection algorithm:
    (1) golf score all candidates based off summing rankings
    (2) take top candidate(s) from golf score and add to ordered list
    (3) update people's rankings by removing these candidates from their rankings
    (4) repeat steps 2-3 until no candidates remain 
'''
def calc_top_candidates(votes):
    # helper function to remove selected candidates 
    def remove_candidate_from_votes(votes, candidate):
        for vote in votes:
            vote.remove(candidate)
        return votes

    # helper function for when votes is empty (reached max iteration)
    def votes_is_empty(votes):
        return len(votes[0]) == 0

    sorted_candidates = list()
    max_num_iterations = len(votes[0])

    # step 4
    for i in range(1, max_num_iterations):
        # step 1
        top_candidates = calc_golf_scores(votes)
        for candidate in top_candidates:
            # step 2
            sorted_candidates.append((candidate, i))

            # step 3
            votes = remove_candidate_from_votes(votes, candidate)

            # edge case
            if votes_is_empty(votes):
                return sorted_candidates

    return sorted_candidates
        
candidate_ordering = calc_top_candidates(votes)
print(candidate_ordering)


'''
    test cases
'''
def run_all_tests():
    def test1():
        votes = [["apple", "bob", "cat", "dog"], ["cat", "dog", "apple", "bob"]]
        candidate_ordering = calc_top_candidates(votes)
        print(candidate_ordering)

    def test2():
        votes = [["apple", "bob", "cat", "dog"], ["cat", "dog", "apple", "bob"], ["apple", "bob", "cat", "dog"]]
        candidate_ordering = calc_top_candidates(votes)
        print(candidate_ordering)

    test1()
    test2()

# run_all_tests()