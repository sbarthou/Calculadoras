print('\nIngresar números decimales separados por un "."')
print('-----------------------------------------------')

medida = input('m/s - km/s - m/h - km/h: ')
valor = float(input('Valor: '))

redondear = input('Redondear valores? si(s)/no(n): ')
if redondear == 's' or redondear == 'si':
    redondear = 'si'
    decimales = int(input('Número de decimales: '))
print('')


if medida == 'm/s':
    km_s = valor/1000
    m_h = valor*3600
    km_h = (valor/1000)*3600
    if redondear == 'si':
        print(f'{valor} m/s son {round(km_s, decimales)} km/s')
        print(f'{valor} m/s son {round(m_h, decimales)} m/h')
        print(f'{valor} m/s son {round(km_h, decimales)} km/h')
    else:
        print(f'{valor} m/s son {km_s} km/s')
        print(f'{valor} m/s son {m_h} m/h')
        print(f'{valor} m/s son {km_h} km/h')
        
if medida == 'km/s':
    m_s = valor*1000
    m_h = valor*3600
    km_h = (valor*1000)*3600
    if redondear == 'si':
        print(f'{valor} km/s son {round(m_s, decimales)} m/s')
        print(f'{valor} km/s son {round(m_h, decimales)} m/h')
        print(f'{valor} km/s son {round(km_h, decimales)} km/h')
    else:
        print(f'{valor} km/s son {m_s} m/s')
        print(f'{valor} km/s son {m_h} m/h')
        print(f'{valor} km/s son {km_h} km/h')
        
if medida == 'm/h':
    m_s = valor/3600
    km_s = (valor/3600)/1000
    km_h = valor/1000
    if redondear == 'si':
        print(f'{valor} m/h son {round(m_s, decimales)} m/s')
        print(f'{valor} m/h son {round(km_s, decimales)} km/s')
        print(f'{valor} m/h son {round(km_h, decimales)} km/h')
    else:
        print(f'{valor} m/h son {m_s} m/s')
        print(f'{valor} m/h son {km_s} km/s')
        print(f'{valor} m/h son {km_h} km/h')
        
if medida == 'km/h':
    m_s = valor/3.6
    km_s = valor/3600
    m_h = valor*1000
    if redondear == 'si':
        print(f'{valor} km/h son {round(m_s, decimales)} m/s')
        print(f'{valor} km/h son {round(km_s, decimales)} km/s')
        print(f'{valor} km/h son {round(m_h, decimales)} m/h')
    else:
        print(f'{valor} km/h son {m_s} m/s')
        print(f'{valor} km/h son {km_s} km/s')
        print(f'{valor} km/h son {m_h} m/h')