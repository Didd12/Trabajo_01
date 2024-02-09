#Funcion que sirve para agregar la fecha de inicio de reparacion del producto
def añadir_fecha_ingreso(fechas):
    fecha_ingreso = {}
    fecha_reparacion = input("Ingrese la fecha de inicio de reparacion:")
    fecha_ingreso['Fecha de ingreso:'] = fecha_reparacion
    fechas.append(fecha_ingreso)

#Funcion que sirve para agregar la fecha de culminacion de la reparacion
def añadir_fecha_orden_lista(fechas):
    fecha_orden_lista = {}
    fechaOrdenLista = input("Ingrese la fecha de culminacion de la reparacion:")
    fecha_orden_lista['Fecha de culminacion del trabajo:'] = fechaOrdenLista
    fechas.append(fecha_orden_lista)

#Funcion que sirve para agregar la fecha de de retiro del producto
def añadir_fecha_retiroProducto(fechas):
    fecha_retiro_producto = {}
    fechaRetiroProducto = input("Ingrese la fecha de retiro del producto:")
    fecha_retiro_producto['Fecha de Retiro del Producto:'] = fechaRetiroProducto
    fechas.append(fecha_retiro_producto)
    
#Funcion que sirve para agregar el tipo de orden
def tipo_orden(ordenes):
    tipo_orden = {}
    tipoOrden = input("Ingrese el tipo de orden:")
    tipo_orden['Tipo de Orden:'] = tipoOrden
    ordenes.append(tipo_orden)

#Funcion que sirve para agregar clientes
def clientes(cliente):
    clientes = {}
    cliente_ingresado = input("Ingrese el nombre del cliente:")
    clientes['Nombre del Cliente:'] = cliente_ingresado
    cliente.append(clientes)
    
def tecnicos(tecnico):
    tecnicos = {}
    tecnico_ingresado = input("Ingrese el nombre del cliente ")
    
    

