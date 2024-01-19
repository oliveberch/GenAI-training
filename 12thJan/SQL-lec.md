## SQL Normal Forms

### First Normal Form

Rule1: have Unique values in colomns.

### Second Normal Form

Rule1: Follows 1st normal form

Rule2: have a colomn of primary key

### Third Normal Form

Rule1: Satisfies second normal form

Rule2: Not have a transitive functional dependency

### Boyce-Codd Normal Form

Rule1: Satisfies Third normal form

Rule2: For any dependency A → B, A should be a super key, i.e, A should be a non-key attribute if B is a key attribute.