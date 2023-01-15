from typing import List, NamedTuple

WeightedData = NamedTuple('WeightedData', [
    ('data', any),
    ('weight', int),
])

class Provincia:
    def __init__(self, name: str):
        self.name = name
provincias_weighted_data = [
    WeightedData(Provincia('Azuay'), weight=1),
    WeightedData(Provincia('Bolívar'), weight=1),
    WeightedData(Provincia('Cañar'), weight=1),
    WeightedData(Provincia('Carchi'), weight=1),
    WeightedData(Provincia('Chimborazo'), weight=1),
    WeightedData(Provincia('Cotopaxi'), weight=1),
    WeightedData(Provincia('El Oro'), weight=1),
    WeightedData(Provincia('Esmeraldas'), weight=1),
    WeightedData(Provincia('Galápagos'), weight=1),
    WeightedData(Provincia('Guayas'), weight=2),
    WeightedData(Provincia('Imbabura'), weight=1),
    WeightedData(Provincia('Loja'), weight=1),
    WeightedData(Provincia('Los Ríos'), weight=1),
    WeightedData(Provincia('Manabí'), weight=1),
    WeightedData(Provincia('Morona-Santiago'), weight=1),
    WeightedData(Provincia('Napo'), weight=1),
    WeightedData(Provincia('Orellana'), weight=1),
    WeightedData(Provincia('Pastaza'), weight=1),
    WeightedData(Provincia('Pichincha'), weight=3),
    WeightedData(Provincia('Santa Elena'), weight=1),
    WeightedData(Provincia('Santo Domingo de los Tsáchilas'), weight=1),
    WeightedData(Provincia('Sucumbíos'), weight=1),
    WeightedData(Provincia('Tungurahua'), weight=1),
    WeightedData(Provincia('Zamora-Chinchipe'), weight=1),
]
provincias_data: List[Provincia] = [f.data for f in provincias_weighted_data]
provincias_weight: List[int] = [f.weight for f in provincias_weighted_data]

class Motivo:
    def __init__(self, description: str):
        self.description = description
motivos_data: List[Motivo] = [
    Motivo('Ninguno'),  # Always should be the first one
    Motivo('Problemas de conexión'),
    Motivo('Problemas con pago del producto'),
    Motivo('Los beneficios no están claros'),
    Motivo('Cliente finaliza la operación sin completar el proceso de compra'),
    Motivo('Otros'),
]

class Servicio:
    def __init__(self, description: str, cost: float, time: int, benefits: str):
        self.description = description
        self.cost = cost
        self.time = time
        self.benefits = benefits
servicios_weighted_data = [
    WeightedData(Servicio('Seguro Basico', 50.7, 12, 'Control centralizado del automóvil'), weight=3),
    WeightedData(Servicio('Seguro Premium', 90.0, 12, 'Control centralizado del automóvil + Control App'), weight=2),
    WeightedData(Servicio('Seguro Gold', 180.0, 12, 'Control centralizado del automóvil + Control App + Monitoreo 24/7'), weight=1),
    WeightedData(Servicio('Seguro Deluxe', 240.0, 12, 'Control centralizado del automóvil + Control App + Monitoreo 24/7 + Seguro de robo'), weight=1),
]
servicios_data: List[Servicio] = [f.data for f in servicios_weighted_data]
servicios_weight: List[int] = [f.weight for f in servicios_weighted_data]

class Premio:
    def __init__(self, description: str, cost: float):
        self.description = description
        self.cost = cost
premios_data: List[Premio] = [
    Premio('Bono en la compra de llantas Michelin', 30.0),
    Premio('Moquetas para auto', 50.0),
    Premio('Juego de forros para asientos', 60.0),
    Premio('2 tanqueadas de súper en gasolineras Primax', 60.0),
    Premio('Abrillantador para auto ', 40.0)
]

total_provincias = len(provincias_data)
total_motivos = len(motivos_data)
total_servicios = len(servicios_data)
