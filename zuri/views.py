from .serializers import ArithmeticSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST', 'GET'])
def arithmetic_operation(request):
    serializer = ArithmeticSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    x = serializer.validated_data['x']
    y = serializer.validated_data['y']
    operation_type = serializer.validated_data['operation_type']
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