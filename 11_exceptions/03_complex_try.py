def serve_chai(flavor):
    try:
        print(f"ppreparing {flavor} chai ...")
        if flavor == 'unknown':
            raise ValueError("we dont know that flavor")
    except ValueError as e:
        print("Error ",e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")