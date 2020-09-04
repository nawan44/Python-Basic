dict_ind_eng ={
    'anak' : 'son', 'istri' :'wife' , 'ayah' : 'father', 'ibu' : 'mother'
}

print(dict_ind_eng)
print(dict_ind_eng['ayah'])
print(dict_ind_eng['ibu'])


print('This data send with server')
data_from_server ={
    'date' : '2020 - 09 - 12',
    'name' : ['Rachmat', 'Gunawan', 'Saputra', 'Gundul'],
    'skill' : [{'web' : 'HTML CSS', 'spesifik' :'frontend'}, {'3d':'3dmax', 'spesifik':'modelling'}, {'Game' : 'Unity 3D', 'spesifik': '3D Game'}]
}

print(data_from_server)
print(f"Name {data_from_server['name']}")
print(f"Name #1 {data_from_server['name'][2]}")
print(f"Name {data_from_server['name'][3]}")
print(f"Skill {data_from_server['skill'][1]}")
print(f"Skill {data_from_server['skill'][0]['spesifik']} developer")