if __name__ != "__main__":
    # Using an absolute import
    # from users.manage.crud import guardar

    # .. -> It is a relative import and It allows you to import
    # modules that are higher in our hierachy
    from ..manage.crud import guardar

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()

else:
    print("la ejecucion inicio desde utils")

print(__name__)
