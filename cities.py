def get_connected_cities():
    cities = {
        'Aveiro': {'Porto': 68, 'Viseu': 95, 'Coimbra': 68, 'Leiria': 115},
        'Braga': {'Viana do Castelo': 48, 'Vila Real': 106, 'Porto': 53},
        'Bragança': {'Vila Real': 137, 'Guarda': 202},
        'Beja': {'Évora': 78, 'Faro': 152, 'Setúbal': 142},
        'Castelo Branco': {'Coimbra': 159, 'Guarda': 106, 'Portalegre': 80, 'Évora': 203},
        'Coimbra': {'Viseu': 96, 'Leiria': 67, 'Aveiro': 68, 'Castelo Branco': 159},
        'Évora': {'Lisboa': 150, 'Santarém': 117, 'Portalegre': 131, 'Setúbal': 103, 'Beja': 78, 'Castelo Branco': 203},
        'Faro': {'Setúbal': 249, 'Lisboa': 299, 'Beja': 152},
        'Guarda': {'Vila Real': 157, 'Viseu': 85, 'Bragança': 202, 'Castelo Branco': 106},
        'Leiria': {'Lisboa': 129, 'Santarém': 70, 'Aveiro': 115, 'Coimbra': 67},
        'Lisboa': {'Santarém': 78, 'Setúbal': 50, 'Évora': 150, 'Faro': 299, 'Leiria': 129},
        'Portalegre': {'Castelo Branco': 80, 'Évora': 131},
        'Porto': {'Viana do Castelo': 71, 'Vila Real': 116, 'Viseu': 133, 'Aveiro': 68, 'Braga': 53},
        'Santarém': {'Évora': 117, 'Leiria': 70, 'Lisboa': 78},
        'Setúbal': {'Beja': 142, 'Évora': 103, 'Faro': 249, 'Lisboa': 50},
        'Viana do Castelo': {'Braga': 48, 'Porto': 71},
        'Vila Real': {'Viseu': 110, 'Braga': 106, 'Bragança': 137, 'Guarda': 157, 'Porto': 116},
        'Viseu': {'Aveiro': 95, 'Coimbra': 96, 'Guarda': 85, 'Porto': 133, 'Vila Real': 110}
    }
    return cities


def get_straight_line_cities():
    straight_line_cities = {
        'Aveiro': ['Porto', 'Viseu', 'Coimbra', 'Leiria'],
        'Braga': ['Viana do Castelo', 'Vila Real', 'Porto'],
        'Bragança': ['Vila Real', 'Guarda'],
        'Beja': ['Évora', 'Faro', 'Setúbal'],
        'Castelo Branco': ['Coimbra', 'Guarda', 'Portalegre', 'Évora'],
        'Coimbra': ['Viseu', 'Leiria', 'Aveiro', 'Castelo Branco'],
        'Évora': ['Lisboa', 'Santarém', 'Portalegre', 'Setúbal', 'Beja', 'Castelo Branco'],
        'Faro': ['Setúbal', 'Lisboa', 'Beja'],
        'Guarda': ['Vila Real', 'Viseu', 'Bragança', 'Castelo Branco'],
        'Leiria': ['Lisboa', 'Santarém', 'Aveiro', 'Coimbra'],
        'Lisboa': ['Santarém', 'Setúbal', 'Évora', 'Faro', 'Leiria'],
        'Porto': ['Viana do Castelo', 'Vila Real', 'Viseu', 'Aveiro', 'Braga'],
        'Vila Real': ['Viseu', 'Braga', 'Bragança', 'Guarda', 'Porto'],
        'Viseu': ['Aveiro', 'Guarda', 'Porto', 'Vila Real', 'Coimbra'],
        'Setúbal': ['Beja', 'Évora', 'Faro', 'Lisboa'],
        'Viana do Castelo': ['Braga', 'Porto'],
        'Santarém': ['Évora', 'Leiria', 'Lisboa'],
        'Portalegre': ['Castelo Branco', 'Évora']
    }

    return straight_line_cities
