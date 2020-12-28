from Exceptions.ParametersException import ParametersException
from Exceptions.PrecomputationOTException import PrecomputationOTException
from Exceptions.PsiException import PsiException
from Exceptions.ValidationPsiException import ValidationPsiException

exceptionDict = {'[[[ERROR]]] ParametersException occured: ': ParametersException,
                 '[[[ERROR]]] PsiException occured: ': PsiException,
                 '[[[ERROR]]] PrecomputationOTException occured: ': PrecomputationOTException,
                 '[[[ERROR]]] ValidationPsiException occurred: ': ValidationPsiException}