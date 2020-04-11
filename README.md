# automata_theory
## Description

A finite state machine-based recognizer of strings that match patterns:

`create relation(attributes)` or `relation[ join relation]`

`relation` - is a string of literals, doesn't start with number
`attributes` - non-empty list if attribute, where attribute is a string of literals and doesn't start with number.

## Structure

**generator** - generator of srings to check the program. Some strings match the patterns, others have mistakes. Uses exrex.


The recognizer is implemented three different ways:
**regex_analyzer** - regular expressions (Python)

**smc** - State Machine Compiler (Python)

**ply** - Python Lexer-Yacc
