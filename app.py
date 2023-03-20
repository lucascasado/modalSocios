

# -----------------------------------------  PRESTAMO  -----------------------------------------
# -----------  SHOW PRESTAMO  -----------
from flask import render_template


@app.route('/showPrestamo')
@login_required
def showPrestamo():
    dataPrestamo = db.getAllPrestamo()
    return render_template('show_prestamo.html', prestamos=dataPrestamo)