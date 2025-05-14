import pandas as pd

data_frame_usuarios = pd.read_excel("./data/usuarios_sistema_completo.xlsx")
print(data_frame_usuarios)

print(data_frame_usuarios['especialidad'].unique)
print(data_frame_usuarios['tipo_usuario'].unique)
print(data_frame_usuarios['fecha_nacimiento'].unique)


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
total_por_tipo = data_frame_usuarios['tipo_usuario'].value_counts()
print("Total por tipo de usuario:\n", total_por_tipo)
#2. total por especialidad
total_por_especialidad = data_frame_usuarios['especialidad'].value_counts()
print("Total por especialidad:\n", total_por_especialidad)
#3. cantidad de especialidades distintas
num_especialidades = data_frame_usuarios['especialidad'].nunique()
print("Número de especialidades distintas:", num_especialidades)
#4. tipos de usuario por especialidad
tipos_por_especialidad = data_frame_usuarios.groupby('especialidad')['tipo_usuario'].unique()
print("Tipos de usuario por especialidad:\n", tipos_por_especialidad)
#5. usuario mas antiguo por tipo
usuarios_con_fecha_valida = data_frame_usuarios[data_frame_usuarios['fecha_nacimiento'].notna()]
idx_mas_antiguo_por_tipo = usuarios_con_fecha_valida.groupby('tipo_usuario')['fecha_nacimiento'].idxmin()
usuario_mas_antiguo_por_tipo = data_frame_usuarios.loc[idx_mas_antiguo_por_tipo]
print("Usuario más antiguo por tipo:\n", usuario_mas_antiguo_por_tipo)
#6. usuario mas joven por tipo
usuarios_validos = data_frame_usuarios[data_frame_usuarios['fecha_nacimiento'].notna()]
idx_mas_joven = usuarios_validos.groupby('tipo_usuario')['fecha_nacimiento'].idxmax()
usuario_mas_joven_por_tipo = data_frame_usuarios.loc[idx_mas_joven]
print("Usuario más joven por tipo:\n", usuario_mas_joven_por_tipo)
#7. primer registro por tipo
primer_registro_por_tipo = data_frame_usuarios.groupby('tipo_usuario').first()
print("Primer registro por tipo:\n", primer_registro_por_tipo)
#8. ultimo registro por tipo
ultimo_registro_por_tipo = data_frame_usuarios.groupby('tipo_usuario').last()
print("Último registro por tipo:\n", ultimo_registro_por_tipo)
#9. combinacion tipo por especialidad
combinacion_tipo_especialidad = pd.crosstab(data_frame_usuarios['especialidad'], data_frame_usuarios['tipo_usuario'])
print("Combinación tipo por especialidad:\n", combinacion_tipo_especialidad)
#10. el mas viejo por especialidad
usuarios_validos = data_frame_usuarios[data_frame_usuarios['fecha_nacimiento'].notna()]
idx_mas_viejo = usuarios_validos.groupby('especialidad')['fecha_nacimiento'].idxmin()
mas_viejo_por_especialidad = data_frame_usuarios.loc[idx_mas_viejo]
print("Usuario más viejo por especialidad:\n", mas_viejo_por_especialidad)
#11. cuantos de cada especialidad por tipo
cantidad_por_tipo_y_especialidad = data_frame_usuarios.groupby(['tipo_usuario', 'especialidad']).size().unstack(fill_value=0)
print("Cantidad por tipo y especialidad:\n", cantidad_por_tipo_y_especialidad)
#12. edad promedio por tipo
hoy = pd.Timestamp.today()
data_frame_usuarios['edad'] = (hoy - data_frame_usuarios['fecha_nacimiento']).dt.days // 365
edad_promedio_por_tipo = data_frame_usuarios.groupby('tipo_usuario')['edad'].mean()
#13. años de nacimeinto mas frecuente por especialidad
data_frame_usuarios['anio_nacimiento'] = data_frame_usuarios['fecha_nacimiento'].dt.year
anio_frecuente_por_especialidad = data_frame_usuarios.groupby('especialidad')['anio_nacimiento'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
print("Año de nacimiento más frecuente por especialidad:\n", anio_frecuente_por_especialidad)
#14. mes de nacimiento ams frecuente por tipo
data_frame_usuarios['mes_nacimiento'] = data_frame_usuarios['fecha_nacimiento'].dt.month
mes_frecuente_por_tipo = data_frame_usuarios.groupby('tipo_usuario')['mes_nacimiento'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
print("Mes de nacimiento más frecuente por tipo:\n", mes_frecuente_por_tipo)
#15. UNA CONSULTA O FILTRO QUE UD PROPONGA
usuarios_con_numeros_en_direccion = data_frame_usuarios[data_frame_usuarios['direccion'].str.contains(r'\d', na=False)]
print("Usuarios con números en su dirección:\n", usuarios_con_numeros_en_direccion)