# questions.py

from pyke.qa import *

knows_prolog = question(
    "Do you have some familiarity with the programming language prolog?",
    yn_answer())

knows_ai = question(
    "Do you have some familiarity with artificial intelligence or expert systems?",
    yn_answer())

generic_yn = question("%s?", yn_answer())

pat_master = question(
    """Assume that the following two patterns are contained in different rules
and that none of the pattern variables are initially bound to values:

pattern 1: ((ho, $_, ($a, $a)), ($a, $a, $b), ($a, *$b))
pattern 2: ($a, $a, $x)

If the two patterns are matched together, what will $x be bound to?""",

    multiple_choice(
        ("(a, b)", 1),
        ("$a", 2),
        ("ho", 3),
        ("($a, *$b)", 4),
        ("(ho, *$b)", 5),
        ("(ho, *($a, $a))", 6),
        ("(ho, ($a, $a))", 7),
        ("(ho, $a, $a)", 8),
        ("(ho, *(ho, ho))", 9),
        ("(ho, (ho, ho))", 10),
        ("(ho, $_, (ho, ho))", 11),
        ("(ho, ho, (ho, ho))", 12),
        ("(ho, ho, ho)", 13),
        ("nothing, the two patterns don't match", 14),
        ("nothing, pattern 1 is not a legal pattern", 15),
        ("I don't have a clue...", 16)),

    enumerated_review(
        (1, "Incorrect: Neither of the symbols 'a' nor 'b' appear "
            "in either pattern."),
        (3, "Incorrect: $x is bound to a tuple."),
        (4, "Incorrect: Both pattern variables '$a' and '$b' are "
            "bound to values."),
        (5, "Incorrect: Pattern variable '$b' is bound to a value."),

        (2, "Incorrect: Pattern variable '$a' is bound to a value."),
        (6, "Incorrect: Pattern variable '$a' is bound to a value."),
        (7, "Incorrect: Pattern variable '$a' is bound to a value."),
        (8, "Incorrect: Pattern variable '$a' is bound to a value."),

        (4, "Incorrect: The '*' is part of the pattern syntax and "
            "is not seen in the bound value."),
        (6, "Incorrect: The '*' is part of the pattern syntax and "
            "is not seen in the bound value."),
        (9, "Incorrect: The '*' is part of the pattern syntax and "
            "is not seen in the bound value."),

        (10, "Incorrect: The '*' in '*$b' means "
             "\"the rest of the tuple\" is '$b'."),

        (11, "Incorrect: The '$a' in pattern 1 is "
             "a different pattern variable than\n"
             "           the '$a' in pattern 2."),
        (12, "Incorrect: The '$a' in pattern 1 is "
             "a different pattern variable than\n"
             "           the '$a' in pattern 2."),

        (13, "Correct!  Pattern 1: $a = ho and $b = (ho, ho)\n"
             "     and  Pattern 2: $a = (ho, $_, (ho, ho)), "
             "      so  $x = (ho, ho, ho)."),
        (14, "Incorrect: The patterns do match!"),
        (15, "Incorrect: Pattern 1 is a legal pattern.")))

pat_var_syntax = question(
    "A pattern variable matches any value (including other pattern variables).\n"
    "What is the syntax for a pattern variable?",
    multiple_choice(
        ("any legal identifier not within quotes is a pattern variable", 1),
        ("a '$' in front of any legal identifier", 2),
        ("a '*' in front of any legal identifier", 3)),
    enumerated_review(
        (1, "Incorrect: A legal identifier not within quotes is treated the same\n"
            "           as if it were in quotes.  This just saves you the trouble of typing\n"
            "           the quotes.\n"
            "           A pattern variable is any identifier preceded by a '$'."),
        (2, "Correct: Pattern variables are preceded by a '$'."),
        (3, "Incorrect: Pattern variables must be preceded by a '$'.")))

pat_literal = question(
    "Pattern literals are patterns that only match a single constant value.\n"
    "Which of these is NOT a pattern literal?",
    multiple_choice(
        ("None", 1),
        ("33", 2),
        ("True", 3),
        ("\"hi mom!\"", 4),
        ("fred", 5),
        ("$fred", 6)),
    enumerated_review(
        (1, "Incorrect: Simple python values, like None, are pattern literals."),
        (2, "Incorrect: Simple python values, like 33 and 3.14159, are pattern literals."),
        (3, "Incorrect: Simple python values, like True and False, are pattern literals."),
        (4, "Incorrect: Simple python values, like strings, are pattern literals."),
        (5, "Incorrect: Legal identifiers are strings that don't require quotes\n"
            "           and are pattern literals just like quoted strings are.\n"),
        (6, "Correct: Simple python values are pattern literals that only match themselves.")))

multiple_matching = question(
    "What value matches the pattern: ($a, $a)?",
    multiple_choice(
        ("44", 1),
        ("a", 2),
        ("(a, b)", 3),
        ("(b, b)", 4),
        ("(a, a, b)", 5)),
    enumerated_review(
        (1, "Incorrect: A tuple pattern only matches another tuple."),
        (2, "Incorrect: A tuple pattern only matches another tuple."),
        (3, "Incorrect: Both '$a' pattern variables must match the same value."),
        (4, "Correct: Both '$a' pattern variables must always match the same value,\n"
            "         in this case: b"),
        (5, "Incorrect: A tuple pattern only matches another tuple of the same length.")))

anonymous_syntax = question(
    "Anonymous pattern variables act like \"don't care\" patterns.\n"
    "What is the syntax for an anonymous pattern variable?",
    multiple_choice(
        ("$anonymous", 1),
        ("_anonymous", 2),
        ("Using a pattern variable name that starts with an underscore ('_'),\n"
         "like: $_anonymous.", 3)),
    enumerated_review(
        (1, "Incorrect: An anonymous pattern variable is any pattern variable\n"
            "           whose name starts with an underscore ('_')."),
        (2, "Incorrect: An anonymous pattern variable is any pattern variable\n"
            "           whose name starts with an underscore ('_')."),
        (3, "Correct!")))

rest_pattern_variable_syntax = question(
    "\"Rest\" pattern variables are used at the end of a tuple pattern to match the\n"
    "rest of the tuple.\n"
    "\n"
    "What is the syntax for an \"rest\" pattern variable?",
    multiple_choice(
        ("$rest", 1),
        ("_rest", 2),
        ("Preceding a pattern variable with an asterisk ('*'), like: *$foo.", 3)),
    enumerated_review(
        (1, "Incorrect: A \"rest\" pattern variable is any pattern variable\n"
            "preceded by an asterisk ('*')."),
        (2, "Incorrect: A \"rest\" pattern variable is any pattern variable\n"
            "           preceded by an asterisk ('*')."),
        (3, "Correct!")))

tuple_pattern_syntax = question(
    "What is the syntax for a tuple pattern?",
    multiple_choice(
        ("A series of patterns enclosed in \"tuple(\" ... \")\".", 1),
        ("A series of patterns enclosed in parenthesis.", 2)),
    enumerated_review(
        (1, "Incorrect: a tuple pattern is a series of patterns enclosed in parenthesis."),
        (2, "Correct!")))

anonymous_matching = question(
    "What value matches the pattern: ($_a, $_a)?",
    multiple_choice(
        ("44", 1),
        ("a", 2),
        ("(a, b)", 3),
        ("(a, a, b)", 4)),
    enumerated_review(
        (1, "Incorrect: a tuple pattern only matches another tuple."),
        (2, "Incorrect: a tuple pattern only matches another tuple."),
        (3, "Correct: pattern variable names that begin with an '_' are anonymous and\n"
            "         are not constrained to match the same value.\n"
            "         They serve as a \"don't care\" pattern and their name just\n"
            "         documents that value's function."),
        (4, "Incorrect: a tuple pattern only matches another tuple of the same length.")))

pattern_scope = question(
    "For each answer, assume that the two patterns are contained in different rules.\n"
    "Which set of patterns match each other?",
    multiple_choice(
        ("Pattern 1: a\n"
         "Pattern 2: 44", 1),
        ("Pattern 1: ($a, $a, 3)\n"
         "Pattern 2: (1, 2, 3)", 2),
        ("Pattern 1: ($a, $a, 3)\n"
         "Pattern 2: (1, 1, $a)", 3),
        ("Pattern 1: ($a, $a, 3)\n"
         "Pattern 2: (1, $b, $b)", 4),
        ("None of these match.", 5),
        ("I don't have a clue.", 6)),
    enumerated_review(
        (1, "Incorrect: an identifier is treated as a string, and \"a\" does not match 44."),
        (2, "Incorrect: both '$a' pattern variables in pattern 1 must match the same value."),
        (3, "Correct: All of the pattern variables with the same name within the same rule\n"
            "         must always match the same value.\n"
            "         But pattern variables with the same name within different rules\n"
            "         may match different values.  Thus all of the $a pattern variables\n"
            "         in Pattern 1 must match the same value, but this may be a different\n"
            "         value than the $a in Pattern 2."),
        (4, "Incorrect: All pattern variables with the same name in the same rule\n"
            "           must match the same value.\n"
            "           Here's the sequence of how these patterns are matched:\n"
            "           1. The first $a in Pattern 1 is matched to the 1 in Pattern 2.\n"
            "              This sets the $a in Pattern 1 to 1.\n"
            "           2. The second $a in Pattern 1 is matched to the first $b in\n"
            "              Pattern 2.  This sets $b in Pattern 2 to 1, since that is what\n"
            "              $a in Pattern 1 is set to.\n"
            "           3. The 3 in Pattern 1 is matched to the second $b in Pattern 2.\n"
            "              This tries to match 3 to 1, since $b in Pattern 2 is 1.\n"
            "              This is where the match fails!"),
        (5, "Incorrect: One set of patterns do match!")))

rest_match = question(
    """After matching the following two patterns, what is $c set to?

pattern 1: ($a, $b, *$c)
pattern 2: (1, 2, 3)
""",

    multiple_choice(
        ("3", 1),
        ("(3)", 2),
        ("(3,)", 3),
        ("nothing, the two patterns don't match", 4),
        ("nothing, pattern 1 is not a legal pattern", 5)),

    enumerated_review(
        (1, "Incorrect: a \"rest\" pattern variable is always set to a tuple."),
        (2, "Correct!  (Note that a comma is not required for singleton tuples in pyke)."),
        (3, "Correct, but answer 2 is better because a comma is not required for\n"
            "         singleton tuples in pyke."),
        (4, "Incorrect: these two patterns do match!"),
        (5, "Incorrect: pattern 1 is a legal pattern.")))

same_var_different_rules = question(
    "Assume that the following two patterns are in different rules:\n"
    "\n"
    "  Pattern 1: ($a, 2)\n"
    "  Pattern 2: (1, $a)\n"
    "\n"
    "Do these patterns match?",
    yn_answer(),
    enumerated_review(
        (True, "Correct!  The $a in Pattern 1 is in a different rule than the $a in Pattern 2,\n"
               "          so they are not required to match the same value."),
        (False, "Incorrect: The $a in Pattern 1 is in a different rule than the $a in Pattern 2,\n"
                "           so they are not required to match the same value.")))

#$x matching $y means that both $x and $y have to mean the same thing from then
#    on
#pattern matching to select what to do
#pattern matching to generate values
