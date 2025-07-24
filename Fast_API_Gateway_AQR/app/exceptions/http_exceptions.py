from fastapi import HTTPException, status

def cliente_no_encontrado_exception():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No encontrado en la base de datos"
    )

def cliente_existente_exception():
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Ya existe un cliente con ese id"
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
