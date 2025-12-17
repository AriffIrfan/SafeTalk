grammar grammar_safetalk;

/* --- PARSER RULES (Structure) --- */
program         : statement+ EOF ;

statement       : command
                | assignment
                | conditional
                | explain_cmd
                ;

/* 1. Core Commands */
command         : verb object condition_cl? modifier? ;

/* 2. Assignment (Updated 'variable' to 'ID') */
assignment      : ('set' | 'let') ID ('to' | 'be' | '=') expression ;

/* 3. Arithmetic */
expression      : term (('+' | '-') term)* ;
term            : factor (('*' | '/' | '%') factor)* ;
factor          : NUMBER 
                | ID   
                | attribute
                | '(' expression ')' 
                ;

/* 4. Conditionals */
conditional     : 'if' logic_expr 'then' statement ('else' statement)? ;
logic_expr      : expression comparator expression ;

/* 5. Queries & Filters */
condition_cl    : 'where' attribute comparator value ;
modifier        : 'by' attribute ('ascending' | 'descending')? ;

/* 6. Values & Ambiguity */
value           : expression 
                | STRING 
                | ambiguous_term 
                ;

/* --- LEXER RULES (Vocabulary) --- */

/* Keywords */
verb            : 'find' | 'delete' | 'sort' | 'calculate' | 'archive' | 'list' ;
object          : 'files' | 'images' | 'documents' | 'folders' | 'items' ;
attribute       : 'size' | 'date' | 'type' | 'name' ;
comparator      : '>' | '<' | '==' | '!=' | '>=' | '<=' | 'equals' ;

ambiguous_term  : 'recent' | 'old' | 'huge' | 'tiny' | 'important' ;

explain_cmd     : 'explain' ('last' | 'history') ;

/* Data Types (MUST BE UPPERCASE to use Regex) */
ID              : [a-zA-Z_] [a-zA-Z0-9_]* ;  /* Renamed 'variable' to 'ID' */
NUMBER          : [0-9]+ ;
STRING          : '"' .*? '"' ;

/* Skip whitespace */
WS              : [ \t\r\n]+ -> skip ;