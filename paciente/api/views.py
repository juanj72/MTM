from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from paciente.models import *
from paciente.api.serializers import PacienteSerializer
from paciente.api.serializers import PacientePadrinoSerializer
from paciente.api.serializers import PacienteFamiliarSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import connection
from rest_framework.response import Response


class PacienteApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # permission_classes = [IsAuthenticated]

class PacientePadrinoApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = padrino.objects.all()
    serializer_class = PacientePadrinoSerializer
    # permission_classes = [IsAuthenticated]

class PacienteFamiliarApiViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = familiar.objects.all()
    serializer_class = PacienteFamiliarSerializer
    # permission_classes = [IsAuthenticated]


class pacientes_padrinos(APIView):
    def get(self,request,id):
        with connection.cursor() as cursor:  # Activamos un cursor para las consultas a la BD
            consulta = f"""
        SELECT 
    pd.nombre, pd.apellido, pd.id, pd.correo
FROM
    padrino pd
        INNER JOIN
    paciente_padrino pp ON pp.padrino_id = pd.id
WHERE
    pp.paciente_id = {id}

            """
        # Ejecutar una linea SQL En este caso llamamos un procedimiento almacenado
            cursor.execute(consulta)

            columns = []  # Para guardar el nombre de las columnas

            # Recorrer la descripcion (Nombre de la columna)
            for column in cursor.description:

                columns.append(column[0])  # Guardando el nombre de las columnas

            data = []  # Lista con los datos que vamos a enviar en JSON

            for row in cursor.fetchall():  # Recorremos las fila guardados de la BD

                # Insertamos en data un diccionario
                data.append(dict(zip(columns, row)))

            cursor.close()  # Se cierra el cursor para que se ejecute el procedimiento almacenado

            connection.commit()  # Enviamos la sentencia a la BD
            connection.close()  # Cerramos la conección

        return Response(data)