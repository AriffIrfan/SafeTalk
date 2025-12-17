# Generated from grammar_safetalk.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammar_safetalkParser import grammar_safetalkParser
else:
    from grammar_safetalkParser import grammar_safetalkParser

# This class defines a complete generic visitor for a parse tree produced by grammar_safetalkParser.

class grammar_safetalkVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammar_safetalkParser#program.
    def visitProgram(self, ctx:grammar_safetalkParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#statement.
    def visitStatement(self, ctx:grammar_safetalkParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#command.
    def visitCommand(self, ctx:grammar_safetalkParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#assignment.
    def visitAssignment(self, ctx:grammar_safetalkParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#expression.
    def visitExpression(self, ctx:grammar_safetalkParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#term.
    def visitTerm(self, ctx:grammar_safetalkParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#factor.
    def visitFactor(self, ctx:grammar_safetalkParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#conditional.
    def visitConditional(self, ctx:grammar_safetalkParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#logic_expr.
    def visitLogic_expr(self, ctx:grammar_safetalkParser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#condition_cl.
    def visitCondition_cl(self, ctx:grammar_safetalkParser.Condition_clContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#modifier.
    def visitModifier(self, ctx:grammar_safetalkParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#value.
    def visitValue(self, ctx:grammar_safetalkParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#verb.
    def visitVerb(self, ctx:grammar_safetalkParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#object.
    def visitObject(self, ctx:grammar_safetalkParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#attribute.
    def visitAttribute(self, ctx:grammar_safetalkParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#comparator.
    def visitComparator(self, ctx:grammar_safetalkParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#ambiguous_term.
    def visitAmbiguous_term(self, ctx:grammar_safetalkParser.Ambiguous_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar_safetalkParser#explain_cmd.
    def visitExplain_cmd(self, ctx:grammar_safetalkParser.Explain_cmdContext):
        return self.visitChildren(ctx)



del grammar_safetalkParser