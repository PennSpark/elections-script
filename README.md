# elections

this page is still being updated !

**voting process**:
- everyone ranks candidates in order of preference
- candidate selection algo works so that "strategic voting" is minimized – just give an honest ranking of candidate preferences

**selection process**:
- candidates will be ordered by lowest "golf score" rankings through an iterative process
    - each iteration, the lowest golf score candidate(s) will be chosen and added to an ordered list of top candidates
    - selected candidate(s) will be removed from everyone's rankings list
    - process repeats until all candidates are added to the ordered list
- in the same order of the ordered list of top candidates, roles be assigned based off highest candidate preferences until all roles are filled
    - eg: if the ordered candidates list is A > B > C > D > E > ..., then A will get their top choice role, and that role will be filled. Then, B will get their highest preferenced unfilled role. This continues until all roles are filled
    - *note*: this is different than selecting the top 4 off the ordered list and assigning roles to them, since there is a possibility that the top 4 candidates all are running for the same roles. in this case, candidates E > F ... can potentially be on board.

**notes**
- the script we're running will be open-source so people can review correctness/fairness of the script :)