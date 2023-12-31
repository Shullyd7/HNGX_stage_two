from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status



@api_view(['GET', 'PUT', 'DELETE'])
def get_person_by_id(request, user_id):
    if request.method == 'GET':
        #READ operation
        try:
            person = Person.objects.get(pk=user_id)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        # UPDATE operation
        updated_name = request.data.get('name', '')

        # Check if the person with the given ID exists
        try:
            person = Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        # Validate that the "name" field is a string
        if not isinstance(updated_name, str):
            return Response({'error': 'The "name" field should be a string.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the updated name is the same as any existing name
        if Person.objects.exclude(pk=user_id).filter(name=updated_name).exists():
            return Response({'error': 'A person with the updated name already exists.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(person, data={'name': updated_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # DELETE operation based on ID
        try:
            person = Person.objects.get(pk=user_id)
            person.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'error': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST', 'GET'])
def person_api_view(request):
    if request.method == 'POST':
        # CREATE operation
        name = request.data.get('name', '')

        # Validate that the "name" field is a string
        if not isinstance(name, str):
            return Response({'error': 'The "name" field should be a string.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a person with the same name already exists
        if Person.objects.filter(name=name).exists():
            return Response({'error': 'A person with the same name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(data={'name': name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    return Response({'error': 'Invalid HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)