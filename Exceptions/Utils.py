from Exceptions.ParametersException import ParametersException
from Exceptions.PrecomputationOTException import PrecomputationOTException
from Exceptions.PsiException import PsiException
from Exceptions.ValidationPsiException import ValidationPsiException

exceptionDict = {'[[[ERROR]]] ParametersException occurred: ': ParametersException,
                 '[[[ERROR]]] PsiException occurred: ': PsiException,
                 '[[[ERROR]]] PrecomputationOTException occurred: ': PrecomputationOTException,
                 '[[[ERROR]]] ValidationPsiException occurred: ': ValidationPsiException}