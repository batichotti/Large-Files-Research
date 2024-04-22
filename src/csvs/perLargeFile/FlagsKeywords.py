regex = {
    r"branch" : "Commmit Operation",
    r"merge" : "Commit Operation",
    r"revert" : "Commit Operation",

    r"build" : "Build Configuration",


    r"(?<!de)bug" : "Bug-Fix",
    r"error" : "Bug-Fix",
    r"defect" : "Bug-Fix",
    r"problem" : "Bug-Fix",
    r"failure" : "Bug-Fix",
    r"exception" : "Bug-Fix",
    r"anomaly" : "Bug-Fix",
    r"inconsistency" : "Bug-Fix",
    r"(?<!de)fault" : "Bug-Fix",
    r"flaw" : "Bug-Fix",
    r"issues? ?#?[0-9]" : "Bug-Fix",
    r"(?<!un)patch([a-z]{0,3})? ?#?[0-9]" : "Bug-Fix",
    r"fix([a-z]{0,3})? ?#?[0-9]?" : "Bug-Fix",
    r"closes? ?#?[0-9]?" : "Bug-Fix",
    r"correction" : "Bug-Fix",
    r"conflict" : "Bug-Fix",
    r"work ?around" : "Bug-Fix",
    r"incorrect" : "Bug-Fix",
    r"juggle" : "Bug-Fix ",
    r"brok([a-z]{0,5})?" : "Bug-Fix",
    r"((manner|method|approach|way|mode){1} correct[a-z]{0,3})|(correct[a-z]{0,3} (\w+ ){0,3}(manner|method|approach|way|mode))" : "Bug-Fix",

    r"new ([\w]+ ){0,3}feature" : "New Feature",
    r"new ?\(?[\w \*]+\)?" : "New Feature",
    r"add([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "New Feature",
    r"add([a-z]{0,3})? ([\w]+ ){0,3}(method([a-z]{0,3})?|funct([a-z]{0,3})?|class([a-z]{0,3})?|interfac([a-z]{0,3})?)" : "Refactoring",
    r"add ?\(?[\w \*]+\)?" : "New Feature",
    r"can now": "New Feature",
    r"includ([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "New Feature",
    r"includ([a-z]{0,3})? ([\w]+ ){0,3}(method([a-z]{0,3})?|funct([a-z]{0,3})?|class([a-z]{0,3})?|interfac([a-z]{0,3})?)" : "New Feature",
    r"creat([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "New Feature",
    r"creat([a-z]{0,3})? ([\w]+ ){0,3}(method([a-z]{0,3})?|funct([a-z]{0,3})?|class([a-z]{0,3})?|interfac([a-z]{0,3})?)" : "New Feature",
    r"implement" : "New Feature",
    r"increment" : "New Feature",
    r"feat ?\(?[\w \*]+\)?" : "New Feature",

    r"(?<!un)optimiz" : "Optimizing",

    r"re-?f([a-z]{0,3})? ? ?\(?[\w \*]+\)?#?gh?" : "Refactoring",
    r"code clean" : "Refactoring",
    r"clean([a-z]{0,3})? ?code" : "Refactoring",
    r"clean ?-?up" : "Refactoring",
    r"improve" : "Refactoring",
    r"enhanc" : "Refactoring",
    r"rework" : "Refactoring",
    r"extract([a-z]{0,3})? ([\w]+ ){0,3}(method([a-z]{0,3})?|funct([a-z]{0,3})?|class([a-z]{0,3})?|interfac([a-z]{0,3})?)" : "Refactoring",
    r"rewr[io]t" : "Refactoring",
    r"renam" : "Refactoring",
    r"refin" : "Refactoring",
    r"smarter approach" : "Refactoring",
    r"clarify" : "Refactoring",
    r"simpl([a-z]{0,3})?" : "Refactoring",
    r"revamp" : "Refactoring",
    r"decompos" : "Refactoring",
    r"adjust" : "Refactoring",
    r"tidy" : "Refactoring",
    r"chore ?\(?[\w \*]+\)?" : "Refactoring",
    r"((?<!bad)|(?<!less)|(?<!poor)|(?<!small)) ?perf(orm)? ?\(?[\w \*]+\)?" : "Refactoring",
    r"style? ?\(?[\w \*]+\)?" : "Refactoring",
    r"reimplementing": "Refactoring",
    r"unify" : "Refactoring",
    r"rerrange" : "Refactoring",

    r"(dead|unused|orphaned|unreachable|rotting|stale) ?-?code" : "Refactoring",

    r"remov([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "Refactoring",
    r"delet([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "Refactoring",
    r"destroy([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "Refactoring",
    r"kill([a-z]{0,3})? ([\w]+ ){0,3}(?!.*(?:\blibrar([a-z]{0,3})?\b|\bplugins?\b|\bfold([a-z]{0,3})?\b|\bdependenc([a-z]{0,3})?\b))" : "Refactoring",

    r"(?<!re)move([a-z]{0,3})? ([\w]+ ){0,3}(method([a-z]{0,3})?|funct([a-z]{0,3})?|class([a-z]{0,3})?|interfac([a-z]{0,3})?)" : "Refactoring",

    # "test" : "Testing",
}

keywords = {
    "branch" : "Commmit Operation",
    "merge" : "Commit Operation",
    "revert" : "Commit Operation",

    "build" : "Build Configuration",

    # "test" : "Testing",

    "bug" : "Bug-Fix",
    "error" : "Bug-Fix",
    "defect" : "Bug-Fix",
    "problem" : "Bug-Fix",
    "failure" : "Bug-Fix",
    # "fault" : "Bug-Fix",
    "flaw" : "Bug-Fix",
    "fix" : "Bug-Fix",
    "patch" : "Bug-Fix",
    "conflict" : "Bug-Fix",
    "issue" : "Bug-Fix",
    "closes" : "Bug-Fix",
    "close #" : "Bug-Fix",
    "work around" : "Bug-Fix",
    "workaround" : "Bug-Fix",
    "juggle" : "Bug-Fix ",
    "incorrect" : "Bug-Fix",
    # " #" : "Bug-Fix",

    "new feature" : "New Feature",
    "new(" : "New Feature",
    "add feature" : "New Feature",
    "enhance" : "New Feature",
    "include feature" : "New Feature",
    "create feature" : "New Feature",
    "implement" : "New Feature",
    "increment" : "New Feature",
    "feat" : "New Feature",

    "refact" : "Refactoring",
    "re-fact" : "Refactoring",
    "ref #" : "Refactoring",
    "ref gh-" : "Refactoring",
    "refct" : "Refactoring",
    "code clean" : "Refactoring",
    "clean code" : "Refactoring",
    "cleaner code" : "Refactoring",
    "clean up" : "Refactoring",
    "cleanup" : "Refactoring",
    "clean-up" : "Refactoring",
    "improve" : "Refactoring",
    "rework" : "Refactoring",
    "extract" : "Refactoring",
    "rewrit" : "Refactoring",
    "rewrot" : "Refactoring",
    "renam" : "Refactoring",
    "refin" : "Refactoring",
    "optimiz" : "Refactoring",
    "smarter approach" : "Refactoring",
    "clarify" : "Refactoring",
    "simplif" : "Refactoring",
    "simpler" : "Refactoring",
    "nicer" : "Refactoring",
    "better" : "Refactoring",
    "revamp" : "Refactoring",
    "decompose" : "Refactoring",
    "adjust" : "Refactoring",
    "tidy" : "Refactoring",
    "chore" : "Refactoring",
    "perf(" : "Refactoring",
    "style(" : "Refactoring",
    "reimplementing": "Refactoring",
    "unify" : "Refactoring",
    "rerrange" : "Refactoring",

    "dead code" : "Refactoring",
    "unused code" : "Refactoring",

    # "correct" : "Bug-Fix",
    # "correctly" : "Bug-Fix",
    # "ensure" : "Bug-Fix",
    # "assure" : "Bug-Fix",
    # "bring up" : "New feature",
    # "can now" : "New Feature",
    # "make" : "New Feature",
    # "factor" : "Refactoring",
    # "spell" : "Bug-Fix",
    # "spelling" : "Bug-Fix",
    # "assign" : "Refactoring",
    # "prevent" : "Bug-Fix",
    # "warn" : "Bug-Fix",
    # "avert" : "Refactoring",
    # "avoid" : "Refactoring",
    # "enhance" : "Refactoring",
}

'''
Palavras q eu achei q se repetem ->

closes #
perf()
feat()
chore()
include
conflict
refct()
improve
new()
code clean
clean code
clean up
cleanup
can now
make
ensure
assure
implement
adjust
issue
assign
correct
correctly
avoid
prevent
warn
avert
create
work around
workaround
incorrect
drop use
spell
spelling
refine
optimize
optimizing#
smarter approach
clarify
simplify
simpler
simplifying
nicer
better
factor
rename
tweak#
refine
juggle
implement
revamp
dead code
re-factor
re-factoring
clean-up
ref #
ref gh-
refs #
decompose
cleaner code
tidy
unused code

Palavras genericas/suspeitas q se repetem ->

revert
futher

update
upgrade
test()
test
spec
check
try
reclycle lines
rewrite
remove
delete
eliminate
destroy
move
reset
unfold
restore
delegate
ignore
wip
in development
start
finish
slice
split
disable
swap
tweak disable
separete
increment
fold
unfold
folding
migrate
inject
style()
fill in missing
use {} instead of {}
use {} in
use {} to
send back
remeber
re-apply
bump
chage
merge
merging
missed
reimplementing
unset
shortened
shorter
switch
draft
elaborate
enhance
enhancing
enhancement
inline
break
gol
ungolf
reconcile
combine
flip
diff
genarete
build
disable
release
rake convert
rearrange
bring
combine
handle
detect
verify
initial
invert
code review
insert
flush
highlight
kill
turns off
give
package up
simplifications
backout
back out
backing out
deprecate
define
drop
unify
allow
disallow
wrap
wrapped
wrapping
replace
naming
land
re-land
lint
name
naming
flush
rewrote
dropdown
clear
now {}
merge pull request #
reuse
oops
uops
'''
