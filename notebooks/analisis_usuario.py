import pandas as pd

data_frame_usuarios = pd.read_excel("./data/usuarios_sistema_completo.xlsx")
print(data_frame_usuarios)

print(data_frame_usuarios['especialidad'].unique)
print(data_frame_usuarios['tipo_usuario'].unique)


#1. Solo estudiantes
usuarios_estudiantes=data_frame_usuarios.query('tipo_usuario == "estudiante"')
print(usuarios_estudiantes)
#2. Solo profesores
usuarios_docentes=data_frame_usuarios.query('tipo_usuario == "docente"')
print(usuarios_docentes)
#3. Todos excepto estudiantes
todos_excepto_estudiantes=data_frame_usuarios.query('tipo_usuario != "estudiante"')
print(todos_excepto_estudiantes)
#4. Filtrar por especialidad
especialidad_usuarios=data_frame_usuarios['especialidad'].unique()
print(especialidad_usuarios)
#5. Excluir una especialidad
especialidad_usuarios=data_frame_usuarios.query('especialidad != "Ingenieria de Sistemas"')
print(especialidad_usuarios)
#6. Excluir administrativos
usuarios_sin_administrativos = data_frame_usuarios.query('tipo_usuario != "administrativo"')
print(usuarios_sin_administrativos)
#7. Direcciones en medellin
usuarios_en_medellin = data_frame_usuarios[data_frame_usuarios['direccion'].str.contains('Medellín', case=False, na=False)]
print(usuarios_en_medellin)
#8. Direcciones terminadas en sur
#usuarios_direccion_sur = data_frame_usuarios[data_frame_usuarios['direccion'].str.endswith('sur', case=False, na=False)]
#print(usuarios_direccion_sur)
#9. Direcciones que inician con calle
usuarios_direccion_calle = data_frame_usuarios[data_frame_usuarios['direccion'].str.startswith('Calle', case=False, na=False)]
print(usuarios_direccion_calle)
#10.Especialidades que contienen la palabra datos
#11. instructores en itagui
#12. nacidos despues de 2000
#13. nacidos en los 90
#14. direcciones en envigado
#15. especialdiades que empizan por I
#16. usuarios sin direccion
#17. usuarios sin especialidad
usuarios_sin_especialidad=data_frame_usuarios['especialidad'].isna()
print(usuarios_sin_especialidad)
#18. profesores que viven en sabaneta
#19. aprendices que viven en bello
#20. nacidos en el nuevo milenio


#1. total por tipo
#2. total por especialidad
#3. cantidad de especialidades distintas
#4. tipos de usuario por especialidad
#5. usuario mas antiguo por tipo
#6. usuario mas joven por tipo
#7. primer registro por tipo
#8. ultimo registro por tipo
#9. combinacion tipo por especialidad
#10. el mas viejo por especialidad
#11. cuantos de cada especialidad por tipo
#12. edad promedio por tipo
#13. años de nacimeinto mas frecuente por especialidad
#14. mes de nacimiento ams frecuente por tipo
#15. UNA CONSULTA O FILTRO QUE UD PROPONGA