

# PRÉSTAMO def getAllPrestamo(self): self.cursor.execute( "SELECT prestamo.id, socio.id, socio.apellido, socio.nombre, socio.email, socio.celular, socio.direccion, socio.documentacion, socio.responsable, bibliotecaria.nombre, bibliotecaria.apellido, libro.titulo,
libro.id, prestamo.fechainicio, prestamo.fechadevolucion, prestamo.estado FROM socio, bibliotecaria, libro, prestamo WHERE socio.id = prestamo.idsocio AND bibliotecaria.email = prestamo.idbibliotecaria AND libro.id = prestamo.idlibro ORDER BY prestamo.id")
prestamo = self.cursor.fetchall() return prestamo