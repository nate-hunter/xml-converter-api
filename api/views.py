from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from api import serializers

import lxml.etree as etree
import csv
import os


class ConverterApiView(APIView):
	"""XML Converter APIView"""

	serializer_class = serializers.ConverterSerializer

	def get(self, request, format=None):
		return Response('GET not allowed.')

	def post(self, request):
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			studio = serializer.validated_data.get('studio')
			directory = serializer.validated_data.get('directory')

			# seri_data = {'studio': studio_select, 'directory': directory}
			seri_data = serializer.data

			# content = JSONRenderer().render()

			file_list = []
			studio_select = ''

			for filename in os.scandir(directory):
				if filename.is_file() and filename.name.endswith('.xml'):
					file = os.path.join(directory, filename)
					file_list.append(file)
					if studio.lower() == "a&e":
						studio_select = studio
					elif studio.lower() == "disney":
						studio_select = studio
					elif studio.lower() == 'discovery':
						studio_select = studio
					else:
						studio_select = "'" + studio + "' is not set up to convert XMLs to CSV at this time."
						break


			return Response({
				'json?': seri_data,
				'path': directory,
				'studio': studio_select,
				'file_list': file_list,
			})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

		# if serializer.is_valid():
		# 	studio = serializer.validated_data.get('studio')
		# 	directory = serializer.validated_data.get('directory')
		# 	# directory = 'C:\\Box\\EST & Streampix\\Metadata By Month\\2020\\7. July\\TV\\Disney\\30 For 30'
		# 	# print('\tDIRECTORY --> ' + directory)
		# 	test = serializer.validated_data.get('pathTest')
		# 	list_data = []
		# 	for filename in os.listdir(directory):
		# 		list_data.append(filename)
		# 		if filename.endswith(".xml"):
		# 			# file = os.path.join(directory, filename)
		# 			if studio.lower() == "a&e":
		# 				list_data.append(studio)
		# 			elif studio.lower() == "disney":
		# 				list_data.append(studio)
		# 			elif studio.lower() == 'discovery':
		# 				list_data.append(studio)
		# 			else:
		# 				list_data.append("'" + studio + "' is not set up to convert XMLs to CSV at this time.")
		# 				break
		# 	return Response({'msg': directory, 'file': list_data})
		# else:
		# 	return Response(
		# 		serializer.errors,
		# 		status=status.HTTP_400_BAD_REQUEST
		# 	)