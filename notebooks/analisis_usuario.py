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
usuarios_medellin = data_frame_usuarios[data_frame_usuarios['direccion'].str.contains('Medellin', case=False, na=False)]
print(usuarios_medellin)
#8. Direcciones terminadas en sur
usuarios_terminados_en_sur = data_frame_usuarios[data_frame_usuarios['direccion'].str.lower().str.endswith('sur', na=False)]
print(usuarios_terminados_en_sur)
#9. Direcciones que inician con calle
usuarios_inician_con_calle = data_frame_usuarios[data_frame_usuarios['direccion'].str.lower().str.startswith('calle', na=False)]
print(usuarios_inician_con_calle)
#10.Especialidades que contienen la palabra datos
usuarios_con_datos_en_especialidad = data_frame_usuarios[data_frame_usuarios['especialidad'].str.contains('datos', case=False, na=False)]
print(usuarios_con_datos_en_especialidad)
#11. instructores en itagui
usuarios_instructores_itagui = data_frame_usuarios[
    (data_frame_usuarios['tipo_usuario'].str.contains('instructor', case=False, na=False)) &
    (data_frame_usuarios['direccion'].str.contains('Itagüí', case=False, na=False))
]
print(usuarios_instructores_itagui)
#12. nacidos despues de 2000
data_frame_usuarios['fecha_nacimiento'] = pd.to_datetime(data_frame_usuarios['fecha_nacimiento'], errors='coerce') 

usuarios_nacidos_despues_2000 = data_frame_usuarios[data_frame_usuarios['fecha_nacimiento'].dt.year > 2000]
print(usuarios_nacidos_despues_2000)
#13. nacidos en los 90
usuarios_nacidos_en_90s = data_frame_usuarios[
    (data_frame_usuarios['fecha_nacimiento'].dt.year >= 1990) & 
    (data_frame_usuarios['fecha_nacimiento'].dt.year < 2000)
]
print(usuarios_nacidos_en_90s)
#14. direcciones en envigado
usuarios_envigado = data_frame_usuarios[data_frame_usuarios['direccion'].str.contains('Envigado', case=False, na=False)]
print(usuarios_envigado)
#15. especialdiades que empizan por I
usuarios_con_especialidad_I = data_frame_usuarios[data_frame_usuarios['especialidad'].str.lower().str.startswith('i', na=False)]
print(usuarios_con_especialidad_I)
#16. usuarios sin direccion
usuarios_sin_direccion = data_frame_usuarios[data_frame_usuarios['direccion'].isna()]
print(usuarios_sin_direccion)
#17. usuarios sin especialidad
usuarios_sin_especialidad = data_frame_usuarios[data_frame_usuarios['especialidad'].isna()]
print(usuarios_sin_especialidad)
#18. profesores que viven en sabaneta
profesores_sabaneta = data_frame_usuarios[
    (data_frame_usuarios['tipo_usuario'] == 'profesor') & 
    (data_frame_usuarios['direccion'].str.contains('Sabaneta', case=False, na=False))
]
print(profesores_sabaneta)
#19. aprendices que viven en bello
aprendices_bello = data_frame_usuarios[
    (data_frame_usuarios['tipo_usuario'] == 'aprendiz') & 
    (data_frame_usuarios['direccion'].str.contains('Bello', case=False, na=False))
]
print(aprendices_bello)
#20. nacidos en el nuevo milenio
usuarios_nacidos_en_nuevo_milenio = data_frame_usuarios[
    (data_frame_usuarios['fecha_nacimiento'].dt.year >= 2000) &
    (data_frame_usuarios['fecha_nacimiento'].dt.year < 2025)
]
print(usuarios_nacidos_en_nuevo_milenio)


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