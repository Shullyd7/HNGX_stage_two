from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def person_api_view(request):
    if request.method == 'GET':
        # Retrieve details of a person by either name or ID
        name = request.query_params.get('name', None)
        person_id = request.query_params.get('id', None)

        if name is not None:
            # Search by name
            try:
                person = Person.objects.get(name=name)
                serializer = PersonSerializer(person)
                return Response(serializer.data)
            except Person.DoesNotExist:
                return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        elif person_id is not None:
            # Search by ID
            try:
                person = Person.objects.get(pk=person_id)
                serializer = PersonSerializer(person)
                return Response(serializer.data)
            except Person.DoesNotExist:
                return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Please provide either "name" or "id" as a query parameter'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
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

    elif request.method == 'PUT':
        # UPDATE operation
        id = request.data.get('id', None)
        if id is None:
            return Response({'error': 'The "id" field is required in the request data for the PUT operation.'}, status=status.HTTP_400_BAD_REQUEST)

        updated_name = request.data.get('name', '')

        # Check if the person with the given ID exists
        try:
            person = Person.objects.get(pk=id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        # Validate that the "name" field is a string
        if not isinstance(updated_name, str):
            return Response({'error': 'The "name" field should be a string.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the updated name is the same as any existing name
        if Person.objects.exclude(pk=id).filter(name=updated_name).exists():
            return Response({'error': 'A person with the updated name already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(person, data={'name': updated_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # DELETE operation based on ID or name
        id = request.data.get('id', None)
        name = request.data.get('name', None)

        if id is not None:
            try:
                person = Person.objects.get(pk=id)
                person.delete()
                return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Person.DoesNotExist:
                return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        if name is not None:
            try:
                person = Person.objects.get(name=name)
                person.delete()
                return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Person.DoesNotExist:
                return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Either "id" or "name" field is required in the request data for the DELETE operation.'}, status=status.HTTP_400_BAD_REQUEST)