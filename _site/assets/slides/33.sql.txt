---------------
-- Ancestors --
---------------

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

with
  best(dog) as (
    select "eisenhower" union
    select "barack"
  )
select parent from parents, best where child=dog;

with
  siblings(first, second) as (
    select a.child, b.child from parents as a, parents as b
           where a.parent = b.parent and a.child != b.child
  )
select child as nephew, second as uncle from parents, siblings where parent=first;

with
  ancestors(ancestor, descendent) as (
    select parent, child from parents union
    select ancestor, child from ancestors, parents where parent = descendent
  )
select ancestor from ancestors where descendent="herbert";

---------------
-- Sentences --
---------------

create table nouns as
  select "the dog" as phrase union
  select "the cat"           union
  select "the bird";

select s.phrase || " chased " || o.phrase
       from nouns as s, nouns as o
       where s.phrase != o.phrase;

with
  verbs(word) as (
    select "insulted"  union
    select "intrigued"  union
    select "ignored"
  )
select s.phrase || " " || v.word || " " || o.phrase
       from nouns as s, nouns as o, verbs as v
       where s.phrase != o.phrase;

with
  compounds(phrase, n) as (
    select phrase, 1 from nouns union
    select subject.phrase || " that chased " || object.phrase, n+1
           from compounds as subject, nouns as object
           where n < 2 and subject.phrase != object.phrase
  )
select subject.phrase || " ate " || object.phrase
    from compounds as subject, compounds as object
    where subject.phrase != object.phrase;

-------------
-- Numbers --
-------------

create table odds as
  with
    odds(n) as (
      select 1 union
      select n+2 from odds where n < 15
    )
  select n from odds

with
  i(n) as (
    select 1 union select n+1 from i where n < 20
  )
select a.n, b.n, c.n from i as a, i as b, i as c
       where a.n < b.n and a.n*a.n + b.n*b.n = c.n*c.n;

-- Fibonacci sequence
create table fibs as
  with
    fib(previous, current) as (
      select 0, 1 union
      select current, previous+current from fib
      where current <= 100
    )
  select previous from fib;

-- Arithmetic
create table pairs as
  with
    i(n) as (
      select 1 union select n+1 from i where n < 20
    )
  select a.n as x, b.n as y from i as a, i as b where a.n <= b.n;
select * from pairs where x+y = 24;
select * from pairs where x*y = 24;
select x from pairs where x = y and 24 % x = 0;

-- Interesting number: 1729 is the smallest sum of 2 cubes in 2 ways
create table interesting as
  with
    cubes(x, y, cube) as (
      select x, y, x*x*x + y*y*y from pairs
      )
  select a.cube from cubes a, cubes b
    where a.cube = b.cube and
          a.x < b.x;

