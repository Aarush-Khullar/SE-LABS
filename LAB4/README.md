Name – Aarush Khullar

SRN – PES2UG24CS014

Issues in code:

1. The Chain-Merge Bug (slide_line): The current implementation keeps merging identical tiles consecutively if there are more than two in a row (e.g., merging [2, 2, 2, 2] all the way into [16, 0, 0, 0] instead of [4, 4, 0, 0]). In standard 2048 rules, a single tile can only merge once per move. 
2. Missing Score Tracking: The self.score variable is initialized to 0, but it is never updated when tiles combine.
