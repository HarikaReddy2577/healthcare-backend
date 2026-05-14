from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import MappingCreateSerializer, MappingDetailSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mapping_list_create(request):
    if request.method == 'GET':
        mappings = PatientDoctorMapping.objects.all()
        serializer = MappingDetailSerializer(mappings, many=True)
        return Response({'success': True, 'count': mappings.count(), 'data': serializer.data})

    serializer = MappingCreateSerializer(data=request.data)
    if serializer.is_valid():
        mapping = serializer.save()
        detail = MappingDetailSerializer(mapping)
        return Response({'success': True, 'message': 'Doctor assigned to patient.', 'data': detail.data}, status=status.HTTP_201_CREATED)
    return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mappings_by_patient(request, patient_id):
    mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
    if not mappings.exists():
        return Response({'success': True, 'message': 'No doctors assigned to this patient.', 'data': []})
    serializer = MappingDetailSerializer(mappings, many=True)
    return Response({'success': True, 'count': mappings.count(), 'data': serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def mapping_delete(request, pk):
    try:
        mapping = PatientDoctorMapping.objects.get(pk=pk)
    except PatientDoctorMapping.DoesNotExist:
        return Response({'success': False, 'message': 'Mapping not found.'}, status=status.HTTP_404_NOT_FOUND)
    mapping.delete()
    return Response({'success': True, 'message': 'Doctor removed from patient.'}, status=status.HTTP_200_OK)
