## NOR-INT-05 · Falta de cama: espera o derivación

§1. Si al recibir la indicación de internación hay una cama libre que cumple NOR-INT-01 a NOR-INT-04, se interna al paciente en ella dentro del plazo fijado en el parámetro P-INT-5, contado desde la indicación. Las camas reservadas para un ingreso programado no están disponibles.

§2. Si no hay una cama así, se consulta el tablero de camas del sector. Si un alta prevista va a dejar disponible una cama adecuada dentro del tiempo máximo de espera del sector, contado desde la indicación (parámetros P-INT-1 para la UTI, P-INT-2 para la UCO y P-INT-3 para la sala general), el paciente espera en la guardia y se lo interna cuando la cama queda libre, dentro del plazo fijado en el parámetro P-INT-5, contado desde ese momento.

§3. Si no hay cama adecuada ni un alta prevista que la deje disponible dentro de ese tiempo, el paciente se deriva a otro establecimiento según NOR-DER-01.

§4. Si mientras el paciente espera el médico modifica la indicación, esta sección se vuelve a aplicar con la indicación nueva, desde el momento en que se la recibe.
