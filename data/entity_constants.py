from collections import namedtuple
from typing import List


provincias_name = [
    'Azuay',
    'Bolívar',
    'Cañar',
    'Carchi',
    'Chimborazo',
    'Cotopaxi',
    'El Oro',
    'Esmeraldas',
    'Galápagos',
    'Guayas',
    'Imbabura',
    'Loja',
    'Los Ríos',
    'Manabí',
    'Morona-Santiago',
    'Napo',
    'Orellana',
    'Pastaza',
    'Pichincha',
    'Santa Elena',
    'Santo Domingo de los Tsáchilas',
    'Sucumbíos',
    'Tungurahua',
    'Zamora-Chinchipe',
]

motivos_description = [
    'Ninguno',  # Always should be the first one
    'Problemas de conexión',
    'Problemas con pago del producto',
    'Los beneficios no están claros',
    'Cliente finaliza la operación sin completar el proceso de compra',
    'Otros',
]

Servicio = namedtuple('Servicio', ['description', 'cost', 'time', 'benefits'])
servicios_data: List[Servicio] = [
    Servicio('Seguro Basico', 50.7, 12, 'Control centralizado del automóvil'),
    Servicio('Seguro Premium', 90.0, 12,
             'Control centralizado del automóvil + Control App'),
    Servicio('Seguro Gold', 180.0, 12,
             'Control centralizado del automóvil + Control App + Monitoreo 24/7'),
    Servicio('Seguro Deluxe', 240.0, 12,
             'Control centralizado del automóvil + Control App + Monitoreo 24/7 + Seguro de robo'),
]

total_provincias = len(provincias_name)
total_motivos = len(motivos_description)
total_servicios = len(servicios_data)
