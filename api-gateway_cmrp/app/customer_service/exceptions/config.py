from fastapi import HTTPException, status

def CLIENTE_no_encontrado_exception():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Cliente no encontrado"
    )

def cliente_existente_exception():
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Ya existe un cliente con ese nombre"
    )

def error_crear_cliente_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar crear el cliente"
    )

def error_eliminar_cliente_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar eliminar el cliente"
    )

def error_eliminar_cliente_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar eliminar el cliente"
    )
