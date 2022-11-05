from .serializers import ArithmeticSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def arithmetic_operation(request):
    """
    A function that helps in performing a simple arithmetic operation by either
    getting it operand from a long string or  directly using the serializer
    Args:
        (i) operation type
        (ii) value (x and y)
    Response:
        
        (i) "slackUsername"
        (ii) "operation_type"
        (iii) "result"
    """


    KEYWORDS = ['add','subtract','multiply','addition', 'sum','subtraction','multiplication', 'product']
    # check the operation type length first becuase it will throw an error if a long string is passed 
    # which won't correspond with the Enum and django choices that was used in the serializer and model
    data_type = request.data['operation_type']
    if len(data_type) == 1:
        serializer = ArithmeticSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        x = serializer.validated_data['x']
        y = serializer.validated_data['y']
        if type(x or y) !=int:
            return Response("x and y must be an integer", status=status.HTTP_400_BAD_REQUEST)
        operation_type = serializer.validated_data['operation_type']
        operation_type_list = operation_type.split()
        if len(operation_type_list) == 1:
            if operation_type == 'addition':
                result = x + y
            elif operation_type == 'subtraction':
                result = x - y
            elif operation_type == 'multiplication':
                result = x * y
            context = {
                "slackUsername": "Tech-matt",
                "operation_type": operation_type,
                "result": result
            }
            return Response(context, status=status.HTTP_200_OK)  
    else:    
            
        operation_type = request.data['operation_type']
        operation_type_list = operation_type.split()
        print(operation_type_list)
        x = int(request.data['x'])
        y = int(request.data['y'])
        # assign the calue of item from the loop to match variable and check
        #  if there's any value like that in the keywords list
        if any((match := item)  in operation_type_list for item in KEYWORDS):
            print(match)
            operation = match  
            # cleaned = [ x for x in operation_type_list if x.isdigit() ]
            if operation ==  'add' or operation ==  'addition':
                operation_type = 'addition'
                result = x + y
            elif operation ==  'subtract' or operation == 'subtraction':
                operation_type = 'subtraction'
                result = x - y
            elif operation ==  'multiplication' or operation == 'multiply' or operation== 'product':
                operation_type = 'multiplication'
                result = x * y
            context = {
                "slackUsername": "Tech-matt",
                "operation_type": operation_type,
                "result": result
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(
            "bad request, enter a valid input", 
            status=status.HTTP_400_BAD_REQUEST
            )  




