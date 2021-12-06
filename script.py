import csv
from collections import defaultdict

'''
returns votes[[]] given csv filename
'''
def import_csv(csv_filename):
    '''converts string to int'''
    def parse_reply(text):
        parser_dict = {
            "1st Choice": 1,
            "2nd Choice": 2,
            "3rd Choice": 3,
            "4th Choice": 4,
            "5th Choice": 5,
            "6th Choice": 6,
            "7th Choice": 7,
            "8th Choice": 8
        }

        return parser_dict.get(text)


    file = open(csv_filename)
    csvreader = csv.reader(file)
    ''' sanity prints '''
    # header = []
    # header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    votes = []
    for row in rows[1:]: #[1:] because removing header
        vote = []
        for i in range(2, len(row)):
            vote.append(parse_reply(row[i]))

        votes.append(vote)

    # sanity prints
    # print(rows)
    # print("VOTES: ")
    # print(votes)
    return votes


'''
    calculates golf scores given input of votes
'''
def calc_golf_scores(all_candidates, votes):
    candidates = defaultdict(int) # key: candidate name, value: score
    # sum scores
    for vote in votes:
        rank = 1
        for person in vote:
            candidates[person] += rank
            rank += 1

    sorted_candidates = sorted(candidates.items(), key=lambda x: x[1])
    formatted_candidates = list(map(lambda x: (all_candidates[x[0]], x[1]), sorted_candidates))
    print("GOLF SCORES: ", formatted_candidates)
    return sorted_candidates

'''
    calculates golf scores for a given input of votes
    returns top candidate(s) with lowest score
'''
def calc_top_candidates(all_candidates, votes):
    # grab & return top candidate(s), inclusive of ties
    sorted_candidates = calc_golf_scores(all_candidates, votes)
    top_candidate_score = sorted_candidates[0][1]
    top_candidates = list()
    for candidate in sorted_candidates:
        if candidate[1] <= top_candidate_score:
            top_candidates.append(candidate[0])
        else:
            return top_candidates
    
    return top_candidates

'''
    calc_candidate_ordering takes in a list of votes and returns an ordered list of 
    (candidate name, which round they got selected).

    selection algorithm:
    (1) golf score all candidates based off summing rankings
    (2) take top candidate(s) from golf score and add to ordered list
    (3) update people's rankings by removing these candidates from their rankings
    (4) repeat steps 2-3 until no candidates remain 
'''
def calc_candidate_ordering(all_candidates, votes):
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
    for i in range(max_num_iterations):
        # step 1
        top_candidates = calc_top_candidates(all_candidates, votes)
        for candidate in top_candidates:
            # step 2
            sorted_candidates.append((all_candidates.get(candidate), i + 1))

            # step 3
            votes = remove_candidate_from_votes(votes, candidate)

            # edge case
            if votes_is_empty(votes):
                return sorted_candidates

    return sorted_candidates

'''
    sanity check with golf scores
'''
def sanity_golfscore_check(all_candidates, votes):
    candidates = calc_golf_scores(all_candidates, votes)
    print(candidates)
        






'''
ACTUAL RESULTS
BADAM TSSSSSSSSSSSSSSSSSSSS
'''
# TODO: Update this ordering if needed!
director_votes = import_csv('director.csv')
director_candidates = {
    1: "Christina Lu",
    2: "Grace Jiang",
    3: "Janice Kim",
    4: "Jimmy Ren"
}
# sanity_golfscore_check(director_candidates, director_votes)
candidate_ordering = calc_candidate_ordering(director_candidates, director_votes)
print(candidate_ordering)


# TODO: Update this ordering if needed!
vp_votes = import_csv('vp.csv')
vp_candidates = {
    1: "Andrew Jiang",
    2: "Claire Zhang",
    3: "Ethan Zhao",
    4: "Janice Kim",
    5: "Jimmy Ren",
    6: "Marcel Kida",
    7: "Subin Kim",
    8: "Yuhan Liu"
}
# sanity_golfscore_check(vp_candidates, vp_votes)
candidate_ordering = calc_candidate_ordering(vp_candidates, vp_votes)
print(candidate_ordering)



'''
    test cases
'''
def run_all_tests():
    def test1():
        votes = [["apple", "bob", "cat", "dog"], ["cat", "dog", "apple", "bob"]]
        candidate_ordering = calc_candidate_ordering(votes)
        print(candidate_ordering)

    def test2():
        votes = [["apple", "bob", "cat", "dog"], ["cat", "dog", "apple", "bob"], ["apple", "bob", "cat", "dog"]]
        candidate_ordering = calc_candidate_ordering(votes)
        print(candidate_ordering)

    test1()
    test2()

# run_all_tests()