# Generated from grammar_safetalk.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammar_safetalkParser import grammar_safetalkParser
else:
    from grammar_safetalkParser import grammar_safetalkParser

# This class defines a complete listener for a parse tree produced by grammar_safetalkParser.
class grammar_safetalkListener(ParseTreeListener):

    # Enter a parse tree produced by grammar_safetalkParser#program.
    def enterProgram(self, ctx:grammar_safetalkParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#program.
    def exitProgram(self, ctx:grammar_safetalkParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#statement.
    def enterStatement(self, ctx:grammar_safetalkParser.StatementContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#statement.
    def exitStatement(self, ctx:grammar_safetalkParser.StatementContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#command.
    def enterCommand(self, ctx:grammar_safetalkParser.CommandContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#command.
    def exitCommand(self, ctx:grammar_safetalkParser.CommandContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#assignment.
    def enterAssignment(self, ctx:grammar_safetalkParser.AssignmentContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#assignment.
    def exitAssignment(self, ctx:grammar_safetalkParser.AssignmentContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#expression.
    def enterExpression(self, ctx:grammar_safetalkParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#expression.
    def exitExpression(self, ctx:grammar_safetalkParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#term.
    def enterTerm(self, ctx:grammar_safetalkParser.TermContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#term.
    def exitTerm(self, ctx:grammar_safetalkParser.TermContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#factor.
    def enterFactor(self, ctx:grammar_safetalkParser.FactorContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#factor.
    def exitFactor(self, ctx:grammar_safetalkParser.FactorContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#conditional.
    def enterConditional(self, ctx:grammar_safetalkParser.ConditionalContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#conditional.
    def exitConditional(self, ctx:grammar_safetalkParser.ConditionalContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#logic_expr.
    def enterLogic_expr(self, ctx:grammar_safetalkParser.Logic_exprContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#logic_expr.
    def exitLogic_expr(self, ctx:grammar_safetalkParser.Logic_exprContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#condition_cl.
    def enterCondition_cl(self, ctx:grammar_safetalkParser.Condition_clContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#condition_cl.
    def exitCondition_cl(self, ctx:grammar_safetalkParser.Condition_clContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#modifier.
    def enterModifier(self, ctx:grammar_safetalkParser.ModifierContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#modifier.
    def exitModifier(self, ctx:grammar_safetalkParser.ModifierContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#value.
    def enterValue(self, ctx:grammar_safetalkParser.ValueContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#value.
    def exitValue(self, ctx:grammar_safetalkParser.ValueContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#verb.
    def enterVerb(self, ctx:grammar_safetalkParser.VerbContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#verb.
    def exitVerb(self, ctx:grammar_safetalkParser.VerbContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#object.
    def enterObject(self, ctx:grammar_safetalkParser.ObjectContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#object.
    def exitObject(self, ctx:grammar_safetalkParser.ObjectContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#attribute.
    def enterAttribute(self, ctx:grammar_safetalkParser.AttributeContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#attribute.
    def exitAttribute(self, ctx:grammar_safetalkParser.AttributeContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#comparator.
    def enterComparator(self, ctx:grammar_safetalkParser.ComparatorContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#comparator.
    def exitComparator(self, ctx:grammar_safetalkParser.ComparatorContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#ambiguous_term.
    def enterAmbiguous_term(self, ctx:grammar_safetalkParser.Ambiguous_termContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#ambiguous_term.
    def exitAmbiguous_term(self, ctx:grammar_safetalkParser.Ambiguous_termContext):
        pass


    # Enter a parse tree produced by grammar_safetalkParser#explain_cmd.
    def enterExplain_cmd(self, ctx:grammar_safetalkParser.Explain_cmdContext):
        pass

    # Exit a parse tree produced by grammar_safetalkParser#explain_cmd.
    def exitExplain_cmd(self, ctx:grammar_safetalkParser.Explain_cmdContext):
        pass



del grammar_safetalkParser