from fastapi import HTTPException, status

def cuenta_no_encontrada_exception():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Cuenta no encontrada"
    )

def cuenta_existente_exception():
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Ya existe una cuenta con ese nombre"
    )

def error_crear_cuenta_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar crear la cuenta"
    )

def error_eliminar_cuenta_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar eliminar la cuenta"
    )

