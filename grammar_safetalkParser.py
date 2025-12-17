# Generated from grammar_safetalk.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,0,1,0,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,3,2,53,8,2,1,2,
        3,2,56,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,66,8,4,10,4,12,4,
        69,9,4,1,5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,86,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,8,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,108,8,10,1,11,1,
        11,1,11,3,11,113,8,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,
        16,1,16,1,17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,0,11,1,0,1,2,1,0,3,5,1,0,6,7,1,0,8,10,1,0,18,19,
        1,0,20,25,1,0,26,30,1,0,31,34,1,0,35,41,1,0,42,46,1,0,48,49,124,
        0,37,1,0,0,0,2,47,1,0,0,0,4,49,1,0,0,0,6,57,1,0,0,0,8,62,1,0,0,0,
        10,70,1,0,0,0,12,85,1,0,0,0,14,87,1,0,0,0,16,95,1,0,0,0,18,99,1,
        0,0,0,20,104,1,0,0,0,22,112,1,0,0,0,24,114,1,0,0,0,26,116,1,0,0,
        0,28,118,1,0,0,0,30,120,1,0,0,0,32,122,1,0,0,0,34,124,1,0,0,0,36,
        38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,
        0,40,41,1,0,0,0,41,42,5,0,0,1,42,1,1,0,0,0,43,48,3,4,2,0,44,48,3,
        6,3,0,45,48,3,14,7,0,46,48,3,34,17,0,47,43,1,0,0,0,47,44,1,0,0,0,
        47,45,1,0,0,0,47,46,1,0,0,0,48,3,1,0,0,0,49,50,3,24,12,0,50,52,3,
        26,13,0,51,53,3,18,9,0,52,51,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,
        54,56,3,20,10,0,55,54,1,0,0,0,55,56,1,0,0,0,56,5,1,0,0,0,57,58,7,
        0,0,0,58,59,5,50,0,0,59,60,7,1,0,0,60,61,3,8,4,0,61,7,1,0,0,0,62,
        67,3,10,5,0,63,64,7,2,0,0,64,66,3,10,5,0,65,63,1,0,0,0,66,69,1,0,
        0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,9,1,0,0,0,69,67,1,0,0,0,70,75,
        3,12,6,0,71,72,7,3,0,0,72,74,3,12,6,0,73,71,1,0,0,0,74,77,1,0,0,
        0,75,73,1,0,0,0,75,76,1,0,0,0,76,11,1,0,0,0,77,75,1,0,0,0,78,86,
        5,51,0,0,79,86,5,50,0,0,80,86,3,28,14,0,81,82,5,11,0,0,82,83,3,8,
        4,0,83,84,5,12,0,0,84,86,1,0,0,0,85,78,1,0,0,0,85,79,1,0,0,0,85,
        80,1,0,0,0,85,81,1,0,0,0,86,13,1,0,0,0,87,88,5,13,0,0,88,89,3,16,
        8,0,89,90,5,14,0,0,90,93,3,2,1,0,91,92,5,15,0,0,92,94,3,2,1,0,93,
        91,1,0,0,0,93,94,1,0,0,0,94,15,1,0,0,0,95,96,3,8,4,0,96,97,3,30,
        15,0,97,98,3,8,4,0,98,17,1,0,0,0,99,100,5,16,0,0,100,101,3,28,14,
        0,101,102,3,30,15,0,102,103,3,22,11,0,103,19,1,0,0,0,104,105,5,17,
        0,0,105,107,3,28,14,0,106,108,7,4,0,0,107,106,1,0,0,0,107,108,1,
        0,0,0,108,21,1,0,0,0,109,113,3,8,4,0,110,113,5,52,0,0,111,113,3,
        32,16,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,0,0,0,113,23,1,
        0,0,0,114,115,7,5,0,0,115,25,1,0,0,0,116,117,7,6,0,0,117,27,1,0,
        0,0,118,119,7,7,0,0,119,29,1,0,0,0,120,121,7,8,0,0,121,31,1,0,0,
        0,122,123,7,9,0,0,123,33,1,0,0,0,124,125,5,47,0,0,125,126,7,10,0,
        0,126,35,1,0,0,0,10,39,47,52,55,67,75,85,93,107,112
    ]

class grammar_safetalkParser ( Parser ):

    grammarFileName = "grammar_safetalk.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'set'", "'let'", "'to'", "'be'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'if'", 
                     "'then'", "'else'", "'where'", "'by'", "'ascending'", 
                     "'descending'", "'find'", "'delete'", "'sort'", "'calculate'", 
                     "'archive'", "'list'", "'files'", "'images'", "'documents'", 
                     "'folders'", "'items'", "'size'", "'date'", "'type'", 
                     "'name'", "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", 
                     "'equals'", "'recent'", "'old'", "'huge'", "'tiny'", 
                     "'important'", "'explain'", "'last'", "'history'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_command = 2
    RULE_assignment = 3
    RULE_expression = 4
    RULE_term = 5
    RULE_factor = 6
    RULE_conditional = 7
    RULE_logic_expr = 8
    RULE_condition_cl = 9
    RULE_modifier = 10
    RULE_value = 11
    RULE_verb = 12
    RULE_object = 13
    RULE_attribute = 14
    RULE_comparator = 15
    RULE_ambiguous_term = 16
    RULE_explain_cmd = 17

    ruleNames =  [ "program", "statement", "command", "assignment", "expression", 
                   "term", "factor", "conditional", "logic_expr", "condition_cl", 
                   "modifier", "value", "verb", "object", "attribute", "comparator", 
                   "ambiguous_term", "explain_cmd" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    ID=50
    NUMBER=51
    STRING=52
    WS=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(grammar_safetalkParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammar_safetalkParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammar_safetalkParser.StatementContext,i)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grammar_safetalkParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737554423814) != 0)):
                    break

            self.state = 41
            self.match(grammar_safetalkParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(grammar_safetalkParser.CommandContext,0)


        def assignment(self):
            return self.getTypedRuleContext(grammar_safetalkParser.AssignmentContext,0)


        def conditional(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ConditionalContext,0)


        def explain_cmd(self):
            return self.getTypedRuleContext(grammar_safetalkParser.Explain_cmdContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = grammar_safetalkParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.command()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.assignment()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.conditional()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.explain_cmd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self):
            return self.getTypedRuleContext(grammar_safetalkParser.VerbContext,0)


        def object_(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ObjectContext,0)


        def condition_cl(self):
            return self.getTypedRuleContext(grammar_safetalkParser.Condition_clContext,0)


        def modifier(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ModifierContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = grammar_safetalkParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.verb()
            self.state = 50
            self.object_()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 51
                self.condition_cl()


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 54
                self.modifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammar_safetalkParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = grammar_safetalkParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 58
            self.match(grammar_safetalkParser.ID)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 60
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammar_safetalkParser.TermContext)
            else:
                return self.getTypedRuleContext(grammar_safetalkParser.TermContext,i)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = grammar_safetalkParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.term()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 63
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 64
                self.term()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammar_safetalkParser.FactorContext)
            else:
                return self.getTypedRuleContext(grammar_safetalkParser.FactorContext,i)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = grammar_safetalkParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.factor()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 71
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 72
                self.factor()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(grammar_safetalkParser.NUMBER, 0)

        def ID(self):
            return self.getToken(grammar_safetalkParser.ID, 0)

        def attribute(self):
            return self.getTypedRuleContext(grammar_safetalkParser.AttributeContext,0)


        def expression(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = grammar_safetalkParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_factor)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(grammar_safetalkParser.NUMBER)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(grammar_safetalkParser.ID)
                pass
            elif token in [31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.attribute()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.match(grammar_safetalkParser.T__10)
                self.state = 82
                self.expression()
                self.state = 83
                self.match(grammar_safetalkParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_expr(self):
            return self.getTypedRuleContext(grammar_safetalkParser.Logic_exprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammar_safetalkParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammar_safetalkParser.StatementContext,i)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = grammar_safetalkParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(grammar_safetalkParser.T__12)
            self.state = 88
            self.logic_expr()
            self.state = 89
            self.match(grammar_safetalkParser.T__13)
            self.state = 90
            self.statement()
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(grammar_safetalkParser.T__14)
                self.state = 92
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammar_safetalkParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammar_safetalkParser.ExpressionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ComparatorContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_logic_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_expr" ):
                listener.enterLogic_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_expr" ):
                listener.exitLogic_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_expr" ):
                return visitor.visitLogic_expr(self)
            else:
                return visitor.visitChildren(self)




    def logic_expr(self):

        localctx = grammar_safetalkParser.Logic_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logic_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.expression()
            self.state = 96
            self.comparator()
            self.state = 97
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_clContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(grammar_safetalkParser.AttributeContext,0)


        def comparator(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ComparatorContext,0)


        def value(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ValueContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_condition_cl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_cl" ):
                listener.enterCondition_cl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_cl" ):
                listener.exitCondition_cl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_cl" ):
                return visitor.visitCondition_cl(self)
            else:
                return visitor.visitChildren(self)




    def condition_cl(self):

        localctx = grammar_safetalkParser.Condition_clContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition_cl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(grammar_safetalkParser.T__15)
            self.state = 100
            self.attribute()
            self.state = 101
            self.comparator()
            self.state = 102
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(grammar_safetalkParser.AttributeContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifier" ):
                return visitor.visitModifier(self)
            else:
                return visitor.visitChildren(self)




    def modifier(self):

        localctx = grammar_safetalkParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(grammar_safetalkParser.T__16)
            self.state = 105
            self.attribute()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==19:
                self.state = 106
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(grammar_safetalkParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(grammar_safetalkParser.STRING, 0)

        def ambiguous_term(self):
            return self.getTypedRuleContext(grammar_safetalkParser.Ambiguous_termContext,0)


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = grammar_safetalkParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 31, 32, 33, 34, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.expression()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(grammar_safetalkParser.STRING)
                pass
            elif token in [42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.ambiguous_term()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_verb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb" ):
                listener.enterVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb" ):
                listener.exitVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = grammar_safetalkParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = grammar_safetalkParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374784) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = grammar_safetalkParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = grammar_safetalkParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4363686772736) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ambiguous_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_ambiguous_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmbiguous_term" ):
                listener.enterAmbiguous_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmbiguous_term" ):
                listener.exitAmbiguous_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAmbiguous_term" ):
                return visitor.visitAmbiguous_term(self)
            else:
                return visitor.visitChildren(self)




    def ambiguous_term(self):

        localctx = grammar_safetalkParser.Ambiguous_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ambiguous_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 136339441844224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explain_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return grammar_safetalkParser.RULE_explain_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplain_cmd" ):
                listener.enterExplain_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplain_cmd" ):
                listener.exitExplain_cmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplain_cmd" ):
                return visitor.visitExplain_cmd(self)
            else:
                return visitor.visitChildren(self)




    def explain_cmd(self):

        localctx = grammar_safetalkParser.Explain_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_explain_cmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(grammar_safetalkParser.T__46)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





