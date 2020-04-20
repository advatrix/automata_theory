# automata_theory
## Description

A finite state machine-based recognizer of strings that match patterns:

`create relation(attributes)` or `relation` or `relation join relation`

`relation` - is a string of literals, doesn't start with number

`attributes` - non-empty list of attributes, where attribute is a string of literals and it doesn't start with number.

## Structure

**generator** - generator of srings to check the program. Some strings match the patterns, others have mistakes to check recognizer's work. Uses exrex.


The recognizer is implemented three different ways:

**regex_analyzer** - regular expressions (Python module **re**)

**smc** - State Machine Compiler (Python)

**ply** - Python Lexer-Yacc

## Описание

Распознаватель строк заданного шаблона на базе конечных автоматов:

`create relation(attributes)` `relation` `relation join relation`

`relation` - строка литералов, не начинается с цифры

`attributes` - непустой список атрибутов, где атрибут - строка литералов, не начинающаяся с цифры.

## Структура

**generator** - генератор строк. Часть строк соответствует шаблонам, часть создаётся с намеренными ошибками для проверки работы распознавателя. Использует модуль **exrex**.

Распознаватель разработан тремя путями (соответствуют директориям):

**regex_analyzer** - регулярные выражения (модуль **re** Python)

**smc** - State Machine Compiler (Python)

**ply** - Python Lexer-Yacc
